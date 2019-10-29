(function($){

    $(document).ready(function() {


        var $contentBlock = $('#content'),
            contentHeight = $contentBlock.outerHeight(),
            viewPortHeight = $.winHeight(),
            contentBlockanchorPoint = contentHeight * .15;

        function showHideBackToTopBtn(isAnchorPassed, isBottomBorderPassed) {
            var $btn = $('#scroll-top-btn'),
                $btnBox = $('#back-btn-box');

            if (!$btnBox.length) return false;


            console.log(isBottomBorderPassed);

            if (  isAnchorPassed && $btnBox.hasClass("js-active") && !isBottomBorderPassed ) return false;


            if ( isAnchorPassed && !$btnBox.hasClass("js-active") && !isBottomBorderPassed ) {

                $btnBox.addClass("js-active");

                $btnBox.on("click.back", function () {

                   $("html, body").animate({
                       scrollTop: 0,
                   }, 450, 'swing');

                });

            } else {

                $btnBox.removeClass("js-active");
                $btnBox.off("click.back");
            }
        }

        $(window).scroll($.rared(function() {
            var scrollFromTopOfTheBlock = (0 - $contentBlock.get(0).getBoundingClientRect().y),
                footerTopOffset = $('#footer-wrapper').get(0).getBoundingClientRect().top;

            var anchorPassed = ( scrollFromTopOfTheBlock > 0 &&
                                 scrollFromTopOfTheBlock > contentBlockanchorPoint );

            var bottomAnchorPassed = ( viewPortHeight - footerTopOffset ) > 0;


            showHideBackToTopBtn(anchorPassed, bottomAnchorPassed);

        }, 200));


    });

})(jQuery);