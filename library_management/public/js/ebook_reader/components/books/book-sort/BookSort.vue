<script setup lang="ts">
import BookSortItem from './BookSortItem.vue';
</script>

<template>
    <div class="icons-wrapper">
        Sort
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M5 7H19" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
            <path d="M5 12H15" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
            <path d="M5 17H11" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
        </svg>
        <div class="sort-filter-popup 1">
            <div class="title-wrapper">
                <div class="title">Sort112</div>
                <div class="close-icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                        viewBox="0 0 24 24" fill="none">
                        <path d="M18 6L6 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M6 6L18 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                    </svg></div>
            </div>
            <div class="sort-filter-column-wrapper">
                <!-- <div class="column">
                    <template v-for="item in firstHalf" :key="item.title">
                        <BookSortItem :sortItem="item" />
                    </template>
</div>
<div class="column">
    <template v-for="item in secondHalf" :key="item.title">
                        <BookSortItem :sortItem="item" />
                    </template>
</div> -->
            </div>
        </div>
    </div>
</template>

<script>
// const sortItems = [
//     {
//         title: 'Book Title',
//     },
//     {
//         title: 'Author',
//     },
//     {
//         title: 'Language',
//     },
//     {
//         title: 'Subject',
//     },
//     {
//         title: 'Publication Year',
//     },
//     {
//         title: 'Publisher',
//     }
// ]
// const middleIndex = Math.floor(sortItems.length / 2);
// // Split the array into two parts
// const firstHalf = array.slice(0, middleIndex);
// const secondHalf = array.slice(middleIndex);
</script>