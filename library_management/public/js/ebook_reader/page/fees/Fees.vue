<template>
    <div class="fees-page">
        <div class="fees-container">
            <h1>Fees</h1>
            <div class="subtitle">Detailed Fees Structure</div>
            <div class="fees-list-wrapper-section">
                <div class="fees-list-wrapper">
                    <div class="fees-list-title">Borrow Book</div>
                    <div class="fees-list borrow-book-list">
                        <template v-for="item in fees.borrowBook" :key="item.fees">
                            <div class="fee-item borrow-book">
                                <div class="price">₹ {{ item.fees }}/-</div>
                                <div class="benefit-list">
                                    <template v-for="benefitItem in item.benefits" :key="benefitItem">
                                        <div class="benefit"><svg width="20" height="21" viewBox="0 0 20 21" fill="none"
                                                xmlns="http://www.w3.org/2000/svg">
                                                <rect y="0.798584" width="20" height="20" rx="10" fill="#00B0AB" />
                                                <path
                                                    d="M4.5 11.6529L5.4717 10.6508L7.93875 13.1943L14.5283 6.39856L15.5 7.40067L7.93806 15.1986L4.5 11.6529Z"
                                                    fill="white" />
                                            </svg>
                                            {{ benefitItem }}</div>
                                    </template>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>
                <div class="fees-list-wrapper-columns">
                    <div class="fees-list-wrapper">
                        <div class="fees-list-title">Reading Area</div>
                        <div class="fees-list">
                            <div class="fee-item">
                                <div class="price">₹ {{ fees.readingArea.fees }}/-</div>
                                <div class="benefit-list">
                                    <template v-for="benefitItem in fees.readingArea.benefits" :key="benefitItem">
                                        <div class="benefit"><svg width="20" height="21" viewBox="0 0 20 21" fill="none"
                                                xmlns="http://www.w3.org/2000/svg">
                                                <rect y="0.798584" width="20" height="20" rx="10" fill="#00B0AB" />
                                                <path
                                                    d="M4.5 11.6529L5.4717 10.6508L7.93875 13.1943L14.5283 6.39856L15.5 7.40067L7.93806 15.1986L4.5 11.6529Z"
                                                    fill="white" />
                                            </svg>
                                            {{ benefitItem }}</div>
                                    </template>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="fees-list-wrapper">
                        <div class="fees-list-title">Research Desk</div>
                        <div class="fees-list">
                            <div class="fee-item">
                                <div class="price">₹ {{ fees.researchDesk.fees }}/-</div>
                                <div class="benefit-list">
                                    <template v-for="benefitItem in fees.researchDesk.benefits" :key="benefitItem">
                                        <div class="benefit"><svg width="20" height="21" viewBox="0 0 20 21" fill="none"
                                                xmlns="http://www.w3.org/2000/svg">
                                                <rect y="0.798584" width="20" height="20" rx="10" fill="#00B0AB" />
                                                <path
                                                    d="M4.5 11.6529L5.4717 10.6508L7.93875 13.1943L14.5283 6.39856L15.5 7.40067L7.93806 15.1986L4.5 11.6529Z"
                                                    fill="white" />
                                            </svg>
                                            {{ benefitItem }}</div>
                                    </template>
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
const fees = {
    borrowBook: [
        {
            fees: 1200,
            benefits: ['6 Months', 'Borrow up to 4 books a time']
        },
        {
            fees: 2400,
            benefits: ['1 year', 'Borrow up to 4 books a time']
        },
        {
            fees: 12000,
            benefits: ['5 years', 'Borrow up to 4 books a time', 'The applicant can appoint one nominee from his family.']
        }
    ],
    readingArea: {
        fees: 800,
        benefits: ['6 Months']
    },
    researchDesk: {
        fees: 2000,
        benefits: ['1 Month']
    }
}
</script>

<style>
@import './fees.css'
</style>