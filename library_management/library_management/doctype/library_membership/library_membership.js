// Copyright (c) 2024, ramjanali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Membership', {
	refresh(frm) {
        // filter applied on 'New','Active','Current','Expired','Pending','Cancelled'
        frm.set_query('member', function(doc) {
            var status_list = ['New','Active','Expired','Pending','Cancelled'];
            return {
                filters: [
                    ['membership_status', 'in', status_list]
                ]
            };
        });
    },
});


frappe.ui.form.on('Library Membership', {
    before_save: function(frm) {
        frappe.msgprint(__('Before Save is Work'));
        frappe.call({
            method: "get_data.check_duplicate_membership",
            args: {
                document_name: frm.doc.name,
                member: frm.doc.member
            },
            callback: function(response) {
                console.log(document_name)
                if (response.message.has_duplicate) {
                    // Prevent saving by throwing an error
                    frappe.msgprint({
                        title: __('Duplicate Found'),
                        message: __('A duplicate active membership service found: {0}', [response.message.duplicate_service]),
                        indicator: 'red'
                    });
                    // Cancel the save
                    frm.prevent_default();
                }
            }
        });
    }
});


frappe.ui.form.on("Library Membership Details", {
    plan: function(frm, cdt, cdn) {
        var from_date = frappe.datetime.get_today();
        var child_doc = locals[cdt][cdn];
        var plan = child_doc.plan;
        if(plan == "Daily"){
            frappe.msgprint(__('Daily.'));
            var due = frappe.datetime.add_days(frm.doc.from_date, 1);
            frappe.model.set_value(cdt, cdn, 'due_date', due);
            frappe.model.set_value(cdt, cdn, 'days', 1);
        }
        else if(plan == "Weekly") {
            frappe.msgprint(__('Weekly.'));
            var due = frappe.datetime.add_days(frm.doc.from_date, 7);
            frappe.model.set_value(cdt, cdn, 'due_date', due);
            frappe.model.set_value(cdt, cdn, 'days', 7);
        }
        else if(plan == "Monthly") {
            frappe.msgprint(__('Monthly.'));
            var due = frappe.datetime.add_days(frm.doc.from_date, 30);
            frappe.model.set_value(cdt, cdn, 'due_date', due);
            frappe.model.set_value(cdt, cdn, 'days', 30);
        }
        else if(plan == "Quarterly"){
            frappe.msgprint(__('Quarterly.'));
            var due = frappe.datetime.add_days(frm.doc.from_date, 90);
            frappe.model.set_value(cdt, cdn, 'due_date', due);
            frappe.model.set_value(cdt, cdn, 'days', 90);
        }
        else if(plan == "Half yearly"){
            frappe.msgprint(__('Half yearly.'));
            var due = frappe.datetime.add_days(frm.doc.from_date, 180);
            frappe.model.set_value(cdt, cdn, 'due_date', due);
            frappe.model.set_value(cdt, cdn, 'days', 180);
        }
        else if(plan == "Yearly"){
            frappe.msgprint(__('Yearly.'));
            var due = frappe.datetime.add_days(frm.doc.from_date, 365);
            frappe.model.set_value(cdt, cdn, 'due_date', due);
            frappe.model.set_value(cdt, cdn, 'days', 365);
        }
    },
});

