import json
import boto3
import frappe
from frappe.utils.password import get_decrypted_password
from botocore.exceptions import NoCredentialsError, ClientError

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
    bk = frappe.qb.DocType("Book")
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
    bc = frappe.qb.DocType("Book Category")
    category_query = (
        frappe.qb.from_(bc)
        .select(
            bc.name.as_("category"),
        )
        .orderby(bc.name)
    )
    return category_query.run(as_dict=True)


def get_book_image(book):
    """Select Only the default image of the book"""

    bi = frappe.qb.DocType("Book Images")
    book_images = (
        frappe.qb.from_(bi)
        .select(bi.image)
        .where((bi.parent == book.name) & (bi.default == 1))
    ).run(as_dict=True)

    if len(book_images) > 0:
        return book_images[0].image

    return None


@frappe.whitelist()
def get_external_book(aws_key):
    library_setting = frappe.get_cached_doc("Library Setting", "Library Setting")
    access_key = get_decrypted_password(
        "Library Setting", library_setting.name, "access_key"
    )
    secret_key = get_decrypted_password(
        "Library Setting", library_setting.name, "secret_key"
    )
    bucket_name = library_setting.aws_bucket_name
    region_name = library_setting.aws_region_name

    if not access_key or not secret_key:
        frappe.throw("AWS credentials not available")

    if not bucket_name:
        frappe.throw("AWS bucket name not available")

    if not aws_key:
        frappe.throw("AWS Book key not available")

    try:
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=access_key.strip(),
            aws_secret_access_key=secret_key.strip(),
            region_name=region_name,
        )

        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': aws_key},
            ExpiresIn=3
        )

        return presigned_url

    except NoCredentialsError as e:
        frappe.throw(msg=str(e), title="NoCredentialsError")
    except ClientError as e:
        frappe.throw(msg=str(e), title="ClientError")
    except Exception as e:
        frappe.throw(msg=str(e), title="Error")