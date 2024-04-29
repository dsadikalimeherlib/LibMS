import frappe


@frappe.whitelist()
def get_books():
    return fetch_books()


@frappe.whitelist()
def search_books(book_title):
    books = fetch_books(title=book_title)
    # frappe.throw(str(len(books)) + "  <br><br>" + str(books))
    return books


def fetch_books(title=None):
    bk = frappe.qb.DocType("Book")
    bi = frappe.qb.DocType("Book Images")
    book_query = (
        frappe.qb.from_(bk)
        .inner_join(bi)
        .on(bk.name == bi.parent)
        .select(
            bk.title,
            bk.isbn,
            bk.book_code,
            bk.book_tag,
            bk.author,
            bk.book_category,
            bk.year_of_publication,
            bk.publication,
            bk.edition,
            bk.subject,
            bk.no_of_pages,
            bk.book_url,
            bk.type,
            bi.image,
        )
        .where(bk.disabled == 0)
    )

    if title:
        book_query = book_query.where(bk.title.like("%" + title + "%"))

    return book_query.run(as_dict=True)
