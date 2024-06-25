// Copyright (c) 2024, ramjanali and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Book Reservation", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Book Reservation', {
    member: function(frm) {
        if (frm.doc.member) {
            frappe.call({
                method: "library_management.library_management.doctype.book_reservation.book_reservation.count_books_issued",
                args: {
                    member: frm.doc.member
                },
                callback: function(response) {
                    if (response.message) {
                        frm.set_value('issued_book', response.message.count);
                    } else {
                        frappe.msgprint(__('Error fetching books count'));
                    }
                }
            });
        } else {
            frm.set_value('issued_book', 0);
        }
    },
    book: function(frm) {
        if (frm.doc.book) {
            // Fetch all assets related to the given item code
            frappe.db.get_list('Asset', {
                filters: { item_code: frm.doc.book , status:"Available"},
                fields: ['name','asset_name','status']
            }).then(book => {
                // Clear existing data in the child table
                frm.clear_table('book_reservation_details');

                // Add a new row for each asset related to the item code to the child table
                book.forEach(asset => {
                    let row = frappe.model.add_child(frm.doc, 'Book Reservation Details', 'book_reservation_details');
                    row.access_no = asset.name;
                    row.book_name = asset.asset_name;
                    row.status = asset.status;
                });
                // Refresh the child table
                frm.refresh_field('book_reservation_details');

                // Optional: Show a message
                frappe.msgprint(__('Fetched {0} assets', [book.length]));
            });
        }
    },
    on_submit: function(frm) {
        if (!frm.doc.book_reservation_details || frm.doc.book_reservation_details.length === 0) {
            // frappe.msgprint(__('Please add items before submitting the Purchase Order.'));
              // Prevent submission
            return;
        } else {
            frappe.msgprint(__('No Reservation! This Book with Access Number {{}} Is available '));
            frappe.validated = false;
        }
    }
});