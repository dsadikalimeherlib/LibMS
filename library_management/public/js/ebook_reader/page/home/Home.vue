<template>
  <div id="app-container" class="homepage">
    <HeaderBanner :onLinkClick="onLinkClick" />
    <!-- <v-app> -->

    <!-- <button @click="handleClick('about')">About</button>
                This is homepage -->

    <!-- </v-app> -->
  </div>
</template>
<script setup>
import HeaderBanner from '../../components/home/header-banner/HeaderBanner.vue'
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

<style>
.sticky-top {
  display: none;
}
</style>

<style scoped>
.drawer-open {
  transition: margin-left 0.3s;
  margin-left: 10px;
}

.v-card img {
  object-fit: cover;
}
</style>

<style scoped>
@import "./home.css";
</style>
