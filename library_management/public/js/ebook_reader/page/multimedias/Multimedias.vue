<template>
    <div class="medias-wrapper">
        <div class="inner-container">
            <div class="page-header">
                <h1>Multimedia</h1>
                <div class="right">
                    <div class="icons-wrapper">
                        <div :class="gridActiveClass" @click="setShowGrid(true)">
                            <svg width="31" height="24" viewBox="0 0 31 24" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <rect x="6" y="6" width="5" height="5" fill="#33363F" />
                                <rect x="13" y="6" width="5" height="5" fill="#33363F" />
                                <rect x="20" y="6" width="5" height="5" fill="#33363F" />
                                <rect x="6" y="13" width="5" height="5" fill="#33363F" />
                                <rect x="13" y="13" width="5" height="5" fill="#33363F" />
                                <rect x="20" y="13" width="5" height="5" fill="#33363F" />
                            </svg>
                        </div>
                        <div :class="listActiveClass" @click="setShowGrid(false)">
                            <svg width="25" height="18" viewBox="0 0 25 18" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <rect x="3" y="3" width="5" height="5" fill="#33363F" />
                                <rect x="10" y="4" width="12" height="3" fill="#33363F" />
                                <rect x="3" y="10" width="5" height="5" fill="#33363F" />
                                <rect x="10" y="11" width="12" height="3" fill="#33363F" />
                            </svg>
                        </div>
                    </div>
                    <MultimediaSort />
                    <MultimediaFilter />
                </div>
            </div>

            <MultimediaGrid :onLinkClick="onLinkClick" v-if="showGrid" :medias="mediastore.medias" />
            <MultimediaList :onLinkClick="onLinkClick" v-else :medias="mediastore.medias" />
        </div>
    </div>
</template>
<script setup>
import MultimediaGrid from '../../components/multimedias/MultimediaGrid.vue';
import MultimediaList from '../../components/multimedias/MultimediaList.vue';
import MultimediaSort from '../../components/multimedias/multimedia-sort/MultimediaSort.vue';
import MultimediaFilter from '../../components/multimedias/multimedia-filter/MultimediaFilter.vue';
import { useBooksStore } from '../../../books/store';
import { onMounted } from 'vue';
const mediastore = useBooksStore();
const url = new URL(window.location.href);
const params = new URLSearchParams(url.search);
const category = params.get('category');
onMounted(() => {

    mediastore.get_media({ length: 18, category: category !== null ? category : '' });
});

</script>
<script>
let showGridValue = localStorage.getItem('showGrid')
if (showGridValue == null) {
    showGridValue = true
} else {
    showGridValue = JSON.parse(showGridValue)
}
export default {
    props: {
        onLinkClick: {
            type: Function,
            required: true
        },
    },
    methods: {
        setShowGrid(value) {
            this.showGrid = value
            localStorage.setItem('showGrid', value)
        },

    },
    data() {
        return {
            showGrid: showGridValue,
            showSortPopup: false
        };
    },
    computed: {
        gridActiveClass() {
            return [
                'icon-wrapper',  // Static class
                {
                    active: this.showGrid,
                }
            ];
        },
        listActiveClass() {
            return [
                'icon-wrapper',  // Static class
                {
                    active: !this.showGrid,
                }
            ];
        },

    }
}
</script>
<style scoped>
@import "./style.css";
</style>
