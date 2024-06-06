# Copyright (c) 2023, ramjanali and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import today
from frappe import _
from frappe.model.document import Document

class LibraryMembership(Document):
    def validate(self):
        try:
            self.update_member_details()
            #self.new_membership_create()
            #self.auto_expired()
        except Exception as e:
            frappe.msgprint(_("An error occurred: {0}").format(str(e)))

    @frappe.whitelist()
    def on_submit(self):
        # Add your logic for on_submit here
        self.new_membership_create()
        frappe.msgprint("Membership submitted successfully. Additional actions can be performed here.")

    def update_member_details(self):
        if self.membership_status in ["Active", "Pending", "Expired"]:
            member = frappe.get_doc('Member', self.member)
            #frappe.set_value('Member', self.member, 'membership_expiry_date', self.to_date)
            #frappe.set_value('Member', self.member, 'library_service', self.library_service)
            #frappe.set_value('Member', self.member, 'membership_status', self.membership_status)
            frappe.msgprint(f"Membership is {self.membership_status}. Member updated successfully.")

    def new_membership_create(self):
        try:
            
            # parent_doc = frappe.get_doc("Library Membership", self.member)
            library_membership_details = frappe.get_all('Library Membership Details',
                                                        filters={'parent': self.name},
                                                        fields=['*'])
            for details in library_membership_details:
                member_doc = frappe.get_doc("Member", self.member)
                child_table_entry = member_doc.append("membership_details", {})
                child_table_entry.library_membership = self.name
                child_table_entry.library_service = details.get('library_service')
                child_table_entry.from_date = details.get('from_date')
                child_table_entry.due_date = details.get('due_date')
                child_table_entry.membership_status = details.get('service_status')
                member_doc.save()
        except Exception as e:
            frappe.msgprint(_("An error occurred while creating new membership: {0}").format(str(e)))

    def auto_expired(self):
        try:
            expired_details = frappe.get_all("Library Membership", filters={"to_date": ("<", today())}, fields=["name", "to_date"])
            for expire in expired_details:
                member_doc = frappe.get_doc("Library Membership", expire.name)
                member_doc.membership_status = "Expired"
                member_doc.save()
                self.new_membership_create()
        except Exception as e:
            frappe.msgprint(_("An error occurred during auto-expiration: {0}").format(str(e)))
