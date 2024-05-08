<template>
    <v-toolbar color="primary">
        <v-app-bar-nav-icon @click="toggleSidebar"></v-app-bar-nav-icon>
        <v-spacer></v-spacer>
        <v-toolbar-title>Book List</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-text-field bg-color="white" rounded="pill" dense v-model="bookstore.search_book" prepend-icon="mdi-magnify"
            label="Search Books" @input="bookstore.search_books()" single-line hide-details>
        </v-text-field>
        <v-spacer></v-spacer>
    </v-toolbar>
    <v-navigation-drawer app class="nav-drawer" v-if="drawer">
        <v-card height="64" color="primary"></v-card>
        <v-card class="mx-auto">
            <v-list>
                <v-list-group v-model="openFilters" @click="toggleGroup('openFilters')" value="FILTERS:">
                    <template v-slot:activator="{ props }">
                        <v-list-item v-bind="props" prepend-icon="mdi-air-filter" title="FILTERS:"
                            align="left"></v-list-item>
                    </template>

                    <v-list-item color="primary" rounded="shaped">
                        <v-text-field v-model="bookstore.search_book" label="Title" required align="left"
                            @input="bookstore.search_books()" single-line hide-details>
                        </v-text-field>
                    </v-list-item>
                    <v-list-item color="primary" rounded="shaped">
                        <v-text-field v-model="bookstore.book_author" label="Author" required align="left"
                            @input="get_books_by_author(bookstore.book_author)" single-line hide-details>
                        </v-text-field>
                    </v-list-item>
                    <v-list-item color="primary" rounded="shaped">
                        <v-text-field v-model="bookstore.book_subject" label="Subject" required align="left"
                            @input="get_books_by_subject(bookstore.book_subject)" single-line hide-details>
                        </v-text-field>
                    </v-list-item>
                    <v-list-item color="primary" rounded="shaped">
                        <v-text-field v-model="bookstore.book_tag" label="Book Tag" required align="left"
                            @input="get_books_by_book_tag(bookstore.book_tag)" single-line hide-details>
                        </v-text-field>
                    </v-list-item>
                    <v-list-item color="primary" rounded="shaped">
                        <v-text-field v-model="bookstore.book_edition" label="Edition" required align="left"
                            @input="get_books_by_book_edition(bookstore.book_edition)" single-line hide-details>
                        </v-text-field>
                    </v-list-item>
                    <v-list-item color="primary" rounded="shaped">
                        <v-text-field v-model="bookstore.year_of_publication" label="Year of Publication"
                            @input="get_books_by_year_of_publication(bookstore.year_of_publication)" required
                            align="left" single-line hide-details>
                        </v-text-field>
                    </v-list-item>
                </v-list-group>
                <v-list-group v-model="exploreBook" @click="toggleGroup('exploreBook')" value="CATEGORIES:">
                    <template v-slot:activator="{ props }">
                        <v-list-item v-bind="props" prepend-icon="mdi-book-multiple" title="CATEGORIES:"
                            align="left"></v-list-item>
                    </template>

                    <v-list-item color="primary" rounded="shaped" v-for="item in bookstore.book_categories"
                        :key="item.category" @click="get_books_by_category(item.category)" v-model="item.category">
                        <v-list-item-title align="left" v-text="item.category"></v-list-item-title>
                    </v-list-item>
                </v-list-group>
            </v-list>
        </v-card>
    </v-navigation-drawer>
</template>

<script>
export default {
    name: 'Sidebar',
    props: ['drawer', 'bookstore'],
    emits: ['toggle-drawer', 'item-selected'],
    data() {
        return {
            exploreBook: false,
            openFilters: false,
        };
    },
    methods: {
        toggleSidebar() {
            this.$emit('toggle-drawer');
        },
        toggleGroup(group) {
            this[group] = !this[group];
        },

        get_books_by_category(category) {
            this.bookstore.book_category = category;
            this.bookstore.get_books_by_category();
        },

        get_books_by_author(author) {
            this.bookstore.book_author = author;
            this.bookstore.get_books_by_author();
        },

        get_books_by_subject(subject) {
            this.bookstore.book_subject = subject;
            this.bookstore.get_books_by_subject();
        },

        get_books_by_book_tag(tag) {
            this.bookstore.book_tag = tag;
            this.bookstore.get_books_by_tag();
        },

        get_books_by_book_edition(edition) {
            this.bookstore.book_edition = edition;
            this.bookstore.get_books_by_edition();
        },
        get_books_by_year_of_publication(year_of_publication) {
            this.bookstore.year_of_publication = year_of_publication;
            this.bookstore.get_books_by_year_of_publication();
        },


    },
};
</script>

<style scoped>
.app-bar {
    z-index: 2;
    margin-top: 60px;
    height: 60px;
}

.nav-drawer {
    z-index: 1;
    margin-top: 70px;
    width: 70%;
}
</style>