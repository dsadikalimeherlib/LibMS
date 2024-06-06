// Copyright (c) 2024, ramjanali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Membership', {
	// validate:function(frm){
    //     var today = frappe.datetime.get_today();
    //     if(today >= frm.doc.from_date && today <= frm.doc.to_date ){
    //     //if(frm.doc.from_date <= today <= frm.doc.to_date ){
    //         frm.set_value('membership_status',"Active")
    //         frappe.msgprint(__('Membership Active.'));
    //         //frappe.validated = false;
    //     }
    //     else if(today <= frm.doc.from_date && today <= frm.doc.to_date )
    //     {
    //         frm.set_value('membership_status',"Pending")
    //         frappe.msgprint(__('Membership has Pending.'));
    //     }
    //     else
    //     {
    //         frm.set_value('membership_status',"Expired")
    //         frappe.msgprint(__('Membership has expired.'));
    //     }
    // }
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

