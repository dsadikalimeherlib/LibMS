# Copyright (c) 2023, ramjanali and contributors
# For license information, please see license.txt

import frappe
from frappe import _
# For license information, please see license.txt
# Uncomment this line if you need to use frappe module
from frappe.model.document import Document

class Membership(Document):
    def validate(self):
        if self.membership_status == "Active":
            member = frappe.get_doc('Member', self.member)
            frappe.db.set_value('Member', self.member, 'membership_expiry_date', self.to_date)
            frappe.db.set_value('Member', self.member, 'membership_type', self.membership_type)
            frappe.db.set_value('Member', self.member, 'membership_status', self.membership_status)
            frappe.msgprint("Membership is Active. Member updated successfully.")
        if self.membership_status == "Pending":
            member = frappe.get_doc('Member', self.member)
            frappe.db.set_value('Member', self.member, 'membership_expiry_date', self.to_date)
            frappe.db.set_value('Member', self.member, 'membership_type', self.membership_type)
            frappe.db.set_value('Member', self.member, 'membership_status', self.membership_status)
            frappe.msgprint("Membership is Pending. Member updated successfully.")
        if self.membership_status == "Expired":
            member = frappe.get_doc('Member', self.member)
            frappe.db.set_value('Member', self.member, 'membership_expiry_date', self.to_date)
            frappe.db.set_value('Member', self.member, 'membership_type', self.membership_type)
            frappe.db.set_value('Member', self.member, 'membership_status', self.membership_status)
            frappe.msgprint("Membership is Expired. Member updated successfully.")
#def set_indicator(self):
	#if self.to_date < getdate(nowdate()):
	    #self.membership_status == "Expired"
	    #frappe.msgprint("Membership status is Expired.")
