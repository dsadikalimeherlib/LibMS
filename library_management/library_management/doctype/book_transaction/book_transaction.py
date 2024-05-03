import frappe
from frappe.utils import today
from frappe import _
from frappe.model.document import Document

class BookTransaction(Document):
    # @frappe.whitelist()
    # def on_submit(self):
    #     self.create_book_ledger()
    def validate(self):
        try:
            self.create_book_ledger()
        except Exception as e:
            frappe.msgprint(f"An error occurred: {e}")
    
    def create_book_ledger(self):
        if self.is_new():
            frappe.msgprint("Creating Book Ledger Entry")
            try:
                book_transaction_details = frappe.get_all('Book Transaction Detail',
                                                       filters={'parent': self.name},
                                                       fields=['*'])
                for detail in book_transaction_details:
                    book_ledger_entry = frappe.new_doc('Book Ledger')
                    book_ledger_entry.member = self.member
                    # Add other necessary fields here
                    book_ledger_entry.save()

                frappe.msgprint("Book Ledger Entries created successfully.")
                
            except Exception as e:
                frappe.msgprint(_("An error occurred while creating new membership: {0}").format(str(e)))
