(function($) {

    $(document).ready(function() {

      var trending = $('#posts').find('.flex-container');

      // $(trending).masonry({
      //   itemSelector: '.post',
      //   columnWidth: 280,
      //   gutter: 20
      // });

      var item = trending.find('.post');

      item.on('mouseover', function(){
        $(this).siblings().addClass('active');
      });
  
      item.on('mouseout', function(){
        item.removeClass('active');
      });

    });

})(jQuery);