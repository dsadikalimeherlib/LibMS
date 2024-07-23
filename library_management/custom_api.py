import frappe
import pyqrcode
import io
import base64


@frappe.whitelist()
def generate_qrcode(qrcode_data):
    c = pyqrcode.create(qrcode_data)
    s = io.BytesIO()
    c.png(s, scale=3,quiet_zone=1)
    encoded = "data:image/png;base64," + base64.b64encode(s.getvalue()).decode("ASCII")
    return encoded

@frappe.whitelist()
def count_books_issued(member):
    """
    Count the total books issued to the given member.
    """
    if not member:
        return {"count": 0}
    
    count = frappe.db.count("Book Ledger", filters={"member": member,"transaction_type":"Issue","docstatus":1})
    #book_allowed = frappe.get_value('Library Setting', 'number_of_book_allowed','number_of_book_allowed')
    
    #return {"count": count,"book_allowed": book_allowed}
    return {"count": count}

@frappe.whitelist()
def allowed_book(member):
    allowed = frappe.get_value('Library Setting', 'number_of_book_allowed','number_of_book_allowed')
    return(allowed)

@frappe.whitelist()
def fetch_member_issue_book_detail(first_access_no):
    member_details = frappe.get_value("Book Ledger", filters={"access_no":first_access_no,"transaction_type":"Issue","docstatus":1},fieldname=["member","name","transaction_date","due_date"], as_dict=True)
    return(member_details)

@frappe.whitelist()
def check_for_duplicates(document_name):
        """Check for duplicate memberships and ensure they are not active."""
        try:
            # Fetch new service details
            new_service = frappe.get_all('Library Membership Details',
                                         filters={'parent': document_name},
                                         fields=['*'])
            # Fetch existing service details from the Member
            existing_service = frappe.get_all('Membership Details',
                                              filters={'parent': document_name},
                                              fields=['*'])

            # Check for duplicates with active status
            for ns in new_service:
                for es in existing_service:
                    if ns['library_service'] == es['library_service'] and es['membership_status'] == 'Active':
                        frappe.throw(("Duplicate active membership service found: {0}").format(ns['library_service']))
                        return(document_name)
            # No duplicates found, proceed to add new service details
            
        except Exception as e:
            frappe.msgprint(("An error occurred while checking for duplicate membership: {0}").format(str(e)))

# @frappe.whitelist()
# def check_for_duplicates(document_name):
#         """Check for duplicate active memberships and return status."""
#         try:
#             new_service = frappe.get_all('Library Membership Details',
#                                          filters={'parent': document_name},
#                                          fields=['*'])
#             existing_service = frappe.get_all('Membership Details',
#                                               filters={'parent': document_name},
#                                               fields=['*'])
#             for ns in new_service:
#                 for es in existing_service:
#                     if ns['library_service'] == es['library_service'] and es['membership_status'] == 'Active':
#                         return {'has_duplicate': True, 'duplicate_service': ns['library_service']}
#             return {'has_duplicate': False}
#         except Exception as e:
#             frappe.throw(("An error occurred while checking for duplicate membership: {0}").format(str(e)))
