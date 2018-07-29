'use strict';

function buttonClickAndLoad () {
    $('.btn-more').on('click', function() {
        $(this).addClass('onclic', 250, validate);
    });

    function validate () {
        setTimeout(function() {
            $('.btn-more').removeClass('onclic');
        });
    }
};

function changeViewBySelect () {
    var page = $('#sort_by').val();

    $('#sort_by').on('change', function() {
        window.location = this.options[this.selectedIndex].value;
    });
};

function closeNotification () {
    var $closeIcon = $('.close-alert');
    var $notificationAlert = $('.alert-messages');

    $closeIcon.each(function(){
        $(this).on('click', function() {
            $notificationAlert.remove();
        });
    });

};

function prepareDatePicker() {
    $('.datepicker').each(function(index, element) {
        var $element = $(element);

        var options = {
            type: Date,
            format: 'yyyy-mm-dd',
            numberOfMonths: 2,
            showButtonPanel: true,
            weekStart: 1,
            startView: 0,
            minDate: '+1d',
            changeMonth: true,
            changeYear: true,
            onSelect: function(date){
                var dates = date.split('/');
                var lastDate = new Date(dates[2], dates[0], 0);
                var y = lastDate.getFullYear(), m = lastDate.getMonth(), d = lastDate.getDate();
                m = ('0'+ (m+1)).slice(-2);

                $("[name='booking_end_date']").val(y+'-'+m+'-'+d);
            }
        }
        $element.datepicker(options);
    });
};

$(function() {
    buttonClickAndLoad();
    changeViewBySelect();
    closeNotification();
    prepareDatePicker();
    console.log('starting app...')
});
