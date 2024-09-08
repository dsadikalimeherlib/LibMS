<template>
    <div :class="navigationClass">
        <button @click="handleClick('book-categories')">Book categories</button>
        <button @click="handleClick('media-categories')">Multimedia Categories</button>
        <button @click="handleClick('about')">Apply Membership</button>
        <button @click="handleClick('fees')">Fees</button>
        <button @click="handleClick('news-announcement')">News & Announcements</button>
        <button @click="handleClick('holidays')">Holidays</button>
        <button @click="handleClick('about')">Contact us</button>
        <button @click="handleClick('about')">Feedback</button>
    </div>
</template>
<script>


export default {
    props: {
        onLinkClick: {
            type: Function,
            required: true
        },
        isSticky: {
            type: Boolean,
            required: false
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
    computed: {
        navigationClass() {
            return [
                'navigation',  // Static class
                {
                    sticky: this.isSticky,
                }
            ];
        }
    }
}
</script>
<style scoped>
@import "./style.css";
</style>
