import frappe

def validate(doc, event):
    pass

def after_insert(doc, event):
    frappe.msgprint(f"Book {doc.name} inserted successfully.")

    # Create a new Item document
    item = frappe.new_doc("Item")
    item.item_code = doc.title
    item.item_name = doc.title
    item.item_group = doc.book_category
    item.is_stock_item = 0
    item.include_item_in_manufacturing = 0
    item.is_fixed_asset = 1
    item.auto_create_assets = 1
    item.asset_category = doc.book_category

    # Insert the new Item document into the database
    item.insert()
    frappe.msgprint(f"Item {item.name} created for Book {doc.name}.")