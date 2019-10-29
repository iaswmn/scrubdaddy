$('.btn').one('click', function () {
  var $this = $(this);
  var link = $this.attr('link');
  $.ajax({
    url: link,
    type: 'get',
    success: function (response) {
      console.log(response)
      if (response.success_message) {
        // сообщение о успешной отправке
        var $container = $(document).find('.smiling_scrubbers');
        $container.append(response.success_message)
        // $.popup({
        //   classes: 'contact-popup contact-success-popup',
        //   content: response.success_message
        // }).show();
      }
    },
  })
  // var $form = $(this);
  // if ($form.hasClass('sending')) {
  //     return false;
  // }

  // // добавление адреса страницы, откуда отправлена форма
  // var data = $(this).serializeArray();
  // data.push({
  //     name: 'referer',
  //     value: location.href
  // });

  // $.ajax({
  //     url: window.js_storage.ajax_contact,
  //     type: 'post',
  //     data: data,
  //     dataType: 'json',
  //     beforeSend: function() {
  //         $.popup.showPreloader();
  //         $form.addClass('sending');
  //         $form.find('.invalid').removeClass('invalid');
  //     },
  //     success: function(response) {
  //         if (response.success_message) {
  //             // сообщение о успешной отправке
  //             $.popup({
  //                 classes: 'contact-popup contact-success-popup',
  //                 content: response.success_message
  //             }).show();
  //         }
  //     },
  //     error: $.parseError(function(response) {
  //         $.popup.hidePreloader();

  //         if (response && response.errors) {
  //             // ошибки формы
  //             response.errors.forEach(function(record) {
  //                 var $field = $form.find('.' + record.fullname);
  //                 if ($field.length) {
  //                     $field.addClass(record.class);
  //                 }
  //             });
  //         } else {
  //             alert(window.DEFAULT_AJAX_ERROR);
  //         }
  //     }),
  //     complete: function() {
  //         $form.removeClass('sending');
  //     }
  // });

  // return false;
});