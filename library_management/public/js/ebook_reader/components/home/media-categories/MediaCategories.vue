<!-- template for the slider component -->
<template>
  <div v-if="mediaCategoryStore.media_categories?.length > 0" class="book-category-section">
    <div class="container">
      <div class="title-wrapper">
        <h2>Multimedia Categories</h2>
        <div class="right">
          <button @click="handleClick('media-categories')" class="link">See all<img
              src="/files/see-all-arrow.svg" /></button>
        </div>
      </div>
      <div class="category-list-wrapper">

        <template v-for="item in mediaCategoryStore.media_categories" :key="item.category">
          <div class="item">
            <div class="icon-wrapper" style="background-image: url(/files/round.png);"><img :src="item.image ? item.image
              : 'https://placehold.co/150?text=Item'" />

            </div>
            <div class="title">{{ item.category }}</div>
          </div>
        </template>


      </div>
    </div>
  </div>

</template>
<script setup>
import { onMounted } from 'vue';
import { useBooksStore } from '../../../../books/store';
const mediaCategoryStore = useBooksStore();

onMounted(() => {
  mediaCategoryStore.get_mulitmedia_category({ length: 5 });

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
