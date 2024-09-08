<template>
    <div class="book-categories-page">
        <h1>Multimedia Categories</h1>
        <div class="category-list-wrapper">
            <template v-for="item in mediaCategoryStore.media_categories" :key="item.category">
                <div class="item" @click="handleClick(`multimedia&category=${item.category}`)">
                    <div class="icon-wrapper" style="background-image: url(/files/round.png);"><img :src="item.image ? item.image
                        : 'https://placehold.co/150?text=Item'" />
                    </div>
                    <div class="title">{{ item.category }}</div>
                </div>
            </template>
        </div>

    </div>
</template>


<script setup>
import { onMounted } from 'vue';
import { useBooksStore } from '../../../books/store';
const mediaCategoryStore = useBooksStore();

onMounted(() => {
    mediaCategoryStore.get_mulitmedia_category({ length: null });

});

</script>

<script>
export default {
    props: {
        onLinkClick: {
            type: Function,
            required: true
        },
    },
    methods: {
        handleClick(pageName) {
            // Call the function passed via prop
            if (this.onLinkClick) {
                this.onLinkClick(pageName);
            }
        }
    },
}
</script>

<style scoped>
@import "./mediaCategories.css";
</style>
