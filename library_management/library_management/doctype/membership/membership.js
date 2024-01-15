// Copyright (c) 2023, ramjanali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Membership', {
	// refresh: function(frm) {

	// }
	membership_type: function(frm) {
        // Get the current date
        var From = frappe.datetime.get_today();

        // Calculate another date based on the current date (e.g., 30 days later)
        var To = frappe.datetime.add_days(From, frm.doc.days);

        // Set the calculated date in another field (e.g., 'another_date_field')
        frm.set_value('to_date', To);
    }
});
