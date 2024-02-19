# Copyright (c) 2023, ramjanali and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BookTransaction(Document):
    def on_submit(self):
        self.on_submit_asset_update()

    def on_submit_asset_update(self):
        book_details = frappe.get_doc("Asset", self.asset)
        frappe.msgprint(f"Item created successfully: {book_details}")
        if book_details:
            if self.transaction_type == "Issue":
                book_details.status = self.transaction_type
                book_details.save()
                frappe.msgprint("Item updated successfully")
            else:
                book_details.status = "Available"
                book_details.save()
                frappe.msgprint("Item updated successfully")