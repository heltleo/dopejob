'use strict';

function buttonClickAndLoad () {
    django.jQuery('.btn-more').on('click', function() {
        django.jQuery(this).addClass('onclic', 250, validate);
    });

    function validate () {
        setTimeout(function() {
            django.jQuery('.btn-more').removeClass('onclic');
        });
    }
}

function changeViewBySelect () {
    var page = django.jQuery('#sort_by').val();

    django.jQuery('#sort_by').on('change', function() {
        window.location = this.options[this.selectedIndex].value;
    });
}

function closeNotification () {
    var $closeIcon = django.jQuery('.close-alert');
    var $notificationAlert = django.jQuery('.alert-messages');

    $closeIcon.each(function(){
        django.jQuery(this).on('click', function() {
            $notificationAlert.remove();
        });
    });

}

django.jQuery(function() {
    buttonClickAndLoad();
    changeViewBySelect();
    closeNotification();
});
