(function($) {

    $(document).ready(function() {
        $('.country').on('click', function(e) {
            e.preventDefault();
            var anchor = event.target.closest("a");
            var popup = $.popup({
                classes: 'contact-popup contact-form-popup',
                content: '<div class="popup-custom"> <div class="popup-title title-italic-h3" style="max-width: 538px;  line-height: 1.17;">You will now be redirected to our ' + e.target.innerHTML + ' site</div> <div> <div class="btn medium blue moema close-popup" "style="margin-right:15px;">go back</div>  <a href=" '+ anchor.getAttribute('href') + ' " class="btn medium blue moema" ">continue</a> </div> </div>'
            }).show();
        });

    });

})(jQuery);