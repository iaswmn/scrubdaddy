(function ($) {

    $(document).ready(function () {

        if ( $.winWidth() <= 600 ) {

            Slider('#blog-slider', {
                sliderHeight: Slider.prototype.HEIGHT_CURRENT,
                loop: true,
                itemsPerSlide: 1,
                blogPostsSlider: true
            }).attachPlugins([
                SliderSideAnimation({
                    margin: 20
                }),
                SliderSideShortestAnimation({
                    margin: 20
                }),
                SliderFadeAnimation(),
                SliderNavigationPlugin({
                    animationName: 'side'
                }),
                SliderDragPlugin({
                    margin: 20
                }),
                SliderAutoscrollPlugin({
                    animationName: 'fade',
                    direction: 'random',
                    interval: 6000
                })
            ]);

        } else {

            var $trending = $('.trending').find('.flex-container'),
                $item = $trending.find('.item');

            $item.hover(function() {
                $(this).siblings().addClass('active');
                $(this).addClass('link');
            }, function() {
                $item.removeClass('active');
                $(this).removeClass('link');
            })
        }



    });

})(jQuery);