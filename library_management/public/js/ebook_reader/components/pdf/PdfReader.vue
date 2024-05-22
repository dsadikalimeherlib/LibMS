<template>
    <v-dialog v-model="show" fullscreen hide-overlay>
        <v-app>
            <v-app-bar dense elevatedwill>
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
                                <canvas id="pdf-canvas"> </canvas>
                            </v-card-text>
                        </v-card>
                    </v-col>
                    <v-col class="d-flex justify-end align-items-center">
                        <div>
                            <v-btn icon @click="nextPage">
                                <v-icon>mdi-chevron-right</v-icon>
                            </v-btn>
                        </div>

                        
                    </v-col>
                </v-row>
                <v-row>
                    <v-footer padless height="45" class="mt-6 d-flex justify-center align-center">
                        <v-spacer></v-spacer>
                        <v-btn icon @click="previousPage">
                            <v-icon>mdi-arrow-left</v-icon>
                        </v-btn>
                        <span class="mx-2">Page {{ page }} of {{ totalPages }}</span>
                        <v-btn icon @click="nextPage">
                            <v-icon>mdi-arrow-right</v-icon>
                        </v-btn>
                        <v-spacer></v-spacer>
                    </v-footer>
                </v-row>
            </v-main>
        </v-app>
    </v-dialog>
</template>

<script>


export default {
    name: 'PdfReader',
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
            toc: [],
            isTocVisible: false,
            manualPage: '',
            scale: 6,
            showToc: ["Toc"],
        };
    },
    watch: {
        page(newVal) {
            this.manualPage = newVal;
        }
    },
    methods: {
        async loadPdf() {
            try {
                this.url = frappe.urllib.get_full_url(this.book.book_url);

                const loadingTask = pdfjsLib.getDocument(this.url);
                this.pdfDoc = await loadingTask.promise;
                this.totalPages = this.pdfDoc.numPages;
                this.loadToc();
                this.renderPage();
                this.show = true;

            } catch (error) {
                console.error('Error loading PDF:', error);
            }
        },
        async renderPage() {
            try {
                const page = await this.pdfDoc.getPage(this.page);
                const canvas = document.getElementById('pdf-canvas');
                const context = canvas.getContext('2d');
                const viewport = page.getViewport({ scale: this.scale });
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
            if (this.book.type === 'pdf' && this.page < this.totalPages) {
                this.page++;
                this.renderPage();
            }
        },
        previousPage() {
            if (this.book.type === 'pdf' && this.page > 1) {
                this.page--;
                this.renderPage();
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
        toggleToc() {
            this.isTocVisible = !this.isTocVisible;
        },
        zoomIn() {
            this.scale *= 1.1; // Increase scale by 10%
            this.renderPage();
        },
        zoomOut() {
            this.scale /= 1.1; // Decrease scale by 10%
            this.renderPage();
        },
    },
    created() {
        this.loadPdf();
    },
};
</script>

<style scoped>
.v-card-text {
    overflow: auto;
}

#pdf-canvas {
    height: calc(80vh - 80px);
    width: 700px;
    overflow: auto;
}

.wrap-text {
    white-space: normal;
    word-wrap: break-word;
    width: 100%;
}
</style>
