<!-- template for the slider component -->
<template type="text/x-template" id="img-slider-template">


    <!-- demo root element -->
    <div id="demo">
        <img-slider>
            <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/5689/rock.jpg">
            <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/5689/grooves.jpg">
            <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/5689/arch.jpg">
            <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/5689/sunset.jpg">
        </img-slider>
    </div>

    <p>
        Vue.js implements WebComponent-compliant &lt;content&gt; insertion point mechanism.
    </p>
    <p>
        Markup and CSS borrowed from <a href="http://css-tricks.com/modular-future-web-components/" target="_blank">CSS
            Tricks</a>, which is in turn adapted from <a href="http://csscience.com/responsiveslidercss3/"
            target="_blank">CSScience</a>. Images courtesy of <a href="http://www.flickr.com/photos/eliya"
            target="_blank">Eliya Selhub</a>
    </p>
</template>
<script>
// // define slider component
// Vue.component('img-slider', {
//     template: '#img-slider-template',
//     replace: true
// })
// // boot up demo
// new Vue({
//     el: '#demo'
// })
</script>