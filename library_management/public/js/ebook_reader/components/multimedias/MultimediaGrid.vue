<template>
    <div class="media-grid-section">
        <div class="media-list-wrapper" :class="media_type">
            <template v-for="item in medias" :key="item.title">
                <Multimedia :onLinkClick="onLinkClick" :media="item" :media_type="media_type" />
            </template>


        </div>
    </div>
</template>

<script setup>
import Multimedia from './Multimedia.vue';
</script>

<script>


export default {
    props: {
        medias: {
            type: Array,
            required: true
        },
        onLinkClick: {
            type: Function,
            required: true
        },
        media_type: {
            type: String,
            required: true
        }
    },
    methods: {
        handleClick(pageName) {

            // Call the function passed via prop
            if (this.onLinkClick) {
                this.onLinkClick(pageName);
            }
        }
    }
}
</script>

<style scoped>
@import './multimediaGrid.css'
</style>
