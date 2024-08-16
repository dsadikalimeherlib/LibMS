import frappe
from frappe.utils import today
from frappe import _
from frappe.model.document import Document

class LibraryMembership(Document):

    def before_submit(self):
        duplicate_check_result = check_duplicate_membership(self.name, self.member)
        if duplicate_check_result.get('has_duplicate'):
            frappe.throw(_("Duplicate active membership service found: {0}").format(duplicate_check_result.get('duplicate_service')))
        
        self.membership_details_update()

    def membership_details_update(self):
        """Update the membership details in the Member document."""
        try:
            # Fetch Library Membership Details
            library_membership_details = frappe.get_all('Library Membership Details',
                                                        filters={'parent': self.name},
                                                        fields=['*'])
            for details in library_membership_details:
                # Update the Member document
                member_doc = frappe.get_doc("Member", self.member)
                child_table_entry = member_doc.append("membership_details", {})
                child_table_entry.library_membership = self.name
                child_table_entry.library_service = details.get('library_service')
                child_table_entry.from_date = details.get('from_date')
                child_table_entry.due_date = details.get('due_date')
                child_table_entry.membership_status = details.get('service_status')
                member_doc.membership_status = details.get('service_status')
                member_doc.save()
        except Exception as e:
            frappe.msgprint(_("An error occurred while updating membership details: {0}").format(str(e)))
    
    def auto_expired(self):
        """Automatically expire memberships whose end date is past."""
        try:
            expired_details = frappe.get_all("Library Membership", 
                                             filters={"to_date": ("<", today())}, 
                                             fields=["name", "to_date"])
            for expire in expired_details:
                member_doc = frappe.get_doc("Library Membership", expire.name)
                member_doc.membership_status = "Expired"
                member_doc.save()
                self.membership_details_update()
        except Exception as e:
            frappe.msgprint(_("An error occurred during auto-expiration: {0}").format(str(e)))

@frappe.whitelist()
def check_duplicate_membership(document_name, member):
    """Check for duplicate memberships and ensure they are not active."""
    try:
        new_service = frappe.get_all('Library Membership Details',
                                     filters={'parent': document_name},
                                     fields=['*'])
        existing_service = frappe.get_all('Membership Details',
                                          filters={'parent': member},
                                          fields=['*'])

        for ns in new_service:
            for es in existing_service:
                if ns['library_service'] == es['library_service'] and es['membership_status'] == 'Active':
                    return {
                        'has_duplicate': True,
                        'duplicate_service': ns['library_service']
                    }

        return {'has_duplicate': False}
    except Exception as e:
        frappe.msgprint(f"An error occurred while checking for duplicate membership: {str(e)}")
        return {'has_duplicate': False}
