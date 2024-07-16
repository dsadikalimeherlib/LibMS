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
        <div class="d-flex justify-content-center align-items-center mx-24">
          <v-btn icon @click="previousPage" size="small">
            <v-icon>mdi-arrow-left</v-icon>
          </v-btn>
          <v-text-field v-model="manualPage" @keyup.enter="navigateToPage(manualPage)" @mouseleave="updatePlaceholder"
            class="mx-24 mt-2 text-center" min="1" :max="totalPages" outlined align="center" style="width: 200px;">
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
      fontSize: 16,
    };
  },
  watch: {
    page(newVal) {
      this.manualPage = newVal.toString();
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

          this.getTotalPages();
          this.loadToc();
          this.show = true;
        } catch (error) {
          console.error('Error loading book:', error);
        }
      }
    },
    nextPage() {
      if (this.rendition) {
        this.rendition.next().then(() => {
          this.updateCurrentPage();
        });
      }
    },
    previousPage() {
      if (this.rendition) {
        this.rendition.prev().then(() => {
          this.updateCurrentPage();
        });
      }
    },
    navigateToPage(pageNum) {
      let parsedPageNum = parseInt(pageNum, 10);

      const tryDisplayPage = (pageNum) => {
        if (pageNum < 1) {
          return;
        }

        this.rendition.display(pageNum).then(() => {
          this.page = pageNum;
          this.updatePlaceholder();
        }).catch((error) => {
          tryDisplayPage(pageNum - 1);
        });
      };

      if (parsedPageNum && parsedPageNum >= 1 && parsedPageNum <= this.totalPages) {
        tryDisplayPage(parsedPageNum);
      } else {
        return;
      }
    },
    async navigateToHref(href) {
      if (this.rendition) {
        try {
          await this.rendition.display(href);
          this.updateCurrentPage();
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
            this.updatePlaceholder();
          }
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
          console.error("Navigation is not loaded or book instance is not available");
        }
      } catch (error) {
        console.error('Error loading the Table of Contents:', error);
        this.toc = [];
      }
    },
    zoomIn() {
      if (this.fontSize < 22) {
        this.fontSize += 1;
        this.applyZoom();
        // this.getTotalPages();
      }
    },
    zoomOut() {
      if (this.fontSize > 16) {
        this.fontSize -= 1;
        this.applyZoom();
        // this.getTotalPages();
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
      }
    },
    getTotalPages() {
      this.bookInstance.locations.generate(33000).then(() => {
        this.totalPages = this.bookInstance.locations.total;
        this.updatePlaceholder();
      });
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

.text-center input::placeholder {
  text-align: center;
}

.text-center input {
  text-align: center;
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