<template>
    <div @click="handleClick(`book-detail&id=${book.id}`)" class="bookItem">
        <div class="image-wrapper"><v-img :src="book.image_url ? book.image_url
            : 'https://placehold.co/150?text=Item'">
            </v-img></div>
        <div class="book-detail">
            <div class="title">{{ book.title }}</div>
            <div class="meta-wrapper">
                <div class="meta"><span class="label">Author:</span> {{ book.author
                    }}</div>
                <div class="meta"><span class="label">Language:</span> {{ book.language }}</div>
                <div class="meta"><span class="label">Sect:</span> Shia</div>
                <div class="meta"><span class="label">Category:</span> {{ book.category }}</div>
                <div class="meta"><span class="label">Availability:</span> <span class="avail-value">Yes</span></div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    props: {
        book: {
            type: Object,
            required: true
        },
        onLinkClick: {
            type: Function,
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
@import "./bookStyle.css";
</style>