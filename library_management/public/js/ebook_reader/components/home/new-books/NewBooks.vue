<!-- template for the slider component -->
<template>
  <div class="container">
    <div class="new-book-section">

      <div class="title-wrapper">
        <h2>New Books</h2>
        <div class="right">
          <button @click="handleClick('books')" class="link">See all<img src="/files/see-all-arrow.svg" /></button>
        </div>
      </div>
      <div class="book-list-wrapper">
        <template v-for="item in bookstore.books" :key="item.id">
          <Book :onLinkClick="onLinkClick" :book="item" />
        </template>


      </div>
    </div>
  </div>

</template>

<script setup>
import { onMounted } from 'vue';
import { useBooksStore } from '../../../../books/store';
import Book from '../../books/Book.vue';
const bookstore = useBooksStore();
onMounted(() => {

  bookstore.get_book_list({ length: 5 });
});
</script>

<script>
export default {
  props: {
    onLinkClick: {
      type: Function,
      required: true
    }
  },
  methods: {
    handleClick(pageName) {
      // Call the function passed via prop
      if (this.onLinkClick) {
        this.onLinkClick(pageName);
      }
    }
  }
};
</script>

<style scoped>
@import "./style.css";
</style>
