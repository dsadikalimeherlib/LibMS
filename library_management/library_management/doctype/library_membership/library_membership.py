# Copyright (c) 2023, Ramjanali and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import today
from frappe import _
from frappe.model.document import Document

class LibraryMembership(Document):

    def validate(self):
        """Ensure no active duplicate memberships exist before submission."""
        #self.check_duplicate_membership()
        
    @frappe.whitelist()
    def on_submit(self):
        """Handle actions to be performed when the document is submitted."""
        # self.check_duplicate_membership()
        self.membership_details_update()
        frappe.msgprint("Membership submitted successfully. Additional actions can be performed here.")

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
    

    def check_duplicate_membership(self):
        """Check for duplicate memberships and ensure they are not active."""
        try:
            # Fetch new service details
            new_service = frappe.get_all('Library Membership Details',
                                         filters={'parent': self.name},
                                         fields=['*'])
            # Fetch existing service details from the Member
            existing_service = frappe.get_all('Membership Details',
                                              filters={'parent': self.member},
                                              fields=['*'])

            # Check for duplicates with active status
            for ns in new_service:
                for es in existing_service:
                    if ns['library_service'] == es['library_service'] and es['membership_status'] == 'Active':
                        frappe.throw(_("Duplicate active membership service found: {0}").format(ns['library_service']))
                        validated = 1
                        return
            # No duplicates found, proceed to add new service details
            # self.membership_details_update()
        except Exception as e:
            frappe.msgprint(_("An error occurred while checking for duplicate membership: {0}").format(str(e)))

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
