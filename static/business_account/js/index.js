(function ($) {

    /** @namespace window.js_storage.ajax_business */


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

        $("#id_date_of_commencement").datepicker();

        var form = $('#business-form');
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

        // function sendData ($form) {
        //
        //     if ($form.hasClass('sending')) {
        //         return false;
        //     }
        //
        //     var data = $form.serializeArray();
        //     data.push({
        //         name: 'referer',
        //         value: location.href
        //     });
        //
        //     $.ajax({
        //         url: window.js_storage.ajax_business,
        //         type: 'post',
        //         data: data,
        //         dataType: 'json',
        //         beforeSend: function() {
        //             $.preloader();
        //             $form.addClass('sending');
        //             $form.find('.invalid').removeClass('invalid');
        //         },
        //         success: function (response) {
        //
        //             if (response.success_message){
        //                 $.preloader().hide();
        //
        //                 $.popup({
        //                     classes: 'contact-popup contact-success-popup',
        //                     content: response.success_message
        //                 }).show();
        //
        //                 $form.get(0).reset();
        //             }
        //
        //         },
        //         error: $.parseError(function(response){
        //
        //             $.preloader().hide();
        //
        //             if (response && response.errors) {
        //
        //                 response.errors.forEach(function(record) {
        //                     var $field = $form.find('.' + record.fullname);
        //                     if ($field.length) {
        //                         $field.addClass(record.class);
        //                     }
        //                 });
        //
        //             } else {
        //                 alert(window.DEFAULT_AJAX_ERROR);
        //             }
        //         })
        //     });
        //
        // }


    });

})(jQuery);