    <template>
        <v-toolbar density="compact" flat>
            <template v-slot:prepend>
                <v-app-bar-nav-icon @click="$emit('toggle-toc')"></v-app-bar-nav-icon>
                <v-tooltip activator="parent" location="bottom">Table of Content</v-tooltip>
            </template>
            <v-spacer></v-spacer>
            <v-spacer></v-spacer>
            <v-toolbar-title>{{ title }}</v-toolbar-title>
            <v-spacer></v-spacer>

            <v-btn icon>
                <v-icon>mdi-crosshairs-gps</v-icon>
                <v-tooltip activator="parent" location="bottom">Theme</v-tooltip>
            </v-btn>

            <v-btn icon>
                <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>

            <v-btn icon @click="toggleFullscreen">
                <v-icon>{{ isfullScreen ? 'mdi-window-minimize' : 'mdi-window-maximize' }}</v-icon>
                <v-tooltip v-if="isfullScreen" activator="parent" location="bottom">Exit Full Screen</v-tooltip>
                <v-tooltip v-else-if="!isfullScreen" activator="parent" location="bottom">Go Full Screen</v-tooltip>
            </v-btn>
            <v-btn icon small @click="CloseReader">
                <v-icon>mdi-close</v-icon>
                <v-tooltip activator="parent" location="bottom">Close</v-tooltip>
            </v-btn>
        </v-toolbar>
    </template>


<script>

export default {
    name: 'PdfTitlebar',
    props: {
        title: {
            default: 'Libms',
            type: String,
        },
    },
    data() {
        return {
            isfullScreen: false,
        };
    },
    mounted() {
        document.addEventListener('fullscreenchange', this.handleFullscreenChange);
    },
    beforeUnmount() {
        document.removeEventListener('fullscreenchange', this.handleFullscreenChange);
    },
    methods: {
        CloseReader() {
            if (document.fullscreenElement) {
                document.exitFullscreen();
            }
            this.$emit('close-reader');
        },
        toggleFullscreen() {
            const reader_container = document.querySelector('.v-overlay-container');
            if (reader_container) {
                if (!document.fullscreenElement) {
                    reader_container.requestFullscreen().then(() => {
                        this.isfullScreen = true;
                    }).catch(err => {
                        console.error(`Error attempting to enable fullscreen mode: ${err.message} (${err.name})`);
                    });
                } else {
                    document.exitFullscreen().then(() => {
                        this.isfullScreen = false;
                    }).catch(err => {
                        console.error(`Error attempting to exit fullscreen mode: ${err.message} (${err.name})`);
                    });
                }
            }
        },
        handleFullscreenChange() {
            this.isFullscreen = !!document.fullscreenElement;
        },
    },
};
</script>

<style scoped>
.v-dialog--fullscreen {
    background-color: white;
}
</style>