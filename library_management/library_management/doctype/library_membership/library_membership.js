// Copyright (c) 2024, ramjanali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Membership', {
	library_service: function(frm) {
        var From = frm.doc.from_date;
        var To = frappe.datetime.add_days(From, frm.doc.days);
        frm.set_value('to_date', To);
    },
	from_date: function(frm) {
        if (frm.doc.from_date < get_today()) {
            frappe.msgprint(__("You can not select past date in From Date"));
            frappe.validated = false;
	        frm.doc.from_date = frappe.datetime.get_today();            
        }
        else{
            var From = frm.doc.from_date;
            var To = frappe.datetime.add_days(From, frm.doc.days);
            frm.set_value('to_date', To);
        }
    },
	validate:function(frm){
        var today = frappe.datetime.get_today();
        if(today >= frm.doc.from_date && today <= frm.doc.to_date ){
        //if(frm.doc.from_date <= today <= frm.doc.to_date ){
            frm.set_value('membership_status',"Active")
            frappe.msgprint(__('Membership Active.'));
            //frappe.validated = false;
        }
        else if(today <= frm.doc.from_date && today <= frm.doc.to_date )
        {
            frm.set_value('membership_status',"Pending")
            frappe.msgprint(__('Membership has Pending.'));
        }
        else
        {
            frm.set_value('membership_status',"Expired")
            frappe.msgprint(__('Membership has expired.'));
        }
    }
});
