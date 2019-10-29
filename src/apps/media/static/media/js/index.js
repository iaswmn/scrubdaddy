(function ($) {

  $(document).ready(function () {

    var media = $(document).find('.media');

    var tabs = media.find('.tabs');

    var btnAll = tabs.find('.btn-all'),
      btnVideo = tabs.find('.btn-video'),
      btnAudio = tabs.find('.btn-audio'),
      btnArticle = tabs.find('.btn-article');

    var all = media.find('.all'),
      video = media.find('.video'),
      audio = media.find('.audio'),
      article = media.find('.article');

    function onClick($select, $openSelect, $hideSelect) {
      $select.on('click', function () {
        $('.btn-tab').removeClass('active');
        $(this).addClass('active');
        $openSelect();
        $hideSelect();
      });
    };

    onClick(btnAll, function () {
      all.css('display', 'block');
    }, function () {
      video.css('display', 'none');
      audio.css('display', 'none');
      article.css('display', 'none');
    });

    onClick(btnVideo, function () {
      video.css('display', 'block');
    }, function () {
      all.css('display', 'none');
      audio.css('display', 'none');
      article.css('display', 'none');
    });


    onClick(btnAudio, function () {
      audio.css('display', 'block');
    }, function () {
      all.css('display', 'none');
      video.css('display', 'none');
      article.css('display', 'none');
    });

    onClick(btnArticle, function () {
      article.css('display', 'block');
    }, function () {
      all.css('display', 'none');
      audio.css('display', 'none');
      video.css('display', 'none');
    });


  });

})(jQuery);