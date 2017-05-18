$(document).ready(function () {
    $("#loading_animation_sensor").hide();
    $("#loading_animation_water").hide();
    $("#ok_sensor").hide();
    $("#not_ok_sensor").hide();
    $("#ok_water").hide();
    $("#not_ok_water").hide();
});

function disableInput() {
    $('input').prop('disabled', true);
}

function enableInput() {
    $('input').prop('disabled', false);
}
function getTime() {
    $.ajax({
        type: "GET",
        url: '/time',
        success: function (data) {
            // data is ur summary
            $('#time').html(data);
        }

    });

}

function getSoilStatus() {
    $.ajax({
        type: "GET",
        url: "/status",
        beforeSend: function () {
            $("#loading_animation_sensor").show();
            disableInput();
        },
        success: function (data) {
            $("#loading_animation_sensor").hide();
            if (data = 'True') {
                $("#ok_sensor").show();
            } else {
                $("#not_ok_sensor").show();
            }
            enableInput();
        }
    });
}

function waterPlants() {
    $.ajax({
        type: "GET",
        url: "/water",
        beforeSend: function () {
            $("#loading_animation_water").show();
            disableInput();
        },
        success: function (data) {
            $("#loading_animation_water").hide();
            $("#ok_water").show();
            enableInput();
        }
    });
}

