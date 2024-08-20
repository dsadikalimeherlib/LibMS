<template>

    <div class="book-detail-wrapper">
        <div class="inner-container">
            <div class="book-image-title-wrapper">
                <div class="image-wrapper"><v-img :src="book.image ? book.image
                    : 'https://placehold.co/150?text=Item'">
                    </v-img></div>
                <div class="title-wrapper">
                    <h1>{{ book.book_title }}</h1>
                    <div class="subtitle">અનુવાદક & પ્રકાશક: મેહેર લાઇબ્રેરી & જાફરી સેમિનરી</div>
                </div>

            </div>
            <div class="book-detail-section">
                <div class="description-wrapper">
                    <div class="description">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                        labore
                        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
                        ut
                        aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
                        cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
                        culpa qui officia deserunt mollit anim id est laborum.

                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmo.
                    </div>
                    <div class="button-wrapper">
                        <div class="primary-button" @click="handleClick('book-reader')">Start reading</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>


// import { onMounted } from 'vue';
// import { useBooksStore } from '../../../../books/store';
// const bookstore = useBooksStore();
const bookstore = {
    book:
    {
        book_title: 'મુન્તખબ મીઝાનુલ હિકમા',
        author: 'Author'
    }

}
const book = bookstore.book
</script>
<script>
export default {
    props: {
        onLinkClick: {
            type: Function,
            required: true
        },
    },
    methods: {
        handleClick(pageName) {

            // Call the function passed via prop
            if (this.onLinkClick) {
                this.onLinkClick(pageName);
            }
        }
    }
}
</script>
<style scoped>
@import "./bookDetail.css";
</style>
