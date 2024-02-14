# Copyright (c) 2023, ramjanali and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Member(Document):
    def before_save(self):
        self.member_name = f'{self.first_name} {self.middle_name or ""} {self.last_name or ""}'
        if self.get('__islocal'):
            new_customer = frappe.new_doc('Customer')
            new_customer.update({
                'customer_code': self.name,
                'customer_name': self.member_name
            })
            new_customer.insert(ignore_permissions=True)
            frappe.msgprint(f"Customer created successfully:")
