import json
import boto3
import frappe
from frappe.query_builder import DocType, Order
from frappe.query_builder.functions import Date


@frappe.whitelist()
def search(keyword):
    search_details = []
    search_details += get_books_by_keyword(keyword)
    search_details += get_book_tags(keyword)
    search_details += get_multimedia_by_keyword(keyword)
    search_details += get_multimedia_tags(keyword)
    return search_details

def get_books_by_keyword(keyword):
    bk = DocType("Book")
    book_query = (
        frappe.qb.from_(bk)
        .select(
            bk.name,
            bk.book_title,
            bk.book_category,
            bk.digital_file_type
        )
        .where(
            (bk.disabled == 0) 
            & (bk.is_digital_book == "Yes")
            || (bk.book_title.like("%" + keyword + "%"))
            || (bk.book_category.like("%" + keyword + "%"))
            || (bk.author.like("%" + keyword + "%"))
            || (bk.subject.like("%" + keyword + "%"))
            || (bk.book_tag.like("%" + keyword + "%"))
            || (bk.year_of_publication.like("%" + keyword + "%"))
            || (bk.publication.like("%" + keyword + "%"))
            || (bk.translator.like("%" + keyword + "%"))
            || (bk.description.like("%" + keyword + "%"))
        )
        # .where(
        #     || (bk.book_title.like("%" + keyword + "%"))
        #     || (bk.book_category.like("%" + keyword + "%"))
        # )
        .orderby(bk.book_title, bt.book_category)
    )
    books = book_query.run(as_dict=True)
    return books


def get_book_tags(tag):
    dl = DocType("Tag Link")
    bk = DocType("Book")
    tag_detials = (
        frappe.qb.from_(dl)
        .inner_join(bk)
        .on(dl.document_name == bk.name)   
        .select(
            dl.tag,
            bk.name,
            bk.book_title,
            bk.book_category,
            bk.digital_file_type
        )
        .where(
            (dl.document_type == "Book")
            && (dl.tag.like("%" + tag + "%"))
            && (bk.disabled == 0)
            && (bk.is_digital_book == "Yes")
        )
    ).run(as_dict=True)
    return tag_detials

def get_multimedia_by_keyword(keyword):
    mm = DocType("Multimedia")
    multimedia_query = (
        frappe.qb.from_(mm)
        .select(
            mm.name,
            mm.multimedia_title,
            mm.digital_file_type,
            mm.multimedia_category,
        )
        .where(
            (mm.disabled == 0)
            || (mm.multimedia_title.like("%" + keyword + "%"))
            || (mm.multimedia_category.like("%" + keyword + "%"))
        )
        .orderby(
            mm.multimedia_title,
            md.multimedia_category
        )
    )
    multimedia = multimedia_query.run(as_dict=True)
    return multimedia

def get_multimedia_tags(tag):
    dl = DocType("Tag Link")
    mm = DocType("Multimedia")
    tag_detials = (
        frappe.qb.from_(dl)
        .inner_join(mm)
        .on(dl.document_name == mm.name)
        .select(
            dl.tag,
            mm.name,
            mm.multimedia_title,
            mm.digital_file_type,
            mm.multimedia_category
        )
        .where(
            (dl.document_type == "Multimedia")
            && (dl.tag.like("%" + tag + "%"))
            && (mm.disabled == 0)
        )
    ).run(as_dict=True)
    return tag_detials

@frappe.whitelist()
def get_banners():
    b = DocType("Banner")
    bii = DocType("Banner Image Item")
    banner_data = (
        frappe.qb.from_(b)
        .inner_join(bii)
        .on(bii.parent == b.name)
        .select(
            b.banner_name,
            bii.image,
            bii.heading,
            bii.description,
            bii.url
        )
        .where(b.disabled == 0)
        .orderby(b.banner_name)
    ).run(as_dict=True)

    return banner_data


def get_multimedia(start_date=None, end_date=None, size=None, page_number=None, category=None, title=None, sort=None):
    mm = DocType("Multimedia")
    multimedia_query = (
        frappe.qb.from_(mm)
        .select(
            mm.image,
            mm.duration,
            mm.video_url,
            mm.multimedia_title,
            mm.digital_file_type,
            mm.multimedia_category,
            Date(mm.creation).as_("date"),
        )
        .where(
            (mm.disabled == 0)
        )
        .orderby(
            mm.multimedia_title,
            mm.creation,
            md.duration,
            md.multimedia_category
        )
    )
    if start_date:
        multimedia_query = multimedia_query.where(mm.creation >= start_date)
    if end_date:
        multimedia_query = multimedia_query.where(mm.creation <= end_date)
    # if size:
    #     multimedia_query = multimedia_query.limit(size)
    # if page_number:
    #     multimedia_query = multimedia_query.offset(page_number)
    if category:
        multimedia_query = multimedia_query.where(mm.multimedia_category == category)
    if title:
        multimedia_query = multimedia_query.where(mm.multimedia_title.like("%" + title + "%"))
    if sort:
        if sort.lower() == "asc":
            multimedia_query = multimedia_query.orderby(order=Order.asc)
        else:
            multimedia_query = multimedia_query.orderby(order=Order.desc)
    
    multimedia = multimedia_query.run(as_dict=True)
    return multimedia


@frappe.whitelist()
def get_books():
    return fetch_books()


@frappe.whitelist()
def search_books(book_title):
    books = fetch_books(book_title=book_title)
    return books


@frappe.whitelist()
def get_books_by_category(book_category):
    return fetch_books(category=book_category)


@frappe.whitelist()
def get_books_by_author(author):
    return fetch_books(author=author)


@frappe.whitelist()
def get_books_by_subject(subject):
    return fetch_books(subject=subject)


@frappe.whitelist()
def get_books_by_book_tag(book_tag):
    return fetch_books(book_tag=book_tag)


@frappe.whitelist()
def get_books_by_book_edition(edition):
    return fetch_books(edition=edition)


@frappe.whitelist()
def get_books_by_publication_year(year_of_publication):
    return fetch_books(year_of_publication=year_of_publication)


def fetch_books(
    book_title=None,
    category=None,
    author=None,
    subject=None,
    book_tag=None,
    edition=None,
    year_of_publication=None,
):
    bk = DocType("Book")
    book_query = (
        frappe.qb.from_(bk)
        .select(
            bk.name,
            bk.book_title,
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
            bk.aws_key,
            bk.digital_file_type,
        )
        .where((bk.disabled == 0) & (bk.is_digital_book == "Yes"))
        .orderby(bk.book_title)
        .limit(300)
    )

    if book_title:
        book_query = book_query.where(bk.book_title.like("%" + book_title + "%"))

    if category:
        book_query = book_query.where(bk.book_category == category)

    if author:
        book_query = book_query.where(bk.author.like("%" + author + "%"))

    if subject:
        book_query = book_query.where(bk.subject.like("%" + subject + "%"))

    if book_tag:
        book_query = book_query.where(bk.book_tag.like("%" + book_tag + "%"))

    if edition:
        book_query = book_query.where(bk.edition.like("%" + edition + "%"))

    if year_of_publication:
        book_query = book_query.where(
            bk.year_of_publication.like("%" + year_of_publication + "%")
        )

    books = book_query.run(as_dict=True)
    for book in books:
        book["image"] = get_book_image(book)

    return books


@frappe.whitelist()
def get_book_categories():
    bc = DocType("Book Category")
    category_query = (
        frappe.qb.from_(bc)
        .select(
            bc.name.as_("category"),
            bc.image
        )
        .where(bc.disabled == 0)
        .orderby(bc.name)
    )
    book_categories = category_query.run(as_dict=True)
    return book_categories


@frappe.whitelist()
def get_multimedia_categories():
    mc = DocType("Multimedia Category")
    category_query = (
        frappe.qb.from_(mc)
        .select(
            mc.name.as_("category"),
            mc.image
        )
        .where(mc.disabled == 0)
        .orderby(mc.name)
    )
    multimedia_categories = category_query.run(as_dict=True)
    return multimedia_categories


def get_book_image(book):
    """Select Only the default image of the book"""

    bi = DocType("Book Images")
    book_images = (
        frappe.qb.from_(bi)
        .select(bi.image)
        .where((bi.parent == book.name) & (bi.default == 1))
    ).run(as_dict=True)

    if len(book_images) > 0:
        return book_images[0].image

    return None


def get_tag_records(doctype, tag):
    dl = DocType("Tag Link")
    return (
        frappe.qb.from_(dl)
        .where(
            (dl.document_type == doctype)
            (dl.tag.like("%" + tag + "%"))
        )
        .select(
            dl.document_name,
            dl.tag
        )
    ).run(as_dict=True)
