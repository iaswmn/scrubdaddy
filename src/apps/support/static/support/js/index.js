// pure js without jquery
(function () {

  // document ready on pure js DOMContentLoaded
  // Simple find height description and give it parent with resize and load

  document.addEventListener("DOMContentLoaded", function (event) {

    var accordion = document.querySelector('.accordion');

    if(accordion){
      var container = accordion.querySelector('.accordion-container');
      var title = container.querySelectorAll('.title');
    }


    if(container){
      // multi events if you're need more than one event
      function addListenerMulti(element, eventNames, listener) {
        var events = eventNames.split(' ');
        // you can see that we gettig two event names, if you make console.log(events)
        // and we handler them
        for (var i = 0, iLen = events.length; i < iLen; i++) {
          element.addEventListener(events[i], listener, false);
        }
      }
  
      // multi events after load we have resize for check heigth description and give it
      addListenerMulti(window, 'load resize', function () {
  
        var elems = document.querySelectorAll('.description');
        for (var l = 0; l < elems.length; l++) {
          var items = elems[l].parentElement.parentElement;
          if (items.classList.contains('active')) {
            elems[l].parentElement.style.height = elems[l].clientHeight + 'px';
          } else {
            elems[l].parentElement.style.height = 0 + 'px';
          }
        }
  
      });
  
      // if he is made click we show our hidden block
      for (var i = 0; i < title.length; i++) {
        // listener with event click
        title[i].addEventListener('click', function () {
  
          var height = this.parentElement.querySelector('.description').clientHeight,
            elem = this.parentElement.querySelector('.hide__side');

          // checking on height if we gave it then elem.style = 0 else elem.style = height description, this is simple
            console.log('this is element clien height', elem.clientHeight);
            console.log('this is height', height);
          if (elem.clientHeight === height) {
            elem.style.height = '0px';
            // it's has arrow on left side, do remove -
            this.parentElement.classList.remove('active');
          } else {
            elem.style.height = height + 'px';
            // after add -
            this.parentElement.classList.add('active');
          }
  
        })
      }
  
  
      var options = {
        valueNames: ['title', 'description']
      };
  
      var list = new List('accordion', options);
    }

  });

  $.widget('app.selectmenu', $.ui.selectmenu, {
    _drawButton: function () {
      this._super();
      var selected = this.element
        .find('[selected]')
        .length,
        placeholder = this.options.placeholder;

      if (!selected && placeholder) {
        this.buttonItem.addClass('select-active');
        this.buttonItem.text(placeholder);
      }
    }
  });


  // jquery

  var faq = $(document).find('.faq');
  var choosen = faq.find('.choosen');
  var cat = choosen.find('.category');

  var items = faq.find('.item');

  cat.selectmenu({
    placeholder: 'Filter by Product',
    classes: {
      'ui-selectmenu-text': 'filter-select-text'
    },
    change: function (event, ui) {
      items.addClass('disable');
      items.removeClass('enable');
      for (var i = 0; i < items.length; i++) {
        if (ui.item.value === 'disable') {
          items.removeClass('disable enable');
        } else if (items.eq(i).attr('data-category').indexOf(ui.item.value) !== -1) {
          items.eq(i).addClass('enable');
        }
      }
    }
  });

})();