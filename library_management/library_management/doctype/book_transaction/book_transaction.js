// Copyright (c) 2023, ramjanali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book Transaction', {
    refresh(frm) {
        frm.set_query('member', function (doc) {
            return {
                filters: {
                    'membership_status': 'Active'
                }
            }
        });

        frm.set_query('asset', function (doc) {
            return {
                filters: {
                    'status': 'Available'
                }
            }
        });
        frm.add_custom_button('Generate OTP', function () {
            var otp = generateOTP();
            frm.set_value('otp', otp);
            frappe.msgprint(__("OTP generated successfully: ") + otp);
        });
        frm.add_custom_button(__('Verify'), function () {
            let d = new frappe.ui.Dialog({
                fields: [
                    {
                        label: 'OTP',
                        fieldname: 'verify_otp',
                        fieldtype: 'Data'
                    }
                ],
                primary_action_label: 'Save',
                primary_action(values) {
                    verify_member(frm, values.verify_otp); // Pass the entered OTP to the function
                    d.hide();
                }
            });

            d.show();
        });
    },
    scan_barcode(frm) {
        if (frm.doc.scan_barcode) {
            frm.call('get_asset_by_barcode', {
                self: frm.doc
            }).then((r) => {
                if (r.message) {
                    frm.add_child('book_transaction_detail', {
                        access_no: r.message.asset_name,
                        isbn_no: r.message.isbn,
                    });
                    frm.refresh_field('book_transaction_detail');

                } else {
                    frappe.msgprint(__("No asset found for the provided barcode: " + frm.doc.scan_barcode));
                }
            })
        }
    },
    onload: function (frm) {
        frm.fields_dict['book_transaction_detail'].grid.get_field('access_no').get_query = function (doc, cdt, cdn) {
            // Get the value of the "transaction_type" field
            var transactionType = frm.doc.transaction_type;
            // Set up the filter based on the value of "transaction_type"
            var filters = {};

            if (transactionType === "Issue") {
                filters = {
                    "status": "Available"
                };
            } else {
                filters = {
                    "status": "Issue"
                };
            }
            return {
                "filters": filters
            };
        },
        frm.fields_dict['return_book_details'].grid.get_field('access_no').get_query = function(doc, cdt, cdn) {
            // Get the value of the "transaction_type" field
            var transactionType = frm.doc.transaction_type;
            // Set up the filter based on the value of "transaction_type"
            var filters = {};

            if (transactionType === "Issue") {
                filters = {
                    "status": "Available"
                };
            } else {
                filters = {
                    "status": "Issue"
                };
            }
            return {
                "filters": filters
            };
        };
    },
    asset: function (frm) {
        var issue = frm.doc.issue_date;
        var due = frappe.datetime.add_days(issue, 30);
        frm.set_value('due_date', due);
    },
    from_date: function (frm) {
        var issue = frm.doc.issue_date;
        var due = frappe.datetime.add_days(issue, 30);
        frm.set_value('due_date', due);
    },
    transaction_type: function (frm) {
        frm.fields_dict['book_transaction_detail'].grid.get_field('access_no').get_query = function (doc, cdt, cdn) {
            // Get the value of the "transaction_type" field
            var transactionType = frm.doc.transaction_type;
            // Set up the filter based on the value of "transaction_type"
            var filters = {};

            if (transactionType === "Issue") {
                filters = {
                    "status": "Available"
                };
            } else {
                filters = {
                    "status": "Issue"
                };
            }
            return {
                "filters": filters
            };
        };
    },
    member: function (frm) {
        if (frm.doc.member) {
            // frappe.db.get_value("Library Setting", "number_of_book_allowed", "number_of_book_allowed").then(function(r){
            //     if (r.message && r.message.number_of_book_allowed !== undefined) {
            //         console.log(r.message.number_of_book_allowed);
            //         frappe.msgprint(__('Allowed') + ': ' + r.message.number_of_book_allowed);
            //     } else {
            //         console.log("Field 'number_of_book_allowed' not found or not set.");
            //         frappe.msgprint(__('Field "number_of_book_allowed" not found or not set.'));
            //     }
            // });
            //frappe.msgprint(__('Allowed') + ': ' + nob);
            // frappe.call({
            //     method: "library_management.library_management.doctype.book_reservation.book_reservation.default_book",
            //     args: {
            //         member: frm.doc.member
            //     },
            //     callback: function(response) {
            //         var issuedbook = response.message;

            //         if (response.message) {
            //             frappe.msgprint(__('Already Issued Book') + ': ' + issuedbook);
            //             //frm.set_value('issued_book', response.message.count);
            //         } else {
            //             frappe.msgprint(__('Error fetching books count'));
            //         }
            //     }
            // })
            // Fetch the count of books already issued
            frappe.call({
                method: "library_management.library_management.doctype.book_reservation.book_reservation.count_books_issued",
                args: {
                    member: frm.doc.member
                },

                // callback: function (response) {
                //     var issuedbook = response.message.count;

                callback: function(response) {
                    if (response.message) {
                        let issuedBooks = response.message.count;
                        frm.set_value('issued_book', issuedBooks);

                        // Fetch the allowed number of books after getting issued books count
                        frappe.call({
                            method: "book_allowed_issue.allowed_book",
                            args: {
                                member: frm.doc.member
                            },
                            callback: function(data) {
                                if (data.message) {
                                    let allowedBooks = data.message;
                                    // Check if the member has reached the allowed limit
                                    if (issuedBooks >= allowedBooks) {
                                        frappe.msgprint({
                                            title: __('Not Allowed'),
                                            message: __('You have already issued the maximum allowed number of books.'),
                                            indicator: 'red'
                                        });
                                        frm.disable_save(); // Disable save if the limit is reached
                                    } else {
                                        frappe.msgprint({
                                            title: __('Allowed'),
                                            message: __('You can issue more books.'),
                                            indicator: 'green'
                                        });
                                        frm.enable_save(); // Enable save if within the limit
                                    }
                                } else {
                                    frappe.msgprint(__('Error fetching allowed books count'));
                                }
                            }
                        });
                    } else {
                        frappe.msgprint(__('Error fetching issued books count'));
                    }
                }
            });
        } else {
            frm.set_value('issued_book', 0);
        }
    }
});

function verify_member(frm, enteredOTP) {
    var generatedOTP = frm.doc.otp;
    if (generatedOTP === enteredOTP) {
        frappe.msgprint(__('Verify Member'));
    } else {
        frappe.msgprint(__('Enter Valid OTP'));
    }
}

function generateOTP() {
    var otp = '';
    var possibleDigits = '0123456789';
    for (var i = 0; i < 6; i++) {
        otp += possibleDigits.charAt(Math.floor(Math.random() * possibleDigits.length));
    }
    return otp;
}

// Issue Book Code
frappe.ui.form.on("Book Transaction Detail", {
    access_no: function (frm, cdt, cdn) {
        var child_doc = locals[cdt][cdn];
        var due = frappe.datetime.add_days(child_doc.transaction_date, 30);
        frappe.model.set_value(cdt, cdn, 'due_date', due);
    },
    transaction_date: function (frm, cdt, cdn) {
        var child_doc = locals[cdt][cdn];
        var due = frappe.datetime.add_days(child_doc.transaction_date, 30);
        frappe.model.set_value(cdt, cdn, 'due_date', due);
    },
});

// Return Book code 
frappe.ui.form.on("Return Book Details", {
    access_no: function(frm, cdt, cdn) {
        var child_doc = locals[cdt][cdn];
        if (frm.doc.transaction_type === "Return") {
            var child_rows = frm.doc.return_book_details || [];
            if (child_rows.length > 0) {
                var i = 0;
                frm.doc.return_book_details.forEach(function(access){
                    var first_access_no = child_rows[i].access_no;
                    frappe.call({
                        method: "fetch_member_details.fetch_member_issue_book_detail",
                        args: {
                            first_access_no
                        },
                        callback: function(details) {
                                if (details.message){
                                    if (frm.doc.member){
                                        var member_id = details.message.member;
                                        if (frm.doc.member == member_id){
                                            frappe.model.set_value(cdt, cdn, 'transaction_no', details.message.name);
                                            frappe.model.set_value(cdt, cdn, 'transaction_date', details.message.transaction_date);
                                            frappe.model.set_value(cdt, cdn, 'due_date', details.message.due_date);
                                            frm.set_value('member', details.message.member);
                                            frappe.msgprint(__("Member ") + member_id);
                                        }else {
                                            frm.doc.return_book_details[i].transaction_no = '';
                                            frm.doc.return_book_details[i].transaction_date = '';
                                            frm.doc.return_book_details[i].due_date = '';
                                            //frm.doc.return_book_details[i].member = '';
                                            frappe.msgprint(__("Different Member - Clearing row"));
                                        }
                                    }
                                    else {
                                        frappe.model.set_value(cdt, cdn, 'transaction_no', details.message.name);
                                        frappe.model.set_value(cdt, cdn, 'transaction_date', details.message.transaction_date);
                                        frappe.model.set_value(cdt, cdn, 'due_date', details.message.due_date);
                                        frm.set_value('member', details.message.member);
                                    }
                                }
                        }
                    });
                    //frappe.msgprint(__("OTP generated successfully: ") + i);
                    i++;
                });
            } else {
                frappe.msgprint(__('No rows in book_transaction_detail'));
            }
        }
    }
});


