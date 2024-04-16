import { createApp } from 'vue';
import { createPinia } from 'pinia';
import { useBooksStore } from './store';
import BooksComponent from './Books.vue';

import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

import { loadCSS } from './../utils';

// Loading Vuetify CSS
loadCSS('https://cdn.jsdelivr.net/npm/vuetify@3.5.14/dist/vuetify.min.css');

class Book {
    constructor(wrapper) {
        this.wrapper = $(wrapper);
        this.page = frappe.ui.make_app_page({
            parent: wrapper,
        });
        this.sidebar = this.wrapper.find(".layout-side-section");
        this.main_section = this.wrapper.find(".layout-main-section");
        this.wrapper.bind("show", () => {
            this.show();
        });
    }

    show() {
        this.page.set_title(__("Books"));
        this.setup_page();
    }

    setup_page() {
        const vuetify = createVuetify({
            icons: {
                defaultSet: 'mdi',
            },
            components,
            directives,
        })

        const pinia = createPinia();

        const app = createApp(BooksComponent);
        SetVueGlobals(app);

        app.use(vuetify);
        app.use(pinia);

        this.bookstore = useBooksStore();
        this.$books = app.mount(this.main_section.get(0));

    }
}

frappe.require("frappe-ui")
frappe.ui.Book = Book
export default Book