<template>
    <div v-if="media_type == '' || media_type == media.media_type" @click="handleClick(`media-detail&id=${media.id}`)"
        :class="media.media_type" class="media-item">
        <div class="image-wrapper">
            <v-img :src="media.image_url ? media.image_url
                : '/files/default-media.png'">
            </v-img>
            <div class="player-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30" fill="none">
                    <circle cx="15" cy="15" r="15" fill="#00B0AB" />
                    <path
                        d="M23.2111 14.1055L10.07 7.53495C9.27211 7.13601 8.33333 7.71621 8.33333 8.60827V21.3917C8.33333 22.2837 9.27211 22.8639 10.07 22.465L23.2111 15.8944C23.9482 15.5259 23.9482 14.4741 23.2111 14.1055Z"
                        fill="white" />
                </svg>
            </div>
            <div v-if="media.duration !== null" class="duration">{{ media.duration }}</div>
        </div>
        <div class="book-detail">
            <div class="title">{{ media.title }}</div>
            <div class="meta-wrapper">
                <!-- <div class="meta"><span class="label">Date:</span> {{ media.date
                    }}</div> -->
                <div class="meta"><span class="label">Category:</span> {{ media.category
                    }}</div>
                <div class="meta"><span class="label">Type:</span> {{ media.media_type
                    }}</div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    props: {
        media: {
            type: Object,
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
};
</script>

<style scoped>
@import "./multimediaStyle.css";
</style>