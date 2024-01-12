# Copyright (c) 2023, ramjanali and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.contacts.address_and_contact import (
	delete_contact_and_address,
	load_address_and_contact,
)

class Member(Document):
	def before_save(self):
		self.member_name = f'{self.first_name} {self.middle_name or ""} {self.last_name or ""}'
