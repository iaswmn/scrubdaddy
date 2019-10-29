(function($) {

    /** @namespace window.js_storage.ajax_contact */

    /*
        Показ окна контактов
     */
    window.contactPopup = function() {
        $.preloader();

        return $.ajax({
            url: window.js_storage.ajax_contact,
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                if (response.form) {
                    var popup = $.popup({
                        classes: 'contact-popup contact-form-popup',
                        content: response.form
                    }).show();
                    
                }
            },
            error: $.parseError(function() {
                alert(window.DEFAULT_AJAX_ERROR);
                $.popup().hide();
            })
        });
    };


    /*
        Открытие окна контактов при клике на кнопки
     */
    $(document).on('click', '.open-contact-popup', function() {
        contactPopup();
        return false;
    });


    /*
        Отправка AJAX-формы со страницы
     */
    $(document).on('submit', '#ajax-contact-form', function() {
        var $form = $(this);
        if ($form.hasClass('sending')) {
            return false;
        }

        // добавление адреса страницы, откуда отправлена форма
        var data = $(this).serializeArray();
        data.push({
            name: 'referer',
            value: location.href
        });

        $.ajax({
            url: window.js_storage.ajax_contact,
            type: 'post',
            data: data,
            dataType: 'json',
            beforeSend: function() {
                $.preloader();
                $form.addClass('sending');
                $form.find('.invalid').removeClass('invalid');
            },
            success: function(response) {
                if (response.success_message) {
                    // сообщение о успешной отправке
                    $.popup({
                        classes: 'contact-popup contact-success-popup',
                    }).show();

                    $form.get(0).reset();
                }
            },
            error: $.parseError(function(response) {
                $.popup().hide();

                if (response && response.errors) {
                    // ошибки формы
                    response.errors.forEach(function(record) {
                        var $field = $form.find('.' + record.fullname);
                        if ($field.length) {
                            $field.addClass(record.class);
                        }
                    });
                } else {
                    alert(window.DEFAULT_AJAX_ERROR);
                }
            }),
            complete: function() {
                $form.removeClass('sending');
            }
        });

        return false;
    });


    /*
        Отправка AJAX-формы из попапа
     */
    $(document).on('submit', '#ajax-popup-contact-form', function() {
        var $form = $(this);
        if ($form.hasClass('sending')) {
            return false;
        }

        // добавление адреса страницы, откуда отправлена форма
        var data = $(this).serializeArray();
        data.push({
            name: 'referer',
            value: location.href
        });

        $.ajax({
            url: window.js_storage.ajax_contact,
            type: 'post',
            data: data,
            dataType: 'json',
            beforeSend: function() {
                $.popup.showPreloader();
                $form.addClass('sending');
                $form.find('.invalid').removeClass('invalid');
            },
            success: function(response) {
                if (response.success_message) {
                    // сообщение о успешной отправке
                    $.popup({
                        classes: 'contact-popup contact-success-popup',
                        content: response.success_message
                    }).show();
                }
            },
            error: $.parseError(function(response) {
                $.popup.hidePreloader();

                if (response && response.errors) {
                    // ошибки формы
                    response.errors.forEach(function(record) {
                        var $field = $form.find('.' + record.fullname);
                        if ($field.length) {
                            $field.addClass(record.class);
                        }
                    });
                } else {
                    alert(window.DEFAULT_AJAX_ERROR);
                }
            }),
            complete: function() {
                $form.removeClass('sending');
            }
        });

        return false;
    });



    window.getInTouchPopup = function() {
        $.preloader();

        return $.ajax({
            url: window.js_storage.ajax_get_in_touch,
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                if (response.form) {
                    var popup = $.popup({
                        classes: 'contact-popup contact-form-popup',
                        content: response.form
                    }).show();
                    initUpload($('.upload-field').first());
                }
            },
            error: $.parseError(function() {
                alert(window.DEFAULT_AJAX_ERROR);
                $.popup().hide();
            })
        });
    };


    /*
        Открытие окна контактов при клике на кнопки
     */
    $(document).on('click', '.open-get-in-touch-popup', function() {
        getInTouchPopup();
        return false;
    });

    /*
        Отправка AJAX-формы из попапа
     */
    $(document).on('submit', '#ajax-popup-get-in-touch-form', function() {
        var $form = $(this);
        if ($form.hasClass('sending')) {
            return false;
        }

        // добавление адреса страницы, откуда отправлена форма
        var data = $(this).serializeArray();
        data.push({
            name: 'referer',
            value: location.href
        });

        $.ajax({
            url: window.js_storage.ajax_get_in_touch,
            type: 'post',
            data: data,
            dataType: 'json',
            beforeSend: function() {
                $.popup.showPreloader();
                $form.addClass('sending');
                $form.find('.invalid').removeClass('invalid');
            },
            success: function(response) {
                if (response.success_message) {
                    // сообщение о успешной отправке
                    $.popup({
                        classes: 'contact-popup contact-success-popup',
                        content: response.success_message
                    }).show();
                }
            },
            error: $.parseError(function(response) {
                $.popup.hidePreloader();

                if (response && response.errors) {
                    // ошибки формы
                    response.errors.forEach(function(record) {
                        var $field = $form.find('.' + record.fullname);
                        if ($field.length) {
                            $field.addClass(record.class);
                        }
                    });
                } else {
                    alert(window.DEFAULT_AJAX_ERROR);
                }
            }),
            complete: function() {
                $form.removeClass('sending');
            }
        });

        return false;
    });




      /*
        Инициализация поля загрузки файлов.
     */
  var initUpload = function ($root) {
    var name = $root.attr('data-upload-name');

    Uploader($root, {
      url: $root.attr('data-upload-url'),
      fileName: name,
      buttonSelector: '.add-photo',
      dropSelector: null,
      multiple: true,
      max_size: '40mb',
      prevent_duplicates: false,

      onBeforeFileUpload: function (file) {
        var that = this;
        var $queue = this.$root.find('.queue');
        $('<div>').addClass('record record-' + file.id).data({
          'id': file.id
        }).append(
          $('<div>').addClass('cancel-btn'),
          $('<div>').addClass('name').text(file.name),
          $('<input>').attr({
            'type': 'hidden',
            'name': name + '[][name]',
            'value': ''
          }),
          $('<input>').attr({
            'type': 'hidden',
            'name': name + '[][file]',
            'value': ''
          })
        ).on('click', '.cancel-btn', function () {
          var $record = $(this).closest('.record');
          var file_id = $record.data('id');
          $record.find('input').remove();

          that.removeFile(file_id);

          $record.fadeOut({
            duration: 200,
            complete: function () {
              $(this).remove();
            }
          });
        }).appendTo($queue);
      },
      onFileUploadProgress: function (file, percent) {
        var $queue = this.$root.find('.queue');
        var $record = $queue.find('.record-' + file.id);

        $record.find('.name').css('background-size', percent + '% 1px');
      },
      onFileUploaded: function (file, response) {
        var $queue = this.$root.find('.queue');
        var $record = $queue.find('.record-' + file.id);

        $record.addClass('loaded');
        $record.find('.name').css('background', 'none');

        if (response && response.name && response.filename) {
          $record.find('input[name$="[name]"]').val(response.name);
          $record.find('input[name$="[file]"]').val(response.filename);
        }
      },
      onFileUploadError: function (file, error) {
        if (error.code === plupload.FILE_EXTENSION_ERROR) {
          alert('This type of file is not allowed.\nMust be one of the following: jpg,jpeg,png,bmp,gif');
        } else {
          console.log(error);
        }
      }
    });
  };



})(jQuery);
