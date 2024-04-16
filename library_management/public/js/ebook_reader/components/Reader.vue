<template>
  <v-dialog v-model="show" fullscreen hide-overlay>
    <v-app>
      <v-app-bar dense elevatedwill>
        <Titlebar :title="book.title" @close-reader="closeReader" />
      </v-app-bar>
      <v-main>
        <v-row>
          <v-col class="d-flex justify-start align-items-center">
            <v-btn icon @click="previousPage">
              <v-icon>mdi-chevron-left</v-icon>
            </v-btn>
          </v-col>
          <v-col class="align-items-center">
            <v-card
              class="mx-auto mt-8"
              max-width="1000"
              max-height="800"
              hover
            >
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
      <v-footer padless height="45">
        <!-- <v-slider v-model="sliderValue" :step="0.01" :format="lableFromPercentage" @change="onSliderValueChange" /> -->
        page footer
      </v-footer>

      <!-- <buble-menu ref="bubleMenu" @highlight-btn-click="highlightSelection" /> -->
    </v-app>
  </v-dialog>
</template>

<script>
// Import your components like toc-menu, bookmark-menu etc.
import { Book, Rendition } from 'epubjs';

import Titlebar from './Titlebar.vue';

export default {
  name: 'Reader',
  components: {
    Titlebar,
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
    };
  },
  methods: {
    async renderPage() {
      if (this.book && this.book.book_url) {
        this.url = frappe.urllib.get_full_url(this.book.book_url);

        if (this.book.type === 'epub') {
          this.loadEPUB();
        } 
      }
    },

    async loadEPUB() {
      try {
        this.bookInstance = new Book(this.url);
        await this.bookInstance.ready;

        this.rendition = new Rendition(this.bookInstance, {
          width: "100%",
          height: "100%",
        });
        this.rendition.attachTo("epub-render-area");
        this.rendition.display();

        this.show = true;
      } catch (error) {
        console.error('Error loading book:', error);
      }
    },
    nextPage() {
      if (this.book.type === 'epub' && this.rendition) {
        this.rendition.next();
      }
    },
    previousPage() {
      if (this.book.type === 'epub' && this.rendition) {
        this.rendition.prev();
      }
    },
    closeReader() {
      if (this.rendition) {
        this.rendition.destroy();
        this.bookInstance = null;
        this.bookTitle = '';
        this.show = false;
      }
    },
  },
  created() {
    this.renderPage();
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
</style>