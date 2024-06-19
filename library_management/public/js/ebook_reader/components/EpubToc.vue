<template>
    <v-col cols="2" v-if="isTocVisible" hover class="d-flex justify-start align-items-left">
        <v-navigation-drawer permanent class="deep-purple lighten-1 white--text" width="300">
            <v-list v-model:opened="showToc" :lines="false" density="compact" dense nav>
                <v-list-group value="Toc">
                    <template v-slot:activator="{ props }">
                        <v-list-item v-bind="props" title="Table of Content">
                            <template v-slot:prepend>
                                <v-btn icon="mdi-table-of-contents" size="large" variant="text"></v-btn>
                                <v-tooltip activator="parent" location="bottom">Content</v-tooltip>
                            </template>
                        </v-list-item>
                    </template>
                    <v-list-item v-for="(item, index) in toc" :key="item.id" @click="navigateToPage(item.href, index)"
                        link>
                        <v-list-item-title class="wrap-text">
                            <!-- {{ index + 1 }}. -->
                            <!-- {{ item.label }} -->

                            {{ index }} - {{ item.id }}
                        </v-list-item-title>
                    </v-list-item>
                </v-list-group>
            </v-list>
        </v-navigation-drawer>
    </v-col>
</template>

<script>
export default {
    name: 'EpubToc',
    props: {
        isTocVisible: {
            default: true,
            type: Boolean,
        },
        toc: {
            default: () => [],
            type: Array,
        },
    },
    data() {
        return {
            showToc: ["Toc"],
        };
    },
    methods: {
        navigateToPage(href, index) {
            this.$emit('render-page', (href, index));
        },
    },
}

</script>

<style scoped>
.wrap-text {
    white-space: normal;
    word-wrap: break-word;
    width: 100%;
}
</style>