# Copyright (c) 2023, ramjanali and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class Membership(Document):
    def validate(self):
        if self.membership_status == "Active":
            member = frappe.get_doc('Member', self.member)
            frappe.db.set_value('Member', self.member, 'membership_expiry_date', self.to_date)
            frappe.db.set_value('Member', self.member, 'library_service', self.library_service)
            frappe.db.set_value('Member', self.member, 'membership_status', self.membership_status)
            frappe.msgprint("Membership is Active. Member updated successfully.")
        if self.membership_status == "Pending":
            member = frappe.get_doc('Member', self.member)
            frappe.db.set_value('Member', self.member, 'membership_expiry_date', self.to_date)
            frappe.db.set_value('Member', self.member, 'library_service', self.library_service)
            frappe.db.set_value('Member', self.member, 'membership_status', self.membership_status)
            frappe.msgprint("Membership is Pending. Member updated successfully.")
        if self.membership_status == "Expired":
            member = frappe.get_doc('Member', self.member)
            frappe.db.set_value('Member', self.member, 'membership_expiry_date', self.to_date)
            frappe.db.set_value('Member', self.member, 'library_service', self.library_service)
            frappe.db.set_value('Member', self.member, 'membership_status', self.membership_status)
            frappe.msgprint("Membership is Expired. Member updated successfully.")