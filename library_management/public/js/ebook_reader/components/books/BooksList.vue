<template>
    <div class="book-table-wrapper">
        <table>
            <tr class="t-header-row">
                <th>Image</th>
                <th>Title</th>
                <th>Author</th>
                <th>Language</th>
                <th>Book type</th>
                <th>Sec</th>
                <th>Available</th>
            </tr>
            <template v-for="item in books" :key="item.book_title">
                <tr>
                    <td class="image-wrapper"><img :src="item.image ? item.image
                        : 'https://placehold.co/150?text=Item'" />
                    </td>
                    <td>
                        <h2>{{ item.book_title }}</h2>
                    </td>
                    <td>{{ item.author
                        }}</td>
                    <td>Gujarati</td>
                    <td>E-Book</td>
                    <td>Shia</td>
                    <td><span class="availability yes">Yes</span></td>
                </tr>
            </template>
        </table>
    </div>
</template>

<script>
export default {
    props: {
        books: {
            type: Array,
            required: true
        },
    },
}
</script>
<style scoped>
@import "./booksList.css";
</style>
