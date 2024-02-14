# Copyright (c) 2024, ramjanali and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class BookCategory(Document):
	def validate(self):
		frappe.msgprint(f"ABC")