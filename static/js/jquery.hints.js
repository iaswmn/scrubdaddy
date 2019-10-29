(function( $ ) {

    $.fn.aboutHints = function() {


        this.each(function() {

            var hidden = true,
                $element = $(this),
                $innerWrapper = $element.find('.hint-inner-wrapper'),
                height = $innerWrapper.outerHeight(),
                position = $element.data('position'),
                width = $innerWrapper.outerWidth();


            var init = function() {


                $.winWidth() >= 1360 ? wideScreensHintPosition() : smallScreensHintPosition();


                clickHandler();

            };

            var wideScreensHintPosition = function () {
                $innerWrapper.css({
                    left: ( 0 - ( width ) / 2 ) + 20,
                    top: 0 - ( height + 24 )
                });
            };

            var smallScreensHintPosition = function () {
                $innerWrapper.css({
                    top: 0 - ( height + 2 )
                });

                if ( position === 'top-center' || position === 'top-center' || position === 'bottom-center' ) {

                    $innerWrapper.css({
                        left: ( 0 - ( width ) / 2 ) + 20
                    });

                } else if ( position === 'right' || position === 'top-right' || position === 'bottom-right' ) {

                    $innerWrapper.css({
                        right: 0
                    });

                }
            };

            var hideHint = function () {
                $innerWrapper.removeClass('js active-marker').find('.hint-text').removeAttr('style');

                return hidden = true;
            };

            var showHint = function() {
                $innerWrapper.addClass('js active-marker');

                $element.css({'z-index': 2});

                $innerWrapper.find('.hint-text').css({'opacity': 1});

                return hidden = false;
            };

            var clickHandler = function() {

                $element.on('click.Hint', function() {
                    hidden ? showHint() : hideHint();
                });

            };



            return init();
        });



        return this;
    };

}( jQuery ));