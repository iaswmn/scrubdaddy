(function () {

    /*
        Модальное окно с прелоадером.
        Возвращает Deferred-объект анимации показа.

        Требует:
            jquery.utils.js, jquery.popups.js
     */
    var addPreloader = function ($container) {
        var $preloader = $('<div>').addClass('preloader');
        $container.append($preloader);
    };

    $.preloader = function (options) {
        var opts = $.extend(true, {
            classes: 'popup-preloader',
            content: function () {
                addPreloader(this.$content);
            },
            closeButton: false,
            hideOnClick: false
        }, options);

        var popup = OverlayedPopup(opts);
        return popup && popup.show();
    };

    /*
        Показ/скрытие прелоадера над текущим окном.

        Требует:
            jquery.utils.js, jquery.popups.js
     */
    $.popup.showPreloader = function () {
        var popup = $.popup();
        if (!popup) {
            return
        }

        var $preloaderHolder = popup.$window.find('.preloader-overlay');
        if (!$preloaderHolder.length) {
            $preloaderHolder = $('<div>').addClass('preloader-overlay').appendTo(popup.$window);
            addPreloader($preloaderHolder);
        }

        if (typeof popup._origHideOnClick === "undefined") {
            popup._origHideOnClick = popup.opts.hideOnClick;
            popup.opts.hideOnClick = false;
        }

        popup.$container.find('.' + popup.CLOSE_BUTTON_CLASS).hide();
        popup.$container.addClass('popup-preloader-overlay');
    };

    $.popup.hidePreloader = function () {
        var popup = $.popup();
        if (!popup) {
            return
        }

        if (typeof popup._origHideOnClick !== "undefined") {
            popup.opts.hideOnClick = popup._origHideOnClick;
            delete popup._origHideOnClick;
        }

        popup.$container.find('.' + popup.CLOSE_BUTTON_CLASS).show();
        popup.$container.removeClass('popup-preloader-overlay');
    };

    function setCookie(cname, cvalue, exdays) {
        var d = new Date();
        d.setTime(d.getTime() + (exdays*24*60*60*1000));
        var expires = "expires="+ d.toUTCString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    }

    var $flug = $('.btn-box .flug');

    // !!!example data-country
    // $flug.attr('data-country', localStorage.getItem('country'));

    var country = $flug.data('country');

    console.log(country);

    if(country === 'usa'){
        $flug.addClass('active-usa');
        $flug.find('.choosen').addClass('usa');
    }else if(country === 'canada'){
        $flug.addClass('active-canada');
        $flug.find('.choosen').addClass('canada');
    }else if(country === 'israel'){
        $flug.addClass('active-israel');
        $flug.find('.choosen').addClass('israel');
    }else{
        $flug.addClass('active-usa');
        $flug.find('.choosen').addClass('usa');
    }

    // если область клика не флаг
    $('body').on('click', function(e){
        if($(e.target).attr('data-close') !== 'flug'){
            $flug.removeClass('active')
        }
    });

    $flug.on('click', function(){
        var el = $(this);
        el.toggleClass('active');
    });

    $flug.find('.usa').on('click', function () {
        $flug.addClass('active-usa');
        $flug.find('.choosen').removeClass('canada').removeClass('israel').addClass('usa');
        $flug.removeClass('active-canada').removeClass('active-israel');
        setCookie('country', 'US', 365);
        location.reload();
    });

    $flug.find('.canada').on('click', function () {
        $flug.addClass('active-canada');
        $flug.find('.choosen').removeClass('usa').removeClass('israel').addClass('canada');
        $flug.removeClass('active-usa').removeClass('active-israel');
        setCookie('country', 'CA', 365);
        location.reload();
    });

    $flug.find('.israel').on('click', function () {
        $flug.addClass('active-israel');
        $flug.find('.choosen').removeClass('usa').removeClass('canada').addClass('israel');
        $flug.removeClass('active-usa').removeClass('active-canada');
        setCookie('country', 'IL', 365);
        location.reload();
    });

})(jQuery);
