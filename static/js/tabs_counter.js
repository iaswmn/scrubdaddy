(function($){

    $(document).ready(function() {

       var $tabsBox = $("#tabs-list");

       if ( $tabsBox.length ) {
           var tabBtnsAmount = $tabsBox.children().length;

           console.log("this is tabs amount", tabBtnsAmount );
       }

    });

})(jQuery);