(function ($) {

    $(document).ready(function () {

        var sign = $("#signature");

        sign.jSignature({
            width: '260px',
            height: '160px',
            lineWidth: 0,
            color: '#154cc5',
            'background-color': 'transparent',
            'decor-color': 'transparent',
            'signatureLine': false,
            'getData': 'image'
        });


        var form = $('#employment_opportunities-form');
        var button = form.find('button');
        var reset = form.find('.reset');

        reset.on('click', function () {
            sign.jSignature("reset")
        });

        button.on('click', function(e){
            e.preventDefault();
            var file = sign.jSignature("getData", "image");

            sign.jSignature('getData', 'native').length ? $('#id_signature').val(file[1]) : null;
            form.submit();
        });



        $('.field-resume').find('.control').append('<div class="btn small blue">SELECT A FILE</div>');
        $( "#id_date_available" ).datepicker();
        $( "#id_user_date" ).datepicker();

        $("#id_education").selectmenu({
            classes: {
                'ui-selectmenu-button': 'custom-select-button',
                'ui-selectmenu-menu': 'custom-select-menu'
            }
        });

    });

})(jQuery);
