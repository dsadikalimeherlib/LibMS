// Copyright (c) 2023, ramjanali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book Transaction', {
    refresh(frm) {
		frm.set_query('member', function(doc) {
			return {
				filters: {
					//'link_doctype': 'Member',
					//'link_name': doc.name,
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
	}
});