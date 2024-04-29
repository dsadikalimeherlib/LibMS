# Copyright (c) 2024, ramjanali and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Book(WebsiteGenerator):
    def validate(self):
        # Uncomment the line below to create an item when the book is saved
        # self.create_item_from_book()
        frappe.msgprint("Validation successful")
        self.create_item_from_book()
        # self.sample()

    # def sample(self):
    #     if self.is_new():
    #         frappe.msgprint("Book is new")
    #         self.create_item_from_book()
        
    def create_item_from_book(self):
        if self.is_new():
            frappe.msgprint("Creating Item from Book")
            category = frappe.get_value('Library Setting', 'default_asset_category','default_asset_category')
            #category = frappe.get_value('Library Setting', filters={'name': 'default_asset_category'}, fieldname='default_asset_category')
            item_doc = frappe.get_doc({
                'doctype': 'Item',
                'item_code': self.title,
                'item_name': self.title,
                'item_group': self.book_category,
                'is_stock_item': 0,
                'include_item_in_manufacturing': 0,
                'is_fixed_asset': 1,
                'auto_create_assets': 1,
                'asset_category': category
            })
            item_doc.insert()
            self.item_name = item_doc.name
            frappe.msgprint("Item created successfully")
