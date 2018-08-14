'use strict';

function closeNotification () {
    var $closeIcon = $('.close-alert');
    var $notificationAlert = $('.alert-messages');

    $closeIcon.each(function(){
        $(this).on('click', function() {
            $notificationAlert.remove();
        });
    });

};

$(function() {
    closeNotification();
});
