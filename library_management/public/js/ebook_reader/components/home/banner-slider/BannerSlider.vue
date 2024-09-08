<!-- template for the slider component -->
<template>
  <div class="banner-section">
    <div class="container">
      <div class="slider-container">
        <div class="slider">
          <!-- Display each banner -->
          <div v-for="(banner, index) in bookCategoryStore.banners" :key="index" class="slide"
            :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
            <img :src="banner.image" :alt="banner.title" />
          </div>
        </div>


        <!-- Pagination Dots -->

      </div>
      <div class="pagination-dots">
        <span v-for="(banner, index) in bookCategoryStore.banners" :key="index" class="dot"
          :class="{ active: index === currentIndex }" @click="goToSlide(index)"></span>
      </div>
    </div>
  </div>



</template>
<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue';
import { useBooksStore } from '../../../../books/store';

const bookCategoryStore = useBooksStore(); // Use the store
const currentIndex = ref(0);
let autoSlideInterval = null;

// Fetch the banners when the component mounts
onMounted(() => {
  bookCategoryStore.get_banners(); // Call the API to fetch banners
  startAutoSlide(); // Start auto-sliding when banners are loaded
});

// Auto-slide function to automatically change slides
function startAutoSlide() {
  autoSlideInterval = setInterval(nextSlide, 3000); // Auto-slide every 3 seconds
}

// Clear and reset the auto-slide interval
function resetAutoSlide() {
  clearInterval(autoSlideInterval);
  startAutoSlide();
}

// Navigate to the next slide
function nextSlide() {
  currentIndex.value =
    (currentIndex.value + 1) % bookCategoryStore.banners.length;
}

// Navigate to the previous slide
function prevSlide() {
  currentIndex.value =
    (currentIndex.value - 1 + bookCategoryStore.banners.length) %
    bookCategoryStore.banners.length;
}

// Navigate to a specific slide
function goToSlide(index) {
  currentIndex.value = index;
  resetAutoSlide();
}

// Clear the interval when the component is destroyed
onBeforeUnmount(() => {
  clearInterval(autoSlideInterval);
});
</script>

<style scoped></style>
<style scoped>
@import "./style.css";
</style>
