import frappe
from frappe.model.document import Document
from frappe.contacts.address_and_contact import (
	delete_contact_and_address,
	load_address_and_contact,
)

class Member(Document):
    def validate(self):
        self.member_name = f'{self.first_name} {self.middle_name or ""} {self.last_name or ""}'
        self.create_customer_from_member()

    def create_customer_from_member(self):
        if self.is_new():
            customer_doc = frappe.get_doc({
                'doctype': 'Customer',
                'customer_code': self.name,
                'customer_name': self.member_name
            })
            frappe.msgprint("Customer created successfully")
            customer_doc.insert()
            self.customer_code = customer_doc.name
