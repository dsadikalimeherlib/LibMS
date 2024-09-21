<template>
    <div class="search-wrapper">
        <div class="search-input-wrapper">
            <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="19" height="19" viewBox="0 0 19 19" fill="none">
                <path
                    d="M7.9427 14.8416C11.5009 14.8416 14.3854 11.855 14.3854 8.1708C14.3854 4.48662 11.5009 1.5 7.9427 1.5C4.38449 1.5 1.5 4.48662 1.5 8.1708C1.5 11.855 4.38449 14.8416 7.9427 14.8416Z"
                    stroke="#818098" stroke-width="2.31353" stroke-linecap="round" stroke-linejoin="round" />
                <path d="M16.9531 17.5L12.4955 12.8846" stroke="#818098" stroke-width="2.31353" stroke-linecap="round"
                    stroke-linejoin="round" />
            </svg>
            <input v-model="message" @input="debouncedSearch"
                placeholder="Looking for specific book? Enter Book Title here.." />
            <div v-if="message !== ''" @click="clearSearchInput" class="close-btn">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M18 6L6 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M6 6L18 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
            </div>
        </div>
        <div v-if="showSearchSuggestions" class="search-dropdown">
            <ul class="tab-wrapper">
                <ul class="tab-wrapper">
                    <li @click="filterResults('', searchStore.results)" :class="selectedFilter == '' ? 'active' : ''">
                        All<span>{{
                            searchStore.totalResults }}</span></li>
                    <template v-for="searchFitler in searchFitlers" :key="searchFitler">
                        <li @click="filterResults(searchFitler, searchStore.results)"
                            :class="selectedFilter == searchFitler ? 'active' : ''">{{ searchFitler
                            }}s<span>{{
                                searchStore.categoryCounts[searchFitler] || 0 }}</span></li>
                    </template>
                </ul>
            </ul>
            <ul class="results">

                <template v-for="result in showFilteredData ? filteredData : searchStore.results" :key="result.id">
                    <li
                        @click="handleClick(`${result.type == 'Video' || result.type == 'Audio' ? `media-detail&id=${result.id}` : `book-detail&id=${result.id}`}`, true); clearSearchInput()">
                        <div class="result-title">{{ result.name }}</div>
                        <div class="category">{{ result.category }}</div>
                    </li>
                </template>
            </ul>
        </div>
    </div>
</template>
<script setup>
import { debounce } from "lodash";
import { onMounted, ref } from 'vue';
import { useBooksStore } from '../../../books/store';
const searchStore = useBooksStore();
const message = ref('');
const showSearchSuggestions = ref(false);
const searchFitlers = ['Book', 'Magazine', 'E-Book', 'Video', 'Audio']
onMounted(() => {
    searchStore.search('Hajjaj ibn Yusuf ath-Thaqafi, Historical Stories For Children 1');

});

// Debounced search method
const debouncedSearch = debounce(() => {
    if (message.value.trim() === '') {
        showSearchSuggestions.value = false;
        return;
    }
    searchStore.search(message.value);
    showSearchSuggestions.value = true;
}, 300); // 300ms debounce delay

// Lifecycle hook
onMounted(() => {
    searchStore.search('Hajjaj ibn Yusuf ath-Thaqafi, Historical Stories For Children 1');
});

// Method to clear search input
const clearSearchInput = () => {
    message.value = ""; // Clear the input value
    showSearchSuggestions.value = false; // Hide the suggestions
};

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
        handleClick(pageName, refresh) {
            // Call the function passed via prop
            if (this.onLinkClick) {
                this.onLinkClick(pageName, refresh);
            }
        },
        setShowSearchSuggestions(value) {
            this.showSearchSuggestions = value
        },
        filterResults(key, data) {
            let filteredData = []
            if (key == '') {
                this.showFilteredData = false
            } else if (key == 'Video' || key == 'Audio') {
                this.showFilteredData = true
                filteredData = data.filter(item => item.type.toLowerCase() == key.toLowerCase());
            } else {
                this.showFilteredData = true
                filteredData = data.filter(item => item.category.toLowerCase() == key.toLowerCase());
            }

            this.selectedFilter = key


            this.filteredData = filteredData


        }
    },
    data() {
        return {
            showSearchSuggestions: false,
            message: '',
            filteredData: [],
            showFilteredData: false,
            selectedFilter: ''
        };
    },
}
</script>
<style scoped>
@import "./style.css";
</style>
