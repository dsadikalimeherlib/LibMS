// Copyright (c) 2024, ramjanali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Barcode Generator', {
    refresh: function(frm) {
        frm.set_query('item_code', function() {
            return {
                filters: {
                    is_fixed_asset: 1
                }
            };
        });
    },
    item_code: function(frm) {
        if (frm.doc.item_code) {
            // Fetch all assets related to the given item code

            frappe.db.get_list('Asset', {
                filters: { item_code: frm.doc.item_code },
                fields: ['name','asset_name','status']
            }).then(assets => {
                // Clear existing data in the child table
                frm.clear_table('barcode_generator_details');

                // Add a new row for each asset related to the item code to the child table
                assets.forEach(asset => {
                    let row = frappe.model.add_child(frm.doc, 'Barcode Generator Details', 'barcode_generator_details');
                    row.asset = asset.name;
                    row.asset_name = asset.asset_name;
                    row.status = asset.status;
                });
                // Refresh the child table
                frm.refresh_field('barcode_generator_details');
            });
        }
    }
});

