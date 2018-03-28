'use strict';

function buttonClickAndLoad () {
    $('button').on('click', function() {
        $(this).addClass('onclic', 250, validate);
    });
    
    function validate () {
        setTimeout(function() {
            $('button').removeClass('onclic');
        });
    }
}

function changeViewBySelect () {
    var page = $('#sort_by').val();
    
    $('#sort_by').on('change', function() {
        window.location = this.options[this.selectedIndex].value;
    });
}

$(function() {
    buttonClickAndLoad();
    changeViewBySelect();
});
