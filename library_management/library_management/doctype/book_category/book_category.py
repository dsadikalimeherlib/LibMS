# Copyright (c) 2024, ramjanali and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BookCategory(Document):
    def validate(self):
        frappe.msgprint("Validation successful")
        self.create_category()

    def create_category(self):
        if self.is_new():
            category_doc = frappe.get_doc({
                'doctype': 'Item Group',
                'item_group_name': self.book_category  # Changed 'doc' to 'self'
            })
            category_doc.insert()
            self.item_group_name = category_doc.name
            frappe.msgprint("Item group created successfully")
