<template>

    <div class="books-wrapper">
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
                    <div class="icons-wrapper">
                        Filters
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                            <path d="M5 12L5 4" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <path d="M19 20L19 18" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <path d="M5 20L5 16" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <path d="M19 12L19 4" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <path d="M12 7L12 4" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <path d="M12 20L12 12" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <circle cx="5" cy="14" r="2" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <circle cx="12" cy="9" r="2" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <circle cx="19" cy="15" r="2" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                        </svg>
                    </div>
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

// import { onMounted } from 'vue';
// import { useBooksStore } from '../../../../books/store';
// const bookstore = useBooksStore();
const bookstore = {
    books: [
        {
            book_title: 'Book1',
            author: 'Author'
        },
        {
            book_title: 'Book2',
            author: 'Author'
        },
        {
            book_title: 'Book3',
            author: 'Author'
        },
        {
            book_title: 'Book4',
            author: 'Author'
        },
        {
            book_title: 'Book5',
            author: 'Author'
        }
    ]
}
</script>
<script>
let showGridValue = localStorage.getItem('showGrid')
console.log('showGridValue', showGridValue);
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
            showGrid: showGridValue
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
