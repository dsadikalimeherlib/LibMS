<template>

    <div class="media-detail-wrapper">
        <div class="inner-container">
            <div class="media-image-title-wrapper">

                <div class="image-wrapper">
                    <v-img :src="media.image_url !== '' ? media.image_url
                        : '/files/default-media.png'">
                    </v-img>
                    <div class="player-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="70" height="70" viewBox="0 0 70 70" fill="none">
                            <ellipse cx="35.2552" cy="35.2557" rx="34.4193" ry="34.5229" fill="#00B0AB" />
                            <path
                                d="M56.4188 34.3617L21.6955 16.9478C20.8975 16.5476 19.9575 17.1278 19.9575 18.0205V52.4908C19.9575 53.3834 20.8975 53.9636 21.6955 53.5634L56.4188 36.1495C57.1544 35.7806 57.1544 34.7306 56.4188 34.3617Z"
                                fill="white" />
                        </svg>
                    </div>
                </div>
                <div class="title-wrapper">
                    <h1>{{ media.title }}</h1>
                </div>

            </div>
            <div class="media-detail-section">
                <div class="description-wrapper">
                    <div class="description">{{ media.description }} </div>
                    <div class="button-wrapper">
                        <div class="primary-button" @click="handleClick('video-player')"><svg
                                xmlns="http://www.w3.org/2000/svg" width="19" height="20" viewBox="0 0 19 20"
                                fill="none">
                                <path
                                    d="M18.2111 9.10557L1.73666 0.868328C0.938776 0.469388 0 1.04958 0 1.94164V18.0584C0 18.9504 0.938776 19.5306 1.73666 19.1317L18.2111 10.8944C18.9482 10.5259 18.9482 9.4741 18.2111 9.10557Z"
                                    fill="white" />
                            </svg>Play Video</div>
                    </div>
                </div>


            </div>
        </div>
    </div>
</template>
<script setup>
import BookField from '../../components/book-field/BookField.vue';



// import { onMounted } from 'vue';
// import { useBooksStore } from '../../../../books/store';
// const bookstore = useBooksStore();
const mediastore = {
    media:
    // {

    //     book_title: 'મુન્તખબ મીઝાનુલ હિકમા',
    //     author: 'Author'
    // }
    {
        id: "",
        title: 'Media 1',
        date: '19-Sep-2022 4:07 PM',
        category: 'કરબલાના બહાદુરો',
        duration: '00:20:00',
        media_type: 'Video',
        image_url: '',
        media_url: '',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint  occaecat cupidatat non proident, sunt in culpa qui officia deserunt  mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmo.'

    }

}
const media = mediastore.media
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
    }
}
</script>
<style scoped>
@import "./mediaDetail.css";
</style>
