'use strict';

function changeViewBySelect() {
    var page = $('#sort_by').val();
    
    $('#sort_by').on('change', function() {
        window.location = this.options[this.selectedIndex].value;
    });
}

$(function() {
    changeViewBySelect();
});
