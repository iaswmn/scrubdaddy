(function ($) {

    $(document).ready(function () {

        var container = $('.history-navigation');
        var btn = container.find('.year');
        if (btn.length) {
            btn.on('click', function (event) {
                var target = $($(this).attr('href'));
                if (target.length) {
                    event.preventDefault();
                    $("html, body").animate({
                        scrollTop: target.offset().top
                    }, 600);
                }
            });
        }






        $('.hint-marker').aboutHints();


        var slider = $('.history-container');
        var history = $('.history'),
            lastItem = slider.find('.item').last().get(0);


        $(window).on('load', function () {
            var item = slider.find('.item');



            $(this).on('scroll', $.rared( function () {

                var position = history.offset().top - $(this).scrollTop(),
                    bottomPointPassed = lastItem.getBoundingClientRect().top < Math.round(lastItem.getBoundingClientRect().height * 0.3);


                if (  bottomPointPassed || position > 0 ) {
                    container.removeClass('active');
                } else {
                    container.addClass('active');
                }



                if (item.length) {

                    for (var i = 0; i < item.length; i++) {

                        var pos = item.eq(i).offset().top - $(this).scrollTop();
                        var height = item.eq(i).height() / 2;

                        if (pos <= height) {

                            btn.eq(i).addClass('active');
                            btn.eq(i-1).removeClass('active');

                        } else {
                            btn.eq(i).removeClass('active');
                        }
                    }

                }
            }, 200));

        });

    });

})(jQuery);