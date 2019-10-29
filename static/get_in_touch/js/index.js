(function($) {
    $.widget('app.selectmenu', $.ui.selectmenu, {
        _drawButton: function () {
            this._super();
            var selected = this.element
                    .find('[selected]'),
                selectedExist = selected.length,
                selectedOptionVal = selectedExist ? selected.val() : "";
            placeholder = this.options.placeholder;


            if (!selectedOptionVal && placeholder) {
                this.buttonItem.addClass('select-active');
                this.buttonItem.text(placeholder);
            }
        }
    });

    $(document).ready(function() {

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

        initUpload($('.upload-field').first());

        function fieldsAnimation() {

            var $phoneField = $("#id_phone"),
                $phoneFieldBox = $phoneField.parents(".field"),

                $emailField = $(".field-email"),
                $emailInput = $emailField.find("input"),

                $timeFieldsBox = $(".time-fields-outer-box"),
                $reachTimeField = $("#id_reach_time"),
                $timeZoneField = $("#id_time_zone"),
                $nameField = $("#id_name");



            var init = function(width) {

                if (width >= 1024) $phoneFieldBox .css("position","absolute");

                // $emailField.addClass("show-hide-fields");
                // $phoneFieldBox.addClass("show-hide-fields");


                var option = $('#id_reach_type').find("option").filter("[selected='selected']");

                if ( option.length && option.val() !== "" ) {

                    addRemoveAttr( option.val() );

                } else {
                    $emailField.removeClass("js-active");
                    $phoneFieldBox.removeClass("js-active");

                    // $timeFieldsBox
                    //     .hide();
                }



                $nameField.attr("required", "");
            };

            var changeHandler = function(ev, ui) {

                if ( addRemoveAttr(ui.item.value) ) { return true; }

                $phoneFieldBox
                    .removeClass("js-active")
                    .addClass("js-move-up");


                $timeFieldsBox.hide();

                $emailField
                    .removeClass("js-active");
            };

            var addRemoveAttr = function (value) {
                if ( value === "Phone" ) {
                    showPhoneFields();
                    return true;

                } else if ( value === "Email" ) {

                    showEmailFields();
                    return true;
                }
            };

            var showEmailFields = function () {
                $phoneFieldBox
                    .removeClass("js-active")
                    .addClass("js-move-up");

                $timeFieldsBox.hide();
                $phoneField.removeAttr("required");
                $reachTimeField.removeAttr("required");
                $timeZoneField.removeAttr("required");

                $emailField.addClass("js-active");
                $emailInput.attr("required", "");
            };

            var showPhoneFields = function () {
                $phoneFieldBox
                    .addClass("js-active")
                    .removeClass("js-move-up");

                $phoneField.attr("required", "");
                $reachTimeField.attr("required", "");
                $timeZoneField.attr("required", "");


                $timeFieldsBox.show();

                $emailField.addClass("js-active");
                $emailInput.attr("required", "");

            };

            return {
                "start": init,
                "changeHandler": changeHandler
            }
        }

        var anim = fieldsAnimation();

        anim.start( $.winWidth() );

        $('#id_reach_type').selectmenu({
            // placeholder: 'Please select',
            classes: {
                'ui-selectmenu-button': 'custom-select-button',
                'ui-selectmenu-menu': 'custom-select-menu'
            },
            change: function (ev, ui) {
                anim.changeHandler(ev, ui);
            }
        });

        $('#id_time_zone').selectmenu({
            // placeholder: 'Time',
            classes: {
                'ui-selectmenu-button': 'custom-select-button',
                'ui-selectmenu-menu': 'custom-select-menu',
                'ui-selectmenu-text': 'custom-select-text'
            }
        });

        $('#id_reach_time').selectmenu({
            classes: {
                'ui-selectmenu-button': 'custom-select-button',
                'ui-selectmenu-menu': 'custom-select-menu',
                'ui-selectmenu-text': 'custom-select-text'
            }
        });
    });

})(jQuery);
