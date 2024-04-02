// Copyright (c) 2023, ramjanali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book Transaction', {
    refresh(frm) {
        frm.set_query('member', function(doc) {
            return {
                filters: {
                    'membership_status': 'Active'
                }
            }
        });

        frm.set_query('asset', function(doc) {
            return {
                filters: {
                    'status': 'Available'
                }
            }
        });

        frm.add_custom_button('Generate OTP', function() {
            var otp = generateOTP();
            frm.set_value('otp', otp);
            frappe.msgprint(__("OTP generated successfully: ") + otp);
        });
        frm.add_custom_button(__('Verify'), function() {
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

    asset:function(frm){
        var issue = frm.doc.issue_date;
        var due = frappe.datetime.add_days(issue, 30);
        frm.set_value('due_date', due);
    },

    from_date: function(frm){
        var issue = frm.doc.issue_date;
        var due = frappe.datetime.add_days(issue, 30);
        frm.set_value('due_date', due);
    },

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
