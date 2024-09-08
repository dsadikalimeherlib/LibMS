<template>
    <div class="holiday-page">
        <div class="holiday-container">
            <div class="title-wrapper">
                <h1>Holiday List</h1>
                <div class="year-dropdown">
                    <select @change="setYear">
                        <template v-for="years in years" :key="years">
                            <option :value="years">{{ years }}</option>
                        </template>
                    </select>
                    <svg class="drpodown-arrow" xmlns="http://www.w3.org/2000/svg" width="12" height="7"
                        viewBox="0 0 12 7" fill="none">
                        <path
                            d="M10 2L6.22154 4.93122C6.16061 4.97551 6.08174 5 6 5C5.91826 5 5.83939 4.97551 5.77846 4.93122L2 2"
                            stroke="#545353" stroke-width="2.31353" stroke-linecap="round" stroke-linejoin="round" />
                    </svg>
                </div>
            </div>
            <div class="holiday-list-wrapper">
                <template v-for="month in holidays" :key="month.month">
                    <div class="month-box">
                        <div class="month-title"><span>{{ month.month }}</span></div>
                        <div class="holiday-list">
                            <template v-for="holiday in month.holidays" :key="holiday.date">
                                <div class="holiday-item">
                                    <div class="date-day">
                                        <div class="date">{{ holiday.holiday_date.date }}</div>
                                        <div class="day">{{ holiday.holiday_date.day }}</div>
                                    </div>
                                    <div class="holiday">{{ holiday.holiday_name }}</div>
                                </div>
                            </template>
                        </div>
                    </div>
                </template>
            </div>
        </div>
    </div>
</template>
<script setup>
import { onMounted } from 'vue';
import { useBooksStore } from '../../../books/store';

const bookStore = useBooksStore();
function getYearStartAndEndDates(year) {
    // Start date: January 1st of the given year at 00:00:00
    const startDate = new Date(year, 0, 1); // Month is 0-based, so 0 represents January

    // End date: December 31st of the given year at 23:59:00
    const endDate = new Date(year, 11, 31, 23, 59, 0); // Month is 0-based, so 11 represents December

    return {
        startDate,
        endDate
    };
}
const { startDate, endDate } = getYearStartAndEndDates(2024);
onMounted(() => {

    bookStore.get_holidays({ from_date: startDate, to_date: endDate });
});
const setYear = (event) => {
    const { startDate, endDate } = getYearStartAndEndDates(event.target.value);
    bookStore.get_holidays({ from_date: startDate, to_date: endDate });
};
const holidays =
    [
        {
            month: 'january',
            holidays: [
                {
                    holiday_date: { date: '01', day: 'Mon' },
                    holiday_name: 'Hii'
                },
                {
                    holiday_date: { date: '01', day: 'Mon' },
                    holiday_name: 'hii'
                }
            ]
        },
        {
            month: 'february',
            holidays: [
                {
                    holiday_date: { date: '01', day: 'Mon' },
                    holiday_name: '00'
                },
                {
                    holiday_date: { date: '01', day: 'Mon' },
                    holiday_name: 'sdf'
                }
            ]
        }, {
            month: 'january',
            holidays: [
                {
                    holiday_date: { date: '01', day: 'Mon' },
                    holiday_name: 'Hii'
                },
                {
                    holiday_date: { date: '01', day: 'Mon' },
                    holiday_name: 'hii'
                }
            ]
        },
        {
            month: 'february',
            holidays: [
                {
                    holiday_date: { date: '01', day: 'Mon' },
                    holiday_name: '00'
                },
                {
                    holiday_date: { date: '01', day: 'Mon' },
                    holiday_name: 'sdf'
                }
            ]
        }
    ]
const years = ['2024', '2023']
</script>
<style>
@import './holiday.css'
</style>