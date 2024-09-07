<template>
    <div class="book-categories-page">
        <h1>Book Categories</h1>
        <div class="category-list-wrapper">
            <template v-for="item in bookCategoryStore.book_categories" :key="item.category">
                <div class="item" @click="handleClick(`books&category=${item.category}`)">
                    <div class="icon-wrapper" style="background-image: url(/files/round.png);"><img
                            src="/files/image.png">
                    </div>
                    <div class="title">{{ item.category }}</div>
                </div>
            </template>
        </div>

    </div>
</template>


<script setup>
import { onMounted } from 'vue';
import { useBooksStore } from '../../../books/store';
const bookCategoryStore = useBooksStore();

onMounted(() => {
    bookCategoryStore.get_book_categories({ length: null });
});
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
    },
}
</script>

<style scoped>
@import "./bookCategories.css";
</style>
