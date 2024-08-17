<template>

    <div class="book-detail-wrapper">
        <div class="inner-container">
            <div class="page-header">
                <h1>Book detail page</h1>

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
        book_title: 'Book1',
        author: 'Author'
    }

}
</script>
<script>
export default {

}
</script>
<style scoped>
@import "./bookDetail.css";
</style>
