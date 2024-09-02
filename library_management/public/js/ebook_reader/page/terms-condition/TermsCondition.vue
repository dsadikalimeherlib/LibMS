<template>
    <div class="terms-condition-page">
        <div class="container">
            <div class="title-wrapper">
                <h1>Terms and Conditions</h1>
                <div class="dropdown-wrapper">
                    <select>
                        <option>English</option>
                        <option>Gujarati</option>
                    </select>
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="6" viewBox="0 0 12 6" fill="none">
                        <path
                            d="M10 1.5L6.22154 4.43122C6.16061 4.47551 6.08174 4.5 6 4.5C5.91826 4.5 5.83939 4.47551 5.77846 4.43122L2 1.5"
                            stroke="#545353" stroke-width="2.31353" stroke-linecap="round" stroke-linejoin="round" />
                    </svg>
                </div>
            </div>
            <div class="accordion">
                <!-- Iterate over the accordion items -->

                <div v-for="(item, index) in items" :key="index" class="accordion-item">
                    <!-- Accordion Header -->
                    <div class="accordion-header" @click="toggle(index)">
                        {{ item.title }}
                        <svg v-if="activeIndex === index" xmlns="http://www.w3.org/2000/svg" width="19" height="19"
                            viewBox="0 0 19 19" fill="none">
                            <circle cx="9.5" cy="9.5" r="9.5" fill="#EEEEF1" />
                            <path d="M15 9L4 9" stroke="#33363F" />
                        </svg>
                        <svg v-else xmlns="http://www.w3.org/2000/svg" width="19" height="19" viewBox="0 0 19 19"
                            fill="none">
                            <circle cx="9.5" cy="9.5" r="9.5" fill="#EEEEF1" />
                            <path d="M15 9L4 9" stroke="#33363F" />
                            <line x1="9.5" y1="4" x2="9.5" y2="15" stroke="#33363F" />
                        </svg>
                    </div>

                    <!-- Accordion Content -->
                    <div class="accordion-content" v-show="activeIndex === index">
                        {{ item.content }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            activeIndex: 0, // Tracks the currently active accordion item
            items: [
                {
                    title: 'General Conditions', content: `The members can use the library for the purpose of study and research. In addition, those who are not the members, can also use the library adhering to the institution s policy.
The CCTVs are installed in the library premises.We regret the inconvenience caused to your privacy but the CCTVs are required for security reasons.
The applicant needs to fill in all the required details to become the member of the library. (For more information, please see the membership details discussed below.)
Kindly deposit your luggage in the locker and obtain the token.
The purpose of Meher Library & Jafari Seminary is to help gain knowledge.It is a private institution and retains the right to revoke the membership and also the permission to enter and use the estate if they engage in criminal behaviour and breach of the rules and procedures of the institution.` },
                { title: 'Item 2', content: 'Content for item 2' },
                { title: 'Item 3', content: 'Content for item 3' },
            ],
        };
    },
    methods: {
        toggle(index) {
            // Toggle the active index
            this.activeIndex = this.activeIndex === index ? null : index;
        },
    },
};
</script>
<style scoped>
@import './style.css'
</style>