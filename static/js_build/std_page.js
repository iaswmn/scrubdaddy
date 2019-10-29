(function(){$('.btn').one('click',function(){var $this=$(this);var link=$this.attr('link');$.ajax({url:link,type:'get',success:function(response){console.log(response)
if(response.success_message){var $container=$(document).find('.smiling_scrubbers');$container.append(response.success_message)
}},})
});}).call(this);