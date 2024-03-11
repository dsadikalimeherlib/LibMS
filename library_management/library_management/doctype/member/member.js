// Copyright (c) 2023, ramjanali and contributors
// For license information, please see license.txt


//frappe.ui.form.on("Member", "member_contact", function(frm, cdt, cdn) {
//			return {
//				filters: {
//					'link_doctype': 'Member',
//					'link_name': doc.name
//				}
//			}
//		})
//		frm.set_query('member_contact', function(doc) {
//			return {
//				filters: {
//					'link_doctype': 'Member',
//					'link_name': doc.name
//				}
//			}
//		})
//	}																	

frappe.ui.form.on('Member', {
	refresh(frm) {
		frm.set_query('member_address', function(doc) {
			return {
				filters: {
					'link_doctype': 'Member',
					'link_name': doc.member_name
				}
			}
		})
		frm.set_query('member_contact', function(doc) {
			return {
				filters: {
					'link_doctype': 'Member',
					'link_name': doc.member_name
				}
			}
		})
	}
});

