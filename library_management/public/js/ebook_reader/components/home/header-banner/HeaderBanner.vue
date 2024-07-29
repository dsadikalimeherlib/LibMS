<template>

  <div class="header-banner-wrapper">
    <img class="background" src="/files/banner-bg.png" />
    <div class="inner">
      <div class="header">
        <div class="logo">
          <img src="/files/logo.svg" />
        </div>
        <div class="right-buttons">
          <button @click="handleClick('books')">Explore all Books</button>
          <button @click="handleClick('multimedia')">Explore all multimedia</button>
        </div>
      </div>
      <div class="banner">
        <div class="title">Explore Books, Magazines, Journal and more...</div>
        <div class="search-wrapper">
          <img class="icon" src="/files/search-icon.svg" />
          <input placeholder="Looking for specific book? Enter Book Title here.." />
        </div>
      </div>
    </div>
  </div>
  <!-- <v-app> -->

  <!-- <button @click="handleClick('about')">About</button>
                This is homepage -->

  <!-- </v-app> -->

</template>

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
