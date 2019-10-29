(function($) {

  $(document).ready(function() {

    var trending = $('#posts').find('.flex-container');


    var item = trending.find('.post');

    item.on('mouseover', function(){
      $(this).siblings().addClass('active');
    });

    item.on('mouseout', function(){
      item.removeClass('active');
    });

    var product = $('.slider-product').find('.slider');

    if(product.length){
      Slider(product, {
        sliderHeight: Slider.prototype.HEIGHT_CURRENT,
        loop: false,
        itemsPerSlide: function() {
          if ($.winWidth() >= 1024)  {
              return 4
          } else if($.winWidth() >= 768) {
              return 3
          } else if ($.winWidth() >= 600){
            return 2
          }else{
            return 1
          }
      }
    }).attachPlugins([
        SliderSideAnimation({
            margin: 20
        }),
        SliderSideShortestAnimation({
            margin: 20
        }),
        SliderFadeAnimation(),
        SliderControlsPlugin({
            animationName: 'side-shortest'
        }),
        SliderNavigationPlugin({
            animationName: 'side'
        }),
        SliderDragPlugin({
            margin: 20
        })
    ]);
    }


  });

})(jQuery);