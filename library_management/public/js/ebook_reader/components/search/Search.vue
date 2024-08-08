<template>
    <div class="search-wrapper">
        <div class="search-input-wrapper">
            <img class="icon" src="/files/search-icon.svg" />
            <input placeholder="Looking for specific book? Enter Book Title here.." />
            <div class="close-btn">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M18 6L6 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M6 6L18 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
            </div>
        </div>
        <div class="search-dropdown">
            <ul class="tab-wrapper">
                <li class="active">All<span>14</span></li>
                <li>Books<span>8</span></li>
                <li>Magazines<span>8</span></li>
                <li>E-books<span>8</span></li>
                <li>Video<span>8</span></li>
                <li>Audio<span>8</span></li>
            </ul>
            <ul class="results">
                <li>
                    <div class="result-title">The Keys of understanding <span>qur</span>an</div>
                    <div class="category">Book</div>
                </li>
                <li>
                    <div class="result-title">The Keys of understanding quran</div>
                    <div class="category">Book</div>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
@import "./style.css";
</style>
