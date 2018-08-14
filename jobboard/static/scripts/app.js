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

function displayUserAccountForm() {
    var profileTypeVal = $('#profileType').val();
    var $employeeForm = $('#employeeForm');
    var $studentForm = $('#studentForm');

    if ( profileTypeVal == 'student') {
        $employeeForm.hide();
        $studentForm.show();
    } else {
        $employeeForm.show();
        $studentForm.hide();
    }
};

$(function() {
    closeNotification();
    displayUserAccountForm();
    $("#profileType").change(displayUserAccountForm);
});
