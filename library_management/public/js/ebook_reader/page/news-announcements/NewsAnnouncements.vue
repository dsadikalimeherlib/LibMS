<template>
    <div class="news-announcement-page">
        <div class="news-announcement-container">
            <h1>News and Announcements</h1>
            <div class="feature-news-section">
                <div class="feature-news-title">Lorem ipsum dolor sit amet</div>
                <div class="feature-news-description">Consectetur adipiscing elit, sed do eiusmod tempor incididunt
                    utlabore et dolore magna aliqua.</div>
                <div class="feature-news-date">6 Jun 2010</div>
            </div>
            <div class="news-list">
                <template v-for="newsItem in news" :key="newsItem.title">
                    <div class="news-item">
                        <div class="news-title">{{ newsItem.title }}</div>
                        <div class="news-description">{{ newsItem.description }}</div>
                        <div class="news-date">{{ newsItem.date }}</div>
                    </div>
                </template>
            </div>
        </div>
    </div>
</template>

<script setup>
const news = [{
    title: 'Lorem ipsum dolor sit amet',
    description: 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua.',
    date: '6 Jun 2010'
},
{
    title: 'Lorem ipsum dolor sit amet',
    description: 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua.',
    date: '6 Jun 2010'
},
{
    title: 'Lorem ipsum dolor sit amet',
    description: 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua.',
    date: '6 Jun 2010'
},
{
    title: 'Lorem ipsum dolor sit amet',
    description: 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua.',
    date: '6 Jun 2010'
},
{
    title: 'Lorem ipsum dolor sit amet',
    description: 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua.',
    date: '6 Jun 2010'
},
{
    title: 'Lorem ipsum dolor sit amet',
    description: 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua.',
    date: '6 Jun 2010'
},
{
    title: 'Lorem ipsum dolor sit amet',
    description: 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua.',
    date: '6 Jun 2010'
}]
</script>

<style>
@import './news-announcement.css'
</style>