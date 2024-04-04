frappe.pages['books'].on_page_load = function (wrapper) {
	frappe.require("books.bundle.js", () => {
		let book = new frappe.ui.Book(wrapper)
		book.show();
	})
}