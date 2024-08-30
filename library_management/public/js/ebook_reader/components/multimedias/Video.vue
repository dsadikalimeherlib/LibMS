<template>
    <div class="youtube-custom-player">
        <!-- YouTube Player Container -->
        <div id="youtube-player"></div>

        <!-- Custom Controls -->
        <div class="controls">
            <button @click="togglePlay">
                <div class="icon-wrapper">
                    <svg v-if="isPlaying" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                        fill="none">
                        <rect x="6" y="5" width="4" height="14" rx="1" stroke="#fff" stroke-width="2"
                            stroke-linecap="round" />
                        <rect x="14" y="5" width="4" height="14" rx="1" stroke="#fff" stroke-width="2"
                            stroke-linecap="round" />
                    </svg>
                    <svg v-else xmlns="http://www.w3.org/2000/svg" width="17" height="17" viewBox="0 0 17 17"
                        fill="none">
                        <path
                            d="M15.2111 7.60557L2.73666 1.36833C1.93878 0.969388 1 1.54958 1 2.44164V14.5584C1 15.4504 1.93878 16.0306 2.73666 15.6317L15.2111 9.39443C15.9482 9.0259 15.9482 7.9741 15.2111 7.60557Z"
                            stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                    </svg>
                </div>
            </button>
            <input class="range-slider" type="range" min="0" max="100" v-model="progress" @input="seekVideo" />
            <div class="volume-control">
                <label for="volume"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="25" viewBox="0 0 24 25"
                        fill="none">
                        <path
                            d="M4.15838 14.4306C3.44537 13.2423 3.44537 11.7577 4.15838 10.5694C4.37596 10.2067 4.73641 9.95272 5.1511 9.86978L6.84413 9.53117C6.94499 9.511 7.03591 9.45691 7.10176 9.37788L9.17085 6.89498C10.3534 5.47592 10.9447 4.76638 11.4723 4.95742C12 5.14846 12 6.07207 12 7.91928L12 17.0807C12 18.9279 12 19.8515 11.4723 20.0426C10.9447 20.2336 10.3534 19.5241 9.17085 18.105L7.10176 15.6221C7.03591 15.5431 6.94499 15.489 6.84413 15.4688L5.1511 15.1302C4.73641 15.0473 4.37596 14.7933 4.15838 14.4306Z"
                            fill="white" />
                        <path
                            d="M14.5355 8.96447C15.4684 9.89732 15.9948 11.1611 16 12.4803C16.0052 13.7996 15.4888 15.0674 14.5633 16.0076"
                            stroke="white" stroke-width="2" stroke-linecap="round" />
                    </svg></label>
                <input class="volume-range-slider " type="range" min="0" max="100" v-model="volume"
                    @input="changeVolume" />
            </div>

        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            player: null,
            isPlaying: false,
            progress: 0,
            volume: 100,
        };
    },
    mounted() {
        // Load the YouTube IFrame API
        const tag = document.createElement('script');
        tag.src = 'https://www.youtube.com/iframe_api';
        document.body.appendChild(tag);

        // Initialize YouTube player when the API is ready
        window.onYouTubeIframeAPIReady = () => {
            this.initYouTubePlayer();
        };
    },
    methods: {
        initYouTubePlayer() {
            this.player = new YT.Player('youtube-player', {
                height: '390',
                width: '640',
                videoId: '2u5jJT9xFd4', // Replace with your video ID
                playerVars: {
                    autoplay: 0,
                    controls: 0, // Disable default controls
                    modestbranding: 1,
                    rel: 0,
                    showinfo: 0,
                    disablekb: 1,
                    playsinline: 1
                },
                events: {
                    onReady: this.onPlayerReady,
                    onStateChange: this.onPlayerStateChange,
                },
            });
        },
        onPlayerReady(event) {
            // Set initial volume to max
            this.player.setVolume(this.volume);
        },
        onPlayerStateChange(event) {
            // Update play/pause state based on player status
            this.isPlaying = event.data === YT.PlayerState.PLAYING;
            if (this.isPlaying) {
                this.updateProgress();
            }
        },
        togglePlay() {
            if (this.isPlaying) {
                this.player.pauseVideo();
            } else {
                this.player.playVideo();
            }
        },
        updateProgress() {
            if (this.player && this.isPlaying) {
                const duration = this.player.getDuration();
                const currentTime = this.player.getCurrentTime();
                this.progress = (currentTime / duration) * 100;

                // Update progress periodically
                requestAnimationFrame(this.updateProgress);
            }
        },
        seekVideo() {
            if (this.player) {
                const duration = this.player.getDuration();
                const seekToTime = (this.progress / 100) * duration;
                this.player.seekTo(seekToTime, true);
            }
        },
        changeVolume() {
            if (this.player) {
                this.player.setVolume(this.volume);
            }
        },
    },
};
</script>
<style>
@import './Video.css'
</style>