<template>
    <div class="icons-wrapper sort">
        <span v-if="filterApplied" class="selected-circle" />
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
        <div v-if="showSortPopup" class="sort-filter-popup filter-popup">
            <div class="title-wrapper">
                <div class="title">Filters</div>
                <div class="right">
                    <div class="clear" @click="clearFilters">Clear All</div>
                    <div @click="setShowSortPopup(false)" class="close-icon"><svg xmlns="http://www.w3.org/2000/svg"
                            width="24" height="24" viewBox="0 0 24 24" fill="none">
                            <path d="M18 6L6 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M6 6L18 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                        </svg></div>
                </div>
            </div>
            <div class="sort-filter-column-wrapper filter">
                <div class="column">
                    <!-- <div class="item">
                        <div class="label">Title</div>
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
                    </div> -->

                    <div class="item">
                        <div class="label">Category</div>
                        <div class="field">
                            <select v-model="category" @change="setCategory">
                                <option value="">Select Category</option>
                                <template v-for="category in store.media_categories" :key="category">
                                    <option :value="category.category">{{ category.category }}</option>
                                </template>
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
                        <div class="label">Multimedia Type</div>
                        <div class="field">
                            <select v-model="media_type" @change="setMedia_type">
                                <option value="">Select Type</option>
                                <template v-for="type in types" :key="type">
                                    <option :value="type">{{ type }}</option>
                                </template>
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

                    <div class="item">
                        <div class="label">Publication Year</div>
                        <div class="field">
                            <select v-model="publication_year" @change="setpublication_year">
                                <option value="">Select Publication Year</option>
                                <template v-for="publication_year in publication_years" :key="publication_year">
                                    <option :value="publication_year">{{ publication_year }}</option>
                                </template>
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
            </div>
            <div class="button-wrapper">
                <div @click="handleFilterChange" class="button">Apply</div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useBooksStore } from '../../../../books/store';
const store = useBooksStore();

onMounted(() => {
    store.get_mulitmedia_category({ length: null });

});
// const titles = ['Book1', 'Book3', 'Book5', 'Book6', 'Breaking The Mould']
const publication_years = ['2001', '2002', '2003', '2004', '2005',]
const types = ['Video', 'Audio']
</script>
<script>
export default {
    props: {
        setFilters: {
            type: Function,
            required: true
        },
    },
    data() {
        return {
            showSortPopup: false,
            category: '',
            publication_year: '',
            filterApplied: false,
            media_type: ''
        };
    },
    methods: {
        setShowSortPopup(value) {
            this.showSortPopup = value
        },
        setCategory(event) {
            this.category = event.target.value
        },
        setpublication_year(event) {
            this.publication_year = event.target.value
        },
        setMedia_type(event) {
            this.media_type = event.target.value
        },
        handleFilterChange({ length = null, category = null, publication_year = null, media_type = null }) {
            if (this.setFilters) {
                this.setFilters({ length: length !== null ? length : this.length, category: category !== null ? category : this.category, publication_year: publication_year !== null ? publication_year : this.publication_year, media_type: media_type !== null ? media_type : this.media_type })
                this.setShowSortPopup(false)
                this.checkfilterApplied()
            }
        },
        checkfilterApplied() {
            if (this.category == '' && this.publication_year == '') {
                this.filterApplied = false
            } else {
                this.filterApplied = true
            }
        },
        clearFilters() {
            this.category = ""
            this.publication_year = ""
            this.handleFilterChange({ length: "", category: "", publication_year: "" })
            this.setShowSortPopup(false)
            this.filterApplied = false
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