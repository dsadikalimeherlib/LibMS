frappe.ui.form.on('Book', {
    onload_post_render: function(frm) {
        toggleSearchVisibility(frm);

        frm.fields_dict['search'].$input.on('click', function() {
            if (frm.doc.isbn) {
                frappe.call({
                    method: 'library_management.api.isbn_api.fetch_book_details',
                    args: { isbn: frm.doc.isbn },
                    callback: function(response) {
                        console.log(response);
                        if (!response.message.error) {
                            var bookInfo = response.message;

                            // Populate fields with book details
                            frm.set_value('title', bookInfo.title);
                            frm.set_value('author', bookInfo.author);
                            frm.set_value('publication', bookInfo.publisher);
                            frm.set_value('year_of_publication', bookInfo.published_year);

                            // Attach thumbnail image from API response
                            if (bookInfo.image_url) {
                                uploadThumbnail(frm, bookInfo.image_url);
                            }



                            // Check and create Author
                            createAuthor(frm, bookInfo.author);

                            // Check and create Publication
                            createPublication(frm, bookInfo.publisher);
                        } else {
                            frappe.msgprint("Book not found.");
                        }
                    }
                });
            } else {
                frappe.msgprint("Please enter an ISBN before searching.");
            }
            
        });

        frm.fields_dict['isbn'].$input.on('change', function() {
            toggleSearchVisibility(frm);
        });
    },
    before_save: function(frm) {
        if (frm.doc.isbn && !frm.doc.image) {
            fetchBookDetails(frm);
        }
    
    // Retrieve book category from the document and call createBookCategory function
    var bookCategory = frm.doc.book_category;
    if (bookCategory) {
        createBookCategory(frm, bookCategory);
    }
    }
});

function toggleSearchVisibility(frm) {
    var showSearch = frm.doc.__unsaved || frm.doc.__islocal;
    frm.toggle_display('search', showSearch);
}

function uploadThumbnail(frm, thumbnailUrl) {
    let imageFile = new FormData();
    imageFile.append('file_url', thumbnailUrl);

    fetch('/api/method/upload_file', {
        headers: {
            'X-Frappe-CSRF-Token': frappe.csrf_token
        },
        method: "POST",
        body: imageFile
    })
    .then(res => res.json())
    .then(data => {
        if (data.message.file_url) {
            frm.set_value('image', data.message.file_url);
            frappe.msgprint(__('Book Cover attached successfully'));
        } else {
            frappe.msgprint("Error attaching thumbnail.");
        }
    })
    .catch(error => {
        console.error("Error attaching thumbnail:", error);
    });
}

function createBookCategory(frm, category) {
    // Check if Book Category exists
    frappe.db.exists('Book Category', category)
        .then(bookExists => {
            if (!bookExists) {
                // Create Book Category
                frappe.db.insert({
                    doctype: 'Book Category',
                    book_category: category
                }).then(bookDoc => {
                    frappe.msgprint(__('New Book Category created'));
                });
            } else {
                frappe.msgprint(__('Book Category exists'));
            }

            // Check if Asset Category exists
    frappe.db.exists('Asset Category', category)
                .then(assetExists => {
                    if (!assetExists) {
                        // Create Asset Category
                        frappe.db.insert({
                            doctype: 'Asset Category',
                            asset_category_name: category
                        }).then(assetDoc => {
                            frappe.msgprint(__('New Asset Category created'));
                        });
                    } else {
                        frappe.msgprint(__('Asset Category exists'));
                    }
                })
                .catch(err => {
                    console.error("Error checking Asset Category existence:", err);
                });
        })
        .catch(err => {
            console.error("Error checking Book Category existence:", err);
        });
}


function createAuthor(frm, authorName) {
    frappe.db.exists('Author', authorName)
        .then(exists => {
            if (!exists) {
                frappe.db.insert({
                    doctype: 'Author',
                    author_name: authorName
                }).then(doc => {
                    frappe.msgprint(__('New author created'));
                });
            } else {
                frappe.msgprint(__('Author already exists'));
            }
        })
        .catch(err => {
            console.error("Error checking Author existence:", err);
        });
}

function createPublication(frm, publicationName) {
    frappe.db.exists('Publication', publicationName)
        .then(exists => {
            if (!exists) {
                frappe.db.insert({
                    doctype: 'Publication',
                    publication: publicationName
                }).then(doc => {
                    frappe.msgprint(__('New publication created'));
                });
            } else {
                frm.set_value('publication', publicationName);
                frappe.msgprint(__('Publication already exists'));
            }
        })
        .catch(err => {
            console.error("Error checking Publication existence:", err);
        });
}
