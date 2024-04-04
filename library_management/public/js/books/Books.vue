<template>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-12 col-lg-12">
                <div class="card book-items-card">
                    <div class="card-header">
                        <div class="container">
                            <div class="row d-flex justify-content-between align-items-center">
                                <div class="col-6">
                                    <h4 class="card-title mb-0">Books</h4>
                                </div>
                                <!-- <div v-for="category in bookstore.item_categories" :key="category.name" class="filter-btn">
                                    <button @click="bookstore.get_items_by_category(category.name)" class="btn btn-sm btn-primary">{{ category.name }}</button>
                                </div> -->
                                <div class="col-6 p-0">
                                    <div class="input-group search-bar text-muted">
                                        <div class="w-100">
                                            <input @input="bookstore.search_books()" v-model="bookstore.search_book"
                                                id="navbar-search" type="text" class="form-control pl-5"
                                                placeholder="Search Books">
                                        </div>
                                        <span class="search-icon">
                                            <svg class="icon icon-sm">
                                                <use href="#icon-search"></use>
                                            </svg>
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="card-body book-items-card-body">
                        <div class="container p-0">
                            <div class="row">
                                <div v-for="item in bookstore.books" :key="item.title" class="col-12 col-md-6 col-lg-3 mb-3">
                                    <div class="card" style="height: 300px;">
                                        <img class="card-img-top book-img" 
                                            :src="item.image ? item.image : 'https://placehold.co/150?text=Item'" alt="Card image cap">
                                        <div class="card-body mt-0" style="overflow: hidden; text-overflow: ellipsis;">
                                            <h4 class="card-title mt-0 d-sm-inline-flex">{{ item.title }}</h4>
                                            <h6 class="card-text ml-0 mb-3">By: {{ item.author }}</h6>
                                            <h6 class="card-text ml-0 mb-3">subjects: {{ item.subject }}</h6>
                                        </div>
                                        <!-- <button @click="bookstore.add_item(item)" class="btn btn-primary" type="button">Add</button> -->
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script setup>
import { onMounted } from 'vue';
import { useBooksStore } from './store';
let bookstore = useBooksStore();

onMounted(() => {
    bookstore.get_books();
})
</script>


<style lang="scss" scoped>
.book-items-card {
    height: calc(100vh - 150px);
}

.book-items-card-body {
    overflow: auto;
}

.book-img {
    height: 200px;
    width: auto;
    object-fit: contain;
}

.card-header {
    background-color: white;
}

@media only screen and (max-width: 768px) {

    .book-items-card {
        height: calc(50vh);
    }

}
</style>
