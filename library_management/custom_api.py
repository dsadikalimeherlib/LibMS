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

# @frappe.whitelist()
# def default_book(member):
#     """
#     Count the total books issued to the given member.
#     """
#     if not member:
#         return {"book_count": 0}
    
#     book_count = frappe.db.count("Library Setting",'number_of_book_allowed','number_of_book_allowed')
    
#     #return {"count": count,"book_allowed": book_allowed}
#     return {"book_count": book_count}