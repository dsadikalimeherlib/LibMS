<template>
  <div id="app-container">
    <v-app>
      <v-main>

        <!-- <button @click="setCurrentComponent('home')">home</button> ???
        <button @click="setCurrentComponent('about')">about</button>??
        <button @click="setCurrentComponent('books')">books</button>??
        <button @click="setCurrentComponent('contact')">contact</button> -->

        <component v-if="page == 'home'" :onLinkClick="setCurrentComponent" :is="currentComponent"
          :setWhiteTheme="setWhiteTheme" :whiteTheme="whiteTheme"></component>
        <Layout v-else :customComponent="currentComponent" :onLinkClick="setCurrentComponent" />
      </v-main>
    </v-app>
  </div>
</template>

<script setup>
import Home from '../ebook_reader/page/home/Home.vue'
import About from '../ebook_reader/page/About.vue'
import Books from '../ebook_reader/page/books/Books.vue'
import Multimedias from '../ebook_reader/page/multimedias/Multimedias.vue'
import Contact from '../ebook_reader/page/Contact.vue'
import Layout from '../ebook_reader/layout/Layout.vue'
import BookCategories from '../ebook_reader/page/book-categories/BookCategories.vue'
import MediaCategories from '../ebook_reader/page/media-categories/MediaCategories.vue'
import BookDetail from '../ebook_reader/page/book-detail/BookDetail.vue'
import MediaDetail from '../ebook_reader/page/media-detail/MediaDetail.vue'
import BookReader from '../ebook_reader/page/book-reader/BookReader.vue'
import VideoPlayer from '../ebook_reader/page/video-player/VideoPlayer.vue'
import TermsCondition from '../ebook_reader/page/terms-condition/TermsCondition.vue'
import Holidays from '../ebook_reader/page/holidays/Holidays.vue'
import NewsAnnouncements from '../ebook_reader/page/news-announcements/NewsAnnouncements.vue'
import Fees from '../ebook_reader/page/fees/Fees.vue'
</script>
<script>
const url = new URL(window.location.href);
const params = new URLSearchParams(url.search);
const pageValue = params.get('page');
const theme = localStorage.getItem('whiteTheme')


export default {

  data() {
    return {
      page: pageValue == null ? 'home' : pageValue,
      currentComponent: Home,
      whiteTheme: theme !== null ? JSON.parse(theme) : true
    };
  },
  methods: {
    setCurrentComponent(pageName, refresh = false) {
      this.page = pageName
      let newUrl = `/app/books`
      if (pageName !== 'home') {
        newUrl = `/app/books?page=${pageName}`
      }
      console.log('refresh', refresh);

      if (refresh) {
        window.location.href = newUrl
      } else {
        window.history.pushState('', '', newUrl);
      }
      switch (pageName) {
        case 'home':
          this.currentComponent = Home
          break;
        case 'about':
          this.currentComponent = About
          break;
        case 'books':
          this.currentComponent = Books
          break;
        case 'multimedia':
          this.currentComponent = Multimedias
          break;

        case 'book-detail':
          this.currentComponent = BookDetail
          break;
        case 'book-categories':
          this.currentComponent = BookCategories
          break;
        case 'media-categories':
          this.currentComponent = MediaCategories
          break;
        case 'media-detail':
          this.currentComponent = MediaDetail
        case 'video-player':
          this.currentComponent = VideoPlayer
        case 'contact':
          this.currentComponent = Contact
          break;
        case 'book-reader':
          this.currentComponent = BookReader
          break;
        case 'terms-condition':
          this.currentComponent = TermsCondition
        case 'holidays':
          this.currentComponent = Holidays
        case 'news-announcement':
          this.currentComponent = NewsAnnouncements
        case 'fees':
          this.currentComponent = Fees
        default:
          if (this.page.includes('books&category=')) {
            this.currentComponent = Books
          }
          else if (this.page.includes('book-detail&id=')) {
            this.currentComponent = BookDetail
          }
          else if (this.page.includes('multimedia&category=')) {
            this.currentComponent = Multimedias
          }
          else if (this.page.includes('media-detail&id=')) {
            this.currentComponent = MediaDetail
          }
          else if (this.page.includes('video-player&id=')) {
            this.currentComponent = VideoPlayer
          }
          else {
            this.currentComponent = Home
          }
          break;
      }
    },
    setWhiteTheme(flag) {
      this.whiteTheme = flag
      localStorage.setItem('whiteTheme', flag)
    }
  },
  computed: {
    currentComponent() {
      switch (this.page) {
        case 'home':
          return Home
        case 'about':
          return About
        case 'books':
          return Books
        case 'multimedia':
          return Multimedias
        case 'media-detail':
          return MediaDetail
        case 'video-player':
          return VideoPlayer
        case 'book-detail':
          return BookDetail
        case 'book-reader':
          return BookReader
        case 'contact':
          return Contact
        case 'book-categories':
          return BookCategories
        case 'media-categories':
          return MediaCategories
        case 'terms-condition':
          return TermsCondition
        case 'holidays':
          return Holidays
        case 'news-announcement':
          return NewsAnnouncements
        case 'fees':
          return Fees
        default:
          if (this.page.includes('books&category=')) {
            return Books
          }
          else if (this.page.includes('book-detail&id=')) {
            return BookDetail
          }
          else if (this.page.includes('multimedia&category=')) {
            return Multimedias
          }
          else if (this.page.includes('media-detail&id=')) {
            return MediaDetail
          }
          else if (this.page.includes('video-player&id=')) {
            return VideoPlayer
          }
          else {
            return Home
          }

      }
    },
  },
};
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap');
@import "./reset.css";
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
<style>
#freeze {
  display: none;
}
</style>
