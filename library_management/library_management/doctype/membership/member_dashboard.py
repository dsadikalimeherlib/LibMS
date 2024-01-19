from frappe import _


def get_data():
	return {
		"heatmap": True,
		"heatmap_message": _(
			"This is based on transactions against this Supplier. See timeline below for details"
		),
		"fieldname": "member",
		"transactions": [
			{"label": _("Membership"), "items": ["Member", "Membership"]}
			# {"label": _("Orders"), "items": ["Purchase Order", "Purchase Receipt", "Purchase Invoice"]},
			# {"label": _("Payments"), "items": ["Payment Entry", "Bank Account"]},
			# {"label": _("Pricing"), "items": ["Pricing Rule"]},
		],
	}