(function($) {

  $.datepicker._generateMonthYearHeader_original = $.datepicker._generateMonthYearHeader;

  $.datepicker._generateMonthYearHeader = function(inst, dm, dy, mnd, mxd, s, mn, mns) {
      var header = $(
          $.datepicker._generateMonthYearHeader_original(inst, dm, dy, mnd, mxd, s, mn, mns)
      );

      var yearReverse = this._get( inst, "yearReverse");
      if (yearReverse) {
          var $years = header.find('.ui-datepicker-year');

          // reverse the years
          $years.html(
              Array.prototype.reverse.apply($years.children())
          );
      }

      // return our new html
      return $('<div />').append(header).html();
  }

})(jQuery);