<!-- template for the slider component -->
<template>
  <div class="container">
    <div class="new-book-section media-section">

      <div class="title-wrapper">
        <h2>New Multimedia</h2>
        <div class="right">
          <button @click="handleClick('multimedia')" class="link">See all<img src="/files/see-all-arrow.svg" /></button>
        </div>
      </div>
      <div class="book-list-wrapper">
        <template v-for="item in mediastore.media" :key="item.title">
          <Multimedia :onLinkClick="onLinkClick" :media="item" />
        </template>


      </div>
    </div>
  </div>

</template>

<script setup>
import { onMounted } from 'vue';
import { useBooksStore } from '../../../../books/store';
import Multimedia from '../../multimedias/Multimedia.vue';
const mediastore = useBooksStore();
onMounted(() => {
  mediastore.get_media({ length: 3 });
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
