'use strict';

var prepareFormBase = function() {
  var $form = $('body').find('form'),
      $helpText = $form.find('helptext');
  
  $helpText.each(function(i) {
    $(this).hide();
  });
};

$(function() {
  prepareFormBase();
});
