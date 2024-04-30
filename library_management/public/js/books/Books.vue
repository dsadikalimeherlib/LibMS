<template>
    <v-container fluid class="pa-0 ma-0">
        <v-row class="align-center pa-0 ma-0">
            <v-col cols="12">
                <v-card outlined>
                    <v-toolbar color="info">
                        <v-toolbar-title>Book List</v-toolbar-title>
                        <v-spacer></v-spacer>
                        <v-text-field bg-color="white" color="blue darken-2" rounded-lg dense
                            v-model="bookstore.search_book" append-icon="mdi-magnify" label="Search Books"
                            @input="bookstore.search_books()" single-line hide-details>
                        </v-text-field>
                    </v-toolbar>
                    <v-divider></v-divider>
                    <v-container class="overflow-y-auto" style="max-height: calc(100vh - 112px);">
                        <v-row align="center" class="fill-height" justify="center">
                            <template v-for="item in bookstore.books" :key="item.title">
                                <v-col cols="12" sm="6" md="4" lg="3">
                                    <v-hover v-slot="{ isHovering, props }">
                                        <v-card :class="{ 'on-hover': isHovering }" :elevation="isHovering ? 12 : 2"
                                            v-bind="props" @click="selectBook(item)">
                                            <v-img :src="item.image ? item.image
                                                : 'https://placehold.co/150?text=Item'" height="300px"
                                                class="white--text align-end">
                                            </v-img>
                                            <v-card-subtitle
                                                class="text-h6 text-center text-body-3 text-sm-left text-dark d-flex flex-column">
                                                <p class="mt-1 text-center">
                                                    {{ item.title }}
                                                </p>
                                            </v-card-subtitle>
                                            <v-card-text class="pa-1">
                                                <p class="ma-0 text-body-6 text-sm-left">
                                                    By: <span class="font-weight-medium">{{ item.author }}</span>
                                                </p>
                                                <p class="text-caption text-sm-left">
                                                    Subject: <span class="font-weight-medium">{{ item.subject }}</span>
                                                </p>
                                                <div class="text-center justify-content" v-show="isHovering">
                                                    <v-btn @click.stop="selectBook(item)" class="mt-2"
                                                        :class="{ 'show-btns': isHovering }" color="info">
                                                        <span class="mdi mdi-read"></span>
                                                        Read
                                                    </v-btn>
                                                </div>
                                            </v-card-text>
                                        </v-card>
                                    </v-hover>
                                </v-col>
                            </template>
                        </v-row>
                    </v-container>
                </v-card>
            </v-col>
        </v-row>
        <v-dialog v-model="isReaderOpen" fullscreen hide-overlay transition="dialog-bottom-transition">
            <Reader :book="selectedBook" :show="isReaderOpen" @close-reader="isReaderOpen = false" />
        </v-dialog>
    </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useBooksStore } from './store';
import Reader from '../ebook_reader/components/Reader.vue';


const bookstore = useBooksStore();
const selectedBook = ref(null);
const isReaderOpen = ref(false);

const selectBook = (book) => {
    selectedBook.value = book;
    isReaderOpen.value = true;
}

onMounted(() => {
    bookstore.get_books();
});
</script>


<style scoped>
.v-card img {
    object-fit: cover;
}
</style>
