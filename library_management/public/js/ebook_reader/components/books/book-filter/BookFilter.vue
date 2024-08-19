<template>
    <div class="icons-wrapper sort">
        <div @click="setShowSortPopup(!showSortPopup)" class="title-icon-wrapper">
            Filters
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M5 12L5 4" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                <path d="M19 20L19 18" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                <path d="M5 20L5 16" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                <path d="M19 12L19 4" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                <path d="M12 7L12 4" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                <path d="M12 20L12 12" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                <circle cx="5" cy="14" r="2" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                <circle cx="12" cy="9" r="2" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                <circle cx="19" cy="15" r="2" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
            </svg>
        </div>
        <div v-if="showSortPopup" class="sort-filter-popup">
            <div class="title-wrapper">
                <div class="title">Filters</div>
                <div class="right">
                    <div class="clear">Clear All</div>
                    <div @click="setShowSortPopup(false)" class="close-icon"><svg xmlns="http://www.w3.org/2000/svg"
                            width="24" height="24" viewBox="0 0 24 24" fill="none">
                            <path d="M18 6L6 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M6 6L18 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                        </svg></div>
                </div>
            </div>
            <div class="sort-filter-column-wrapper filter">
                <div class="column">
                    <div class="item">
                        <div class="label">Book title</div>
                        <div class="field">
                            <select>
                                <option>Tafseer</option>
                                <option>Tafseer1</option>
                            </select>
                            <svg class="dropdown-icon" xmlns="http://www.w3.org/2000/svg" width="12" height="7"
                                viewBox="0 0 12 7" fill="none">
                                <path
                                    d="M10 2L6.22154 4.93122C6.16061 4.97551 6.08174 5 6 5C5.91826 5 5.83939 4.97551 5.77846 4.93122L2 2"
                                    stroke="#545353" stroke-width="2.31353" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg>
                        </div>
                    </div>
                    <div class="item">
                        <div class="label">Author</div>
                        <div class="field">
                            <select>
                                <option>Tafseer</option>
                                <option>Tafseer1</option>
                            </select>
                            <svg class="dropdown-icon" xmlns="http://www.w3.org/2000/svg" width="12" height="7"
                                viewBox="0 0 12 7" fill="none">
                                <path
                                    d="M10 2L6.22154 4.93122C6.16061 4.97551 6.08174 5 6 5C5.91826 5 5.83939 4.97551 5.77846 4.93122L2 2"
                                    stroke="#545353" stroke-width="2.31353" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg>
                        </div>
                    </div>
                </div>
                <div class="column">
                    <template v-for="item in secondHalf" :key="item.title">
                        <BookFilterItem :sortItem="item" />
                    </template>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import BookFilterItem from './BookFilterItem.vue';
</script>

<script>
export default {
    data() {
        return {
            array: [
                {
                    title: 'Book Title',
                },
                {
                    title: 'Author',
                },
                {
                    title: 'Language',
                },
                {
                    title: 'Subject',
                },
                {
                    title: 'Publication Year',
                },
                {
                    title: 'Publisher',
                }
            ],
            showSortPopup: false
        };
    },
    methods: {
        setShowSortPopup(value) {
            this.showSortPopup = value
        }
    },
    computed: {
        middleIndex() {
            return Math.floor(this.array.length / 2);
        },
        firstHalf() {
            return this.array.slice(0, this.middleIndex);
        },
        secondHalf() {
            return this.array.slice(this.middleIndex);
        },
    },
};
</script>