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
                    <div @click="clearFilters" class="clear">Clear All</div>
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
                            <select v-model="book_title" @change="setBookTitle">
                                <option value="">Select Book title</option>
                                <template v-for="book_title in book_titles" :key="book_title">
                                    <option :value="book_title">{{ book_title }}</option>
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
                        <div class="label">Author</div>
                        <div class="field">
                            <select v-model="author" @change="setAuthor">
                                <option value="">Select Author</option>
                                <template v-for="author in authors" :key="author">
                                    <option :value="author">{{ author }}</option>
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
                        <div class="label">Language</div>
                        <div class="field">

                            <select v-model="language" @change="setLanguage">
                                <option value="">Select Language</option>
                                <template v-for="language in languages" :key="language.label">
                                    <option :value="language.value">{{ language.label }}</option>
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
                        <div class="label">Subject</div>
                        <div class="field">
                            <select v-model="subject" @change="setSubject">
                                <option value="">Select Subject</option>
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
                    <div class="item">
                        <div class="label">Publication</div>
                        <div class="field">
                            <select v-model="publication" @change="setPublication">
                                <option value="">Select Publication</option>
                                <template v-for="publication in publications" :key="publication">
                                    <option :value="publication">{{ publication }}</option>
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
                    <div class="item">
                        <div class="label">Category</div>
                        <div class="field">

                            <select v-model="category" @change="setCategory">
                                <option value="">Select Category</option>
                                <template v-for="category in categories" :key="category">
                                    <option :value="category">{{ category }}</option>
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
                        <div class="label">Book Type</div>
                        <div class="radio-fields">
                            <label>
                                <div class="radio-input-wrapper"><input name="book-type" checked type="radio" /><span
                                        class="radio" />
                                </div>
                                <div class="radio-label">All</div>
                            </label>
                            <label>
                                <div class="radio-input-wrapper"><input name="book-type" type="radio" /><span
                                        class="radio" />
                                </div>
                                <div class="radio-label">Religious</div>
                            </label>
                            <label>
                                <div class="radio-input-wrapper"><input name="book-type" type="radio" /><span
                                        class="radio" />
                                </div>
                                <div class="radio-label">Academic</div>
                            </label>
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
import BookFilterItem from './BookFilterItem.vue';
import { useBooksStore } from '../../../../books/store';
import { onMounted } from 'vue';
const bookStore = useBooksStore();
// onMounted(() => {

//     bookStore.get_languages();
// });
// console.log('bookStore', bookStore);

const languageList = [{
    code: 'gu',
    language: 'Gujarati'
},
{
    code: 'en',
    language: 'English'
},
{
    code: 'ar',
    language: 'Arabic'
},
]
const languages = languageList.map(item => ({
    label: item.language,
    value: item.code
}));
const book_titles = ['Book1', 'Book3', 'Book5', 'Book6', 'Breaking The Mould']
const authors = ['Test Author', 'Aasif Sheikh', 'Mohammad Faris']
const publications = ['Test Publication', 'Meher Library and Jafri Seminary', 'Aazaman Firang Wa Irtabatati Islami', 'Lion Publications']
const publication_years = ['2001', '2002', '2003', '2004', '2005',]
const categories = ['Normal Book', 'E-Book', 'Tafsheer']

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
            book_title: '',
            length: 18,
            author: '',
            category: '',
            language: '',
            publication: '',
            publication_year: '',
            subject: '',
            showSortPopup: false,
            bookType: '',
            filterApplied: false
        };
    },
    methods: {
        checkfilterApplied() {
            if (this.book_title == '' && this.author == '' && this.category == '' && this.language == '' && this.publication == '' && this.publication_year == '' && this.subject == '' && this.bookType == '') {
                this.filterApplied = false
            } else {
                this.filterApplied = true
            }
        },
        setShowSortPopup(value) {
            this.showSortPopup = value
        },
        handleFilterChange() {
            if (this.setFilters) {
                this.setFilters({ length: this.length, author: this.author, category: this.category, publication_year: this.publication_year, publication: this.publication, book_title: this.book_title, language: this.language, subject: this.subject })
                this.setShowSortPopup(false)
                this.checkfilterApplied()
            }
        },
        setBookTitle(event) {
            this.book_title = event.target.value
        },
        setSubject(event) {
            this.subject = event.target.value
        },
        setLength(event) {
            this.length = event.target.value
        },
        setAuthor(event) {
            this.author = event.target.value
        },
        setCategory(event) {
            this.category = event.target.value
        },
        setPublication(event) {
            this.publication = event.target.value
        },
        setpublication_year(event) {
            this.publication_year = event.target.value
        },
        setLanguage(event) {
            this.language = event.target.value
        },
        setBookType() {
            this.bookType = value
        },

        clearFilters() {
            this.book_title = ""
            this.subject = ""
            this.author = ""
            this.category = ""
            this.publication = ""
            this.publication_year = ""
            this.language = ""
            this.bookType = ""
            this.handleFilterChange({ length: 18, author: '', category: '' })
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