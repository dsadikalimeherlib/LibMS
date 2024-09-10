import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useBooksStore = defineStore('books', {
    state: () => {
        return {
            books: ref([]),
            search_book: ref(""),
            book_category: ref(""),
            book_categories: ref([]),
            book_author: ref(""),
            book_subject: ref(""),
            book_tag: ref(""),
            book_edition: ref(""),
            year_of_publication: ref(""),

        }
    },
    getters: {

    },
    actions: {
        get_books({ length = null }) {
            frappe.call({
                method: "library_management.api.api.get_books",
                args: {},
                callback: (r) => {
                    if (r.message.length > 0) {
                        if (length !== null) {
                            this.books = r.message.slice(0, length);
                        } else {
                            this.books = r.message;
                        }


                    } else {
                        this.books = [];
                    }
                }
            });
        },


        get_book_categories({ length = null }) {
            frappe.call({
                method: "library_management.api.api.get_book_categories",
                args: {},
                callback: (r) => {
                    if (r.message.length > 0) {
                        if (length !== null) {
                            this.book_categories = r.message.slice(0, length);
                        } else {
                            this.book_categories = r.message;
                        }
                    } else {
                        this.book_categories = [];
                    }
                }
            });
        },

        search_books() {
            frappe.call({
                method: "library_management.api.api.search_books",
                args: {
                    book_title: this.search_book
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_books_by_category() {
            frappe.call({
                method: "library_management.api.api.get_books_by_category",
                args: {
                    book_category: this.book_category
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_books_by_author() {
            frappe.call({
                method: "library_management.api.api.get_books_by_author",
                args: {
                    author: this.book_author
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_books_by_subject() {
            frappe.call({
                method: "library_management.api.api.get_books_by_subject",
                args: {
                    subject: this.book_subject
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_books_by_tag() {
            frappe.call({
                method: "library_management.api.api.get_books_by_book_tag",
                args: {
                    book_tag: this.book_tag
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_books_by_edition() {
            frappe.call({
                method: "library_management.api.api.get_books_by_book_edition",
                args: {
                    edition: this.book_edition
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_books_by_year_of_publication() {
            frappe.call({
                method: "library_management.api.api.get_books_by_publication_year",
                args: {
                    year_of_publication: this.year_of_publication
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        search(search) {

            frappe.call({
                method: "library_management.api.api.search",
                args: {
                    keyword: search,
                },
                callback: (r) => {

                    if (r.message.length > 0) {
                        this.results = r.message;
                        let videoCount = 0;
                        let audioCount = 0;
                        let fil = r.message?.reduce((acc, item) => {
                            if (item.type == 'Video') {
                                videoCount = videoCount + 1
                            }
                            else if (item.type == 'Audio') {
                                audioCount = audioCount + 1

                            }
                            else {
                                // If the category is already present, increment its count, otherwise set it to 1
                                acc[item.category] = (acc[item.category] || 0) + 1;
                            }
                            return { ...acc, Video: videoCount, Audio: audioCount };
                        }, {});

                        this.categoryCounts = fil
                        // Total results count
                        this.totalResults = r.message.length;

                    } else {
                        this.results = [];
                    }
                }
            });
        },
        get_banners() {
            frappe.call({
                method: "library_management.api.api.get_banners",

                callback: (r) => {
                    if (r.message.length > 0) {
                        this.banners = r.message;
                    } else {
                        this.banners = [];
                    }
                }
            });
        },
        get_book_list({ book_title = '', length = 18, author = '', category = '', page_offset = 0, hasMoreBooks, loadMore = false, publication_year = '', sort, language, subject, publication }) {
            frappe.call({
                method: "library_management.api.api.get_book_list",
                args: {
                    book_title,
                    category,
                    author,
                    size: length,
                    subject,
                    publication_year,
                    publication,
                    language,
                    page_offset,
                    sort

                },
                callback: (r) => {
                    if (loadMore) {
                        if (r.message.length < length) {
                            hasMoreBooks.value = false; // No more books to load
                        }
                        if (r.message.length > 0) {
                            this.books = [...this.books, ...r.message]; // Append new data to existing books
                        }
                        else {
                            this.books = [];
                        }
                    } else {
                        if (r.message.length > 0) {
                            this.books = r.message;
                        } else {
                            this.books = [];
                        }
                    }
                }
            });
        },
        get_mulitmedia_category({ length = null }) {
            frappe.call({
                method: "library_management.api.api.get_multimedia_categories",
                args: {},
                callback: (r) => {
                    if (r.message.length > 0) {
                        if (length !== null) {
                            this.media_categories = r.message.slice(0, length);
                        } else {
                            this.media_categories = r.message;
                        }
                    } else {
                        this.media_categories = [];
                    }
                }
            });
        },
        get_media({ length = null, category = '', page_offset = 0, hasMoreBooks, loadMore = false, publication_year = '', sort }) {
            frappe.call({
                method: "library_management.api.api.get_multimedia_list",
                args: { size: length, category, publication_year, page_offset },

                callback: (r) => {
                    if (loadMore) {
                        if (r.message.length < length) {
                            hasMoreBooks.value = false; // No more books to load
                        }
                        if (r.message.length > 0) {
                            this.medias = [...this.medias, ...r.message]; // Append new data to existing medias
                        }
                        else {
                            this.medias = [];
                        }
                    } else {
                        if (r.message.length > 0) {
                            this.medias = r.message;
                        } else {
                            this.medias = [];
                        }
                    }
                }
            });
        },

        get_company_detail() {
            frappe.call({
                method: "library_management.api.api.get_company_contact_details",
                args: { size: length },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.company_detail = r.message;
                    } else {
                        this.company_detail = [];
                    }
                }
            });
        },
        get_book_detail({ id }) {

            frappe.call({
                method: "library_management.api.api.get_book_detail",
                args: {
                    book_id: id,


                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.book = r.message;
                    } else {
                        this.book = [];
                    }
                }
            });
        },

        // get_languages() {
        //     frappe.call({
        //         method: "library_management.api.api.get_languages",
        //         args: { size: length },
        //         callback: (r) => {
        //             if (r.message.length > 0) {
        //                 this.company_detail = r.message;
        //             } else {
        //                 this.company_detail = [];
        //             }
        //         }
        //     });
        // }

        get_terms_and_conditions() {
            frappe.call({
                method: "library_management.api.api.get_terms_and_conditions",
                callback: (r) => {


                    this.terms_condition = r.message;

                }
            });
        },

        get_holidays({ from_date = '', to_date = '' }) {
            frappe.call({
                method: "library_management.api.api.get_holidays",
                args: { from_date: from_date, to_date: to_date },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.holidays = r.message;
                    } else {
                        this.holidays = [];
                    }
                }

            });
        }




    }
})
