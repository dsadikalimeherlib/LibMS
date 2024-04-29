# Copyright (c) 2024, ramjanali and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import today
from frappe import _
from frappe.model.document import Document


class KioskFeedback(Document):
	pass


@frappe.whitelist()
def submit_feedback(data):
    try:
        # Parse the data received from the API endpoint
        feedback_data = frappe.parse_json(data)

        # Create a new Feedback document
        feedback = frappe.get_doc({
            "doctype": "Kiosk Feedback",
            "first_name": feedback_data.get("name"),
            "enter_your_commentscomplains_in_the_space_provided_below": feedback_data.get("feedback"),
        })

        feedback.insert(ignore_permissions=True)

        return _("Feedback submitted successfully")
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Failed to submit feedback"))
        return _("Failed to submit feedback: {0}").format(str(e))
