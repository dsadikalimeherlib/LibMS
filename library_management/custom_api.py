import frappe
import pyqrcode
import io
import base64

@frappe.whitelist()
def generate_qrcode(qrcode_data):
    c = pyqrcode.create(qrcode_data)
    s = io.BytesIO()
    c.png(s, scale=3)
    encoded = "data:image/png;base64," + base64.b64encode(s.getvalue()).decode("ASCII")
    return encoded

@frappe.whitelist()
def count_books_issued(member):
    """
    Count the total books issued to the given member.
    """
    if not member:
        return {"count": 0}
    
    count = frappe.db.count("Book Ledger", filters={"member": member,"transaction_type":"Issue"})
    #book_allowed = frappe.get_value('Library Setting', 'number_of_book_allowed','number_of_book_allowed')
    
    #return {"count": count,"book_allowed": book_allowed}
    return {"count": count}


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