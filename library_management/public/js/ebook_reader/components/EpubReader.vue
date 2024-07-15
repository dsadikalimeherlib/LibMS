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
            <v-hover v-slot="{ isHovering, props }">
              <v-btn icon @click="previousPage" v-bind="props" :elevation="isHovering ? 24 : 8">
                <v-icon>mdi-chevron-left</v-icon>
              </v-btn>
            </v-hover>
          </v-col>
          <v-col class="d-flex justify-center align-items-center mt-4">
            <v-hover v-slot="{ isHovering, props }">
              <v-card class="epub-card mx-auto  mt-4 border border-dark border-5 rounded-5" v-bind="props"
                :elevation="isHovering ? 24 : 8">
                <div v-if="book.type === 'epub'" id="epub-render-area"></div>
              </v-card>
            </v-hover>
          </v-col>
          <v-col class="d-flex justify-end align-items-center">
            <v-hover v-slot="{ isHovering, props }">
              <v-btn icon @click="nextPage" v-bind="props" :elevation="isHovering ? 24 : 8">
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-hover>
          </v-col>
        </v-row>
      </v-main>
      <v-bottom-navigation class="bg-light">
        <v-spacer></v-spacer>
        <div class="d-flex justify-center align-items-center">
          <v-btn icon @click="previousPage" size="small">
            <v-icon>mdi-arrow-left</v-icon>
          </v-btn>
          <v-text-field v-model="manualPage" @keyup.enter="navigateToPage(manualPage)" @mouseleave="updatePlaceholder"
            class="mx-2 mt-2 page-input-field" min="1" :max="totalPages" outlined dense small>
          </v-text-field>
          <v-btn icon @click="nextPage" size="small">
            <v-icon>mdi-arrow-right</v-icon>
          </v-btn>
        </div>
        <v-spacer></v-spacer>
        <div class="d-flex justify-end align-items-right">
          <v-btn icon size="small" @click="zoomOut" class="mb-2">
            <v-icon>mdi-minus</v-icon>
          </v-btn>
          <v-btn icon size="small" @click="zoomIn" class="mb-2">
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </div>
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
      zoomLevel: 100,
      fontSize: 16,
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

          this.rendition = new Rendition(this.bookInstance, {
            flow: 'paginated',
            width: window.innerWidth - 150,
            height: window.innerHeight - 200,
            manager: 'default',
            spread: 'none',
          });
          this.rendition.attachTo("epub-render-area");
          this.rendition.display();

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
    zoomIn() {
      if (this.fontSize < 22) {
        this.fontSize += 1;
        this.applyZoom();
      }
    },
    zoomOut() {
      if (this.fontSize > 16) {
        this.fontSize -= 1;
        this.applyZoom();
      }
    },
    applyZoom() {
      if (this.rendition) {
        this.rendition.themes.default({
          'body': {
            'font-size': `${this.fontSize}px !important`,
            'line-height': '1.6 !important'
          }
        });
        this.rendition.resize();
        // this.rendition.display(this.page);
      }
    }
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

.epub-card {
  width: calc(100% - 150px);
  max-width: 700px;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

#epub-render-area {
  height: calc(100vh - 200px);
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

#epub-render-area,
#epub-render-area * {
  font-size: inherit !important;
}
</style>