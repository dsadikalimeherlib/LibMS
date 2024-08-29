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
        frm.set_query("library_service_plan", "library_membership_details", function (doc, cdt, cdn) {
            const child = locals[cdt][cdn];
            return {
                query: "library_management.library_management.doctype.library_membership.library_membership.get_service_plans",
                filters: {
                    'library_service': child.library_service
                }
            }
        });
    },
    onload(frm) {
        frm.set_query("library_service_plan", "library_membership_details", function (doc, cdt, cdn) {
            const child = locals[cdt][cdn];
            return {
                query: "library_management.library_management.doctype.library_membership.library_membership.get_service_plans",
                filters: {
                    'library_service': child.library_service
                }
            }
        });  
    },
    expired(frm) {
        frappe.call({
            method: "auto_expire_memberships",
            args: {
                member: frm.doc.member
            },
            callback: function(data) {
                
            }
        });
    }
});

frappe.ui.form.on('Library Membership Details', {
    library_service_plan: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];

        if (child.library_service_plan && child.library_service) {
            console.log('Selected Library Service Plan:', child.library_service_plan);
            console.log('Selected Library Service:', child.library_service);

            // Call the server-side method to get days and amount
            frappe.call({
                method: "library_management.library_management.doctype.library_membership.library_membership.get_service_plan_details",
                args: {
                    'library_service_plan': child.library_service_plan,
                    'library_service': child.library_service
                },
                callback: function(r) {
                    if (r.message) {
                        console.log('Fetched Days:', r.message.days);
                        console.log('Fetched Amount:', r.message.amount);

                        // Set the fetched values to fields in the child table
                        frappe.model.set_value(cdt, cdn, 'days', r.message.days);
                        frappe.model.set_value(cdt, cdn, 'amount', r.message.amount);  // Replace 'amount' with your actual field name
                    } else {
                        console.warn('No details found for the selected Library Service Plan and Library Service.');
                    }
                }
            });
        }
    }
});
