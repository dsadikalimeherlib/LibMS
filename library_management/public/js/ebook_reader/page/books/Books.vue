<template>

    <div class="books-wrapper" @scroll="handleScroll">
        <div class="inner-container">
            <div class="page-header">
                <h1>Books</h1>
                <div class="right">
                    <div class="icons-wrapper">
                        <div :class="gridActiveClass" @click="setShowGrid(true)">
                            <svg width="31" height="24" viewBox="0 0 31 24" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <rect x="6" y="6" width="5" height="5" fill="#33363F" />
                                <rect x="13" y="6" width="5" height="5" fill="#33363F" />
                                <rect x="20" y="6" width="5" height="5" fill="#33363F" />
                                <rect x="6" y="13" width="5" height="5" fill="#33363F" />
                                <rect x="13" y="13" width="5" height="5" fill="#33363F" />
                                <rect x="20" y="13" width="5" height="5" fill="#33363F" />
                            </svg>
                        </div>
                        <div :class="listActiveClass" @click="setShowGrid(false)">
                            <svg width="25" height="18" viewBox="0 0 25 18" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <rect x="3" y="3" width="5" height="5" fill="#33363F" />
                                <rect x="10" y="4" width="12" height="3" fill="#33363F" />
                                <rect x="3" y="10" width="5" height="5" fill="#33363F" />
                                <rect x="10" y="11" width="12" height="3" fill="#33363F" />
                            </svg>
                        </div>
                    </div>
                    <BookSort />
                    <BookFilter :setFilters="setFilters" />
                </div>
            </div>

            <BooksGrid :onLinkClick="onLinkClick" v-if="showGrid" :books="bookstore.books" />
            <BooksList :onLinkClick="onLinkClick" v-else :books="bookstore.books" />
        </div>
    </div>
</template>
<script setup>
import BooksGrid from '../../components/books/BooksGrid.vue';
import BooksList from '../../components/books/BooksList.vue';
import BookSort from '../../components/books/book-sort/BookSort.vue';
import BookFilter from '../../components/books/book-filter/BookFilter.vue';

import { onMounted, reactive, ref } from 'vue';
import { useBooksStore } from '../../../books/store';
const bookstore = useBooksStore();
const url = new URL(window.location.href);
const params = new URLSearchParams(url.search);
const category = params.get('category');
const pageOffset = ref(0);
const length = 18
const hasMoreBooks = ref(true);
// Reactive object to store filter state
const filters = reactive({
    length,
    author: '',
    category: category !== null ? category : '',
    book_title: '',
    subject: '',
    page_offset: 0,
    publication_year: '',
    publication: ''
});
onMounted(() => {

    bookstore.get_book_list({ length, author: '', category: category !== null ? category : '' });
});

const setFilters = ({ length, author, category, book_title, subject, publication_year, publication, language }) => {
    // Update the filter values
    filters.length = length;
    filters.author = author;
    filters.category = category;
    filters.book_title = book_title;
    filters.subject = subject;
    filters.publication_year = publication_year
    filters.page_offset = 0;  // Reset page offset on new filter
    filters.publication = publication;
    filters.language = language

    bookstore.get_book_list({ length, author, category, book_title, subject, publication_year, publication, language });
};


const handleScroll = (event) => {
    const element = event.target;
    if (element.scrollHeight - element.scrollTop === element.clientHeight) {
        loadMoreData();
    }
};

const loadMoreData = () => {
    if (hasMoreBooks.value) {
        pageOffset.value += 1
        // Logic to load more books
        bookstore.get_book_list({ length, author: filters.author, category: category !== null ? category : filters.category, page_offset: pageOffset.value, hasMoreBooks, loadMore: true, book_title: filters.book_title, subject: filters.subject, publication_year: filters.publication_year, publication: filters.publication, language: filters.language });
    }
};

</script>
<script>
let showGridValue = localStorage.getItem('showGrid')
if (showGridValue == null) {
    showGridValue = true
} else {
    showGridValue = JSON.parse(showGridValue)
}
export default {
    props: {
        onLinkClick: {
            type: Function,
            required: true
        },
    },
    methods: {
        setShowGrid(value) {
            this.showGrid = value
            localStorage.setItem('showGrid', value)
        },

    },
    data() {
        return {
            showGrid: showGridValue,
            showSortPopup: false
        };
    },
    computed: {
        gridActiveClass() {
            return [
                'icon-wrapper',  // Static class
                {
                    active: this.showGrid,
                }
            ];
        },
        listActiveClass() {
            return [
                'icon-wrapper',  // Static class
                {
                    active: !this.showGrid,
                }
            ];
        },

    }
}
</script>
<style scoped>
@import "./style.css";
</style>
