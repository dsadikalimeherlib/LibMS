<template>
  <v-dialog v-model="show" fullscreen hide-overlay>
    <v-app>
      <v-app-bar dense elevatedwill>
        <EpubTitlebar :title="book.title" @close-reader="closeReader" @toggle-toc="toggleToc" />
      </v-app-bar>
      <v-main>
        <v-row>
          <EpubToc :toc="toc" :isTocVisible="isTocVisible" @render-page="navigateToHref" />

          <v-col class="d-flex justify-start align-items-center">
            <v-btn icon @click="previousPage">
              <v-icon>mdi-chevron-left</v-icon>
            </v-btn>
          </v-col>
          <v-col class="align-items-center">
            <v-card class="mx-auto mt-8" max-width="1000" max-height="800" hover>
              <v-card-text>
                <div v-if="book.type === 'epub'" id="epub-render-area" style="height: calc(80vh - 80px);"></div>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col class="d-flex justify-end align-items-center">
            <v-btn icon @click="nextPage">
              <v-icon>mdi-chevron-right</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-main>
      <v-bottom-navigation class="bg-light">
        <v-spacer></v-spacer>
        <div class="d-flex justify-center align-items-center">
          <v-btn icon @click="previousPage">
            <v-icon>mdi-arrow-left</v-icon>
          </v-btn>
          <v-text-field v-model="manualPage" @keyup.enter="navigateToPage(manualPage)" @mouseleave="updatePlaceholder"
            class="mx-2 page-input-field" min="1" :max="totalPages" outlined dense small>
          </v-text-field>
          <v-btn icon @click="nextPage">
            <v-icon>mdi-arrow-right</v-icon>
          </v-btn>
        </div>
        <v-spacer></v-spacer>
      </v-bottom-navigation>
    </v-app>
  </v-dialog>
</template>

<script>
import { Book, Rendition } from 'epubjs';
import EpubTitlebar from './EpubTitlebar.vue';
import EpubToc from "./EpubToc.vue";

export default {
  name: 'EpubReader',
  components: {
    EpubTitlebar,
    EpubToc,
  },
  props: {
    book: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      show: false,
      url: '',
      bookInstance: null,
      rendition: null,
      page: 1,
      totalPages: 0,
      toc: [],
      isTocVisible: false,
      manualPage: '',
    };
  },
  watch: {
    page(newVal) {
      this.manualPage = newVal.toString();
      this.updatePlaceholder();
    },
  },
  methods: {
    async loadEPUB() {
      if (this.book && this.book.book_url) {
        try {
          this.url = frappe.urllib.get_full_url(this.book.book_url);

          this.bookInstance = new Book(this.url);
          await this.bookInstance.ready;

          await this.bookInstance.locations.generate(1024);
          this.totalPages = this.bookInstance.locations.total;

          this.rendition = new Rendition(this.bookInstance, {
            flow: 'paginated',
            manager: 'continuous',
            snap: true,
            spread: 'always',
            width: "calc(100% - 106px)",
            height: this.calculateReaderHeight()
          });
          this.rendition.attachTo("epub-render-area");
          this.rendition.display();


          this.rendition.on('relocated', (location) => {
            this.page = this.bookInstance.locations.locationFromCfi(location.start.cfi);
          });

          this.updatePlaceholder();
          this.loadToc();
          this.show = true;
        } catch (error) {
          console.error('Error loading book:', error);
        }
      }
    },
    nextPage() {
      if (this.book.type === 'epub' && this.rendition) {
        // this.page++;
        this.rendition.next();
        this.updatePlaceholder();
      }
    },
    previousPage() {
      if (this.book.type === 'epub' && this.rendition) {
        // this.page--;
        this.rendition.prev();
        this.updatePlaceholder();
      }
    },
    navigateToPage(pageNum) {
      pageNum = parseInt(pageNum, 10);
      if (pageNum && pageNum >= 1 && pageNum <= this.totalPages) {
        this.page = pageNum;
        console.log('Navigating to page:', this.page);
        this.rendition.display(this.page);
        this.updatePlaceholder();
      }
    },
    async navigateToHref(href, index) {
      if (this.rendition) {
        try {
          await this.rendition.display(href);
          this.page = index + 1;
          // this.updateCurrentPage();
        } catch (error) {
          console.error('Error navigating to page:', error);
        }
      }
    },
    updateCurrentPage() {
      if (!this.rendition || !this.bookInstance.locations) {
        console.error('Rendition or locations not defined.');
        return;
      }
      try {
        const currentLocation = this.rendition.currentLocation();
        if (currentLocation && currentLocation.start && currentLocation.start.cfi) {
          const currentCfi = currentLocation.start.cfi;
          const location = this.bookInstance.locations.locationFromCfi(currentCfi);
          if (location !== null) {
            const percentage = this.bookInstance.locations.percentageFromLocation(location);
            this.page = Math.ceil(percentage * this.totalPages);
            this.updatePlaceholder();
          } else {
            console.error('Failed to get location from CFI:', currentCfi);
          }
        } else {
          console.error('Current location data is incomplete:', currentLocation);
        }
      } catch (error) {
        console.error('Failed to update current page:', error);
      }
    },

    updatePlaceholder() {
      this.manualPage = `${this.page}/${this.totalPages}`;
    },
    closeReader() {
      if (document.fullscreenElement) {
        document.exitFullscreen();
      }
      this.show = false;
      this.$emit('close-reader');
    },
    toggleToc() {
      this.isTocVisible = !this.isTocVisible;
    },
    async loadToc() {
      try {
        if (this.bookInstance && this.bookInstance.navigation) {
          this.toc = await this.bookInstance.navigation.toc;
        } else {
          throw new Error("Navigation is not loaded or book instance is not available");
        }
      } catch (error) {
        console.error('Error loading the Table of Contents:', error);
        this.toc = [];
      }
    },
    calculateReaderHeight() {
      let h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
      h = h - 50 - 68 - 44;
      return h;
    },
  },
  created() {
    this.loadEPUB();
  },
};
</script>

<style scoped>
.v-card-text {
  overflow: auto;
}

#epub-render-area {
  max-height: 80vh;
}

#pdf-canvas {
  height: calc(80vh - 80px);
  width: 700px;
  overflow: auto;
}
</style>