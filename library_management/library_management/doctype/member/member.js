// Copyright (c) 2023, ramjanali and contributors
// For license information, please see license.txt

//frappe.ui.form.on('Member', {
//    refresh:function (frm) {

//	}
        // Trigger the custom function when the button is clicked
           //openNewDocType(frm);
//});
// Your custom function to open the new DocType
function openNewDocType(frm) {
    frappe.route_options = {
        // Set any default values for the new DocType fields here
        Customer : frm.doc.member_name
    };
    frappe.new_doc("Customer");
}
frappe.ui.form.on('Member', {
    refresh: function(frm) {
        frm.add_custom_button('Customer', () => {
            frappe.new_doc('Customer', {
               custom_member : "abc"
            })
		//openNewDocType(frm);
        })
    }
});
