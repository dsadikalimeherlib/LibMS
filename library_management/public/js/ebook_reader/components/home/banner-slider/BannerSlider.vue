<!-- template for the slider component -->
<template>
  <div class="banner-section">
    <div class="container">
      <div class="slider-container">
        <div class="slider">
          <!-- Display each banner -->
          <div v-for="(banner, index) in banners" :key="index" class="slide"
            :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
            <img :src="banner.image" :alt="banner.title" />
          </div>
        </div>


        <!-- Pagination Dots -->

      </div>
      <div class="pagination-dots">
        <span v-for="(banner, index) in banners" :key="index" class="dot" :class="{ active: index === currentIndex }"
          @click="goToSlide(index)"></span>
      </div>
    </div>
  </div>



</template>
<script>
export default {
  data() {
    return {
      banners: [
        { image: "/files/banner.png", title: "Banner 1" },
        { image: "https://s3-us-west-2.amazonaws.com/s.cdpn.io/5689/grooves.jpg", title: "Banner 2" },
        { image: "https://s3-us-west-2.amazonaws.com/s.cdpn.io/5689/sunset.jpg", title: "Banner 3" }
      ],
      currentIndex: 0,
      autoSlideInterval: null // To hold the interval reference for auto-sliding
    };
  },
  methods: {
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.banners.length; // Loop back to the start
    },
    prevSlide() {
      this.currentIndex =
        (this.currentIndex - 1 + this.banners.length) % this.banners.length; // Loop back to the end
    },
    goToSlide(index) {
      this.currentIndex = index;
      this.resetAutoSlide(); // Reset the auto-slide when user manually selects a slide
    },
    startAutoSlide() {
      this.autoSlideInterval = setInterval(this.nextSlide, 3000); // Auto-slide every 3 seconds
    },
    resetAutoSlide() {
      clearInterval(this.autoSlideInterval);
      this.startAutoSlide();
    }
  },
  mounted() {
    this.startAutoSlide(); // Start auto-sliding when the component is mounted
  },
  beforeDestroy() {
    clearInterval(this.autoSlideInterval); // Clean up the interval when the component is destroyed
  }
};
</script>

<style scoped></style>
<style scoped>
@import "./style.css";
</style>
