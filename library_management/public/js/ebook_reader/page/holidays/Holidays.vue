<template>
    <div class="holiday-page">
        <div class="holiday-container">
            <div class="title-wrapper">
                <h1>Holiday List</h1>
                <div class="year-dropdown">
                    <select>
                        <option>2024</option>
                        <option>2023</option>
                    </select>
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="7" viewBox="0 0 12 7" fill="none">
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
</script>
<style>
@import './holiday.css'
</style>