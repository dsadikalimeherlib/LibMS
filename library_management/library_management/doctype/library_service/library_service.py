# Copyright (c) 2024, ramjanali and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibraryService(Document):
    def validate(self):
        self.create_from_library_service()
        
    def create_from_library_service(self):
        if self.is_new():
            frappe.msgprint("create_from_library_service")
            # category = frappe.get_value('Library Setting', 'default_asset_category','default_asset_category')
            # asset_naming = frappe.get_value('Library Setting', 'asset_naming_series','asset_naming_series')
                
            item_doc = frappe.get_doc({
                'doctype': 'Item',
                'item_code': self.library_service,
                'item_name': self.library_service,
                'item_group': "Services",
                'is_stock_item': 0,
                'include_item_in_manufacturing': 0,
            })
            item_doc.insert()
            self.item_name = item_doc.name
            frappe.msgprint("Item created successfully")
