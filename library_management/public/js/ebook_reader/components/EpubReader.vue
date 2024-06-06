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
      pdfDoc: null,
      page: 1,
      totalPages: 0,
    };
  },
  methods: {
    async renderPage() {
      if (this.book && this.book.book_url) {
        this.url = frappe.urllib.get_full_url(this.book.book_url);

        if (this.book.type === 'epub') {
          this.loadEPUB();
        } else if (this.book.type === 'pdf') {
          this.loadPDF();
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
    async loadPDF() {
      try {
        const loadingTask = pdfjsLib.getDocument(this.url);
        this.pdfDoc = await loadingTask.promise;
        this.totalPages = this.pdfDoc.numPages;
        this.renderPDFPage();
        this.show = true;

      } catch (error) {
        console.error('Error loading PDF:', error);
      }
    },
    async renderPDFPage() {
      try {
        const page = await this.pdfDoc.getPage(this.page);
        const canvas = document.getElementById('pdf-canvas');
        const context = canvas.getContext('2d');
        const viewport = page.getViewport({ scale: 1.25 });
        canvas.height = viewport.height;
        canvas.width = viewport.width;

        const renderContext = {
          canvasContext: context,
          viewport: viewport,
        };
        await page.render(renderContext).promise;

      } catch (error) {
        console.error('Error rendering page:', error);
      }
    },
    nextPage() {
      if (this.book.type === 'epub' && this.rendition) {
        this.rendition.next();

      } else if (this.book.type === 'pdf' && this.page < this.totalPages) {
        this.page++;
        this.renderPDFPage();
      }
    },
    previousPage() {
      if (this.book.type === 'epub' && this.rendition) {
        this.rendition.prev();

      } else if (this.book.type === 'pdf' && this.page > 1) {
        this.page--;
        this.renderPDFPage();
      }
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

#pdf-canvas {
  height: calc(80vh - 80px);
  width: 700px;
  overflow: auto;
}
</style>