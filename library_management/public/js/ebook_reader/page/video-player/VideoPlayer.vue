<template>
    <div v-if="store.media_detail" class="video-player-wrapper">

        <div class="left-column">
            <div class="iframe-wrapper">
                <Video :media="store.media_detail" />
            </div>
            <div class="video-detail">
                <div class="title">{{ store.media_detail.title }}</div>
                <div class="meta-wrapper">
                    <div v-if="store.media_detail.year_of_publication !== null" class="meta">
                        <div class="label">Year:</div>
                        <div class="value">{{ store.media_detail.year_of_publication }}</div>
                    </div>
                    <div class="meta">
                        <div class="label">Category:</div>
                        <div class="value">{{ store.media_detail.category }}</div>
                    </div>
                </div>
                <div v-html="store.media_detail.description" class="description"></div>
            </div>
        </div>
        <div class="right-column">
            <div class="related-medias-section">
                <template v-for="item in store.medias" :key="item.title">
                    <MultimediaHorizonta v-if="media_id !== item.id && item.media_type == 'Video'"
                        :onLinkClick="onLinkClick" :media="item" />
                </template>


            </div>
        </div>
    </div>
</template>

<script setup>
import BookField from '../../components/book-field/BookField.vue';
import MultimediaHorizonta from '../../components/multimedias/MultimediaHorizonta.vue';
import Video from '../../components/multimedias/Video.vue';



import { onMounted } from 'vue';
import { useBooksStore } from '../../../books/store';
const store = useBooksStore();
const url = new URL(window.location.href);
const params = new URLSearchParams(url.search);
const media_id = params.get('id');
onMounted(() => {

    store.get_mediaDetail({ media_id });
});

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
        media_url: '2u5jJT9xFd4',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint  occaecat cupidatat non proident, sunt in culpa qui officia deserunt  mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmo.'

    },
    medias: [
        {
            title: 'Media 1',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Video',
        },
        {
            title: 'Media 2',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Audio',
        },
        {
            title: 'Media 3',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Video',
        },
        {
            title: 'Media 4',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Audio',
        },
        {
            title: 'Media 5',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Video',
        },
        {
            title: 'Media 6',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Audio',
        },
        {
            title: 'Media 7',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Video',
        },
        {
            title: 'Media 8',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Audio',
        },
        {
            title: 'Media 9',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Video',
        }
    ]

}
const media = mediastore.media
const medias = mediastore.medias
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
        },

    }
}
</script>
<style scoped>
@import "./video-player.css";
</style>