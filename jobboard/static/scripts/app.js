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
    var $enterpriseForm = $('#enterpriseForm');

    if ( profileTypeVal == 'student') {
        $employeeForm.hide();
        $studentForm.show();
        $enterpriseForm.hide();
    } else if (profileTypeVal == 'employee') {
        $employeeForm.show();
        $studentForm.hide();
        $enterpriseForm.hide();
    } else {
        $enterpriseForm.show();
        $employeeForm.hide();
        $studentForm.hide();
    }
};

$(function() {
    closeNotification();
    displayUserAccountForm();
    $("#profileType").change(displayUserAccountForm);
});
