import frappe
import qrcode_gen
import pyqrcode
from PIL import Image
import base64
from io import BytesIO

def get_qrcode(input_str):
    qr = qrcode_gen.make(input_str)
    temp = BytesIO()
    qr.save(temp, "PNG")
    temp.seek(0)
    b64 = base64.b64encode(temp.read())
    return "data:image/png;base64,{0}".format(b64.decode("utf-8"))