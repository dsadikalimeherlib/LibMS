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