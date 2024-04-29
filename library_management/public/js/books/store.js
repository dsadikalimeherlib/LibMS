import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useBooksStore = defineStore('books', {
    state: () => {
        return {
            books: ref([]),
            search_book: ref("")
        }
    },
    getters: {

    },
    actions: {
        get_books() {
            frappe.call({
                method: "library_management.api.api.get_books",
                args: {},
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
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
                    }
                }
            });
        }
    }
})
