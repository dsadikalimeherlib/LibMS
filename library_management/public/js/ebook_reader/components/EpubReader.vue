<template>
  <v-dialog v-model="show" fullscreen hide-overlay>
    <v-app>
      <v-app-bar dense elevatedwill>
        <EpubTitlebar :title="book.title" @close-reader="closeReader" />
      </v-app-bar>
      <v-main>
        <v-row>
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

export default {
  name: 'EpubReader',
  components: {
    EpubTitlebar,
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
      manualPage: '',
    };
  },
  watch: {
    page(newVal) {
      this.manualPage = newVal.toString();
      this.updatePlaceholder();
    }
  },
  methods: {
    async loadEPUB() {
      if (this.book && this.book.book_url) {
        try {
          this.url = frappe.urllib.get_full_url(this.book.book_url);

          this.bookInstance = new Book(this.url);
          await this.bookInstance.ready;

          this.rendition = new Rendition(this.bookInstance, {
            width: "100%",
            height: "100%",
          });
          this.rendition.attachTo("epub-render-area");
          this.rendition.display();

          this.totalPages = this.bookInstance.spine.length;
          this.show = true;
        } catch (error) {
          console.error('Error loading book:', error);
        }
      }
    },
    nextPage() {
      if (this.book.type === 'epub' && this.rendition) {
        this.page++;
        this.rendition.next();
        this.updatePlaceholder();
      }
    },
    previousPage() {
      if (this.book.type === 'epub' && this.rendition) {
        this.page--;
        this.rendition.prev();
        this.updatePlaceholder();
      }
    },
    navigateToPage(pageNum) {
      pageNum = parseInt(pageNum, 10);
      if (pageNum && pageNum >= 1 && pageNum <= this.totalPages) {
        this.page = pageNum;
        this.rendition.display(this.page);
        this.updatePlaceholder();
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