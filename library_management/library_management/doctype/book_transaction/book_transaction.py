import frappe
from frappe.utils import today
from frappe import _
from frappe.model.document import Document

class BookTransaction(Document):
    def validate(self):
        # for rt in self.book_transaction_detail:
        #     rt_data = frappe.db.get_value('Book Ledger',rt.access_no,['member'])
        #     self.member = rt_data
        pass
        
    @frappe.whitelist()
    def on_submit(self):
        self.create_book_ledger()
        self.on_submit_asset_update()
        # barcode = frappe.get_doc('Book Transaction', self.barcode)
        # self.find_asset_by_barcode(barcode)

    def on_submit_asset_update(self):
        try:
            # Fetch book transaction details
            book_detail_table = frappe.get_all('Book Transaction Detail',
                                                filters={'parent': self.name},
                                                fields=['access_no'])

            for asset in book_detail_table:
                access_no = asset.get('access_no')
                # Fetch asset document
                asset_doc = frappe.get_doc("Asset", access_no)
                if asset_doc:
                    # Update asset status with the transaction type
                    if self.transaction_type == "Return":
                        asset_doc.status = "Available"
                        asset_doc.save()
                        frappe.msgprint(f"Asset {access_no} updated successfully")
                    else:
                        asset_doc.status = self.transaction_type
                        asset_doc.save()
                        frappe.msgprint(f"Asset {access_no} updated successfully")


        except Exception as e:
            frappe.log_error(f"An error occurred while updating assets: {str(e)}")
            frappe.msgprint(f"Error: {str(e)}")
    # def on_submit_asset_update(self):
    #     book_detail_table = frappe.get_all('Book Transaction Detail',
    #                                                     filters={'parent': self.name},
    #                                                     fields=['*'])
    #     #frappe.msgprint(f"Item created successfully: {book_detail_table}")
    #     for asset in book_detail_table:
    #          asset_update = frappe.get_doc("Asset", asset.get('access_no'))
    #          frappe.msgprint(f"Item created successfully: {asset_update}")
    #          asset_update.status == self.transaction_type
    #          asset_update.save()
    #          frappe.msgprint("Item updated successfully")

        # if book_details:
        #     asset_update = frappe.get_doc("Asset", detail.get('access_no'))
        #     if self.transaction_type == "Issue":
        #         book_details.status = self.transaction_type
        #         book_details.save()
        #         frappe.msgprint("Item updated successfully")
        #     else:
        #         book_details.status = "Available"
        #         book_details.save()
        #         frappe.msgprint("Item updated successfully")

    def create_book_ledger(self):
        try:
                # Fetch only necessary fields from the child table
                book_transaction_details = frappe.get_all('Book Transaction Detail',
                                                        filters={'parent': self.name},
                                                        fields=['*'])
                for detail in book_transaction_details:
                    book_ledger_entry = frappe.new_doc('Book Ledger')
                    book_ledger_entry.member = self.member
                    book_ledger_entry.transaction_no = self.name
                    book_ledger_entry.transaction_type = self.transaction_type
                    book_ledger_entry.voucher_type = self.doctype
                    book_ledger_entry.membership_status = self.membership_status
                    book_ledger_entry.access_no = detail.get('access_no')
                    book_ledger_entry.transaction_date = detail.get('transaction_date')
                    book_ledger_entry.due_date = detail.get('due_date')
                    book_ledger_entry.insert()
                    book_ledger_entry.submit()
                    frappe.msgprint("Book Ledger Entries created successfully.")

        except Exception as e:
                # Log the error for better debugging
                frappe.log_error("An error occurred while creating book ledger entries: {0}".format(str(e)))    
    
    @frappe.whitelist()
    def on_cancle(self):
         self.cancel_book_ledger_entries()

    def on_cancel(self):
        try:
            # Fetch Book Ledger entries associated with the canceled Book Transaction
            book_ledger_entries = frappe.get_all('Book Ledger',
                                                  filters={'transaction_no': self.name},
                                                  fields=['name'])

            # Cancel each fetched Book Ledger entry
            for entry in book_ledger_entries:
                frappe.get_doc('Book Ledger', entry['name']).cancel()

            frappe.msgprint("Book Ledger Entries canceled successfully.")
            
        except Exception as e:
            frappe.msgprint(_("An error occurred while canceling Book Ledger entries: {0}").format(str(e)))
    
    @frappe.whitelist()
    def get_asset_by_barcode(barcode):
        asset = frappe.get_doc('Asset', {'barcode': barcode})
        if asset:
            return {
                'asset_name': asset.asset_name
            }
        else:
            return None