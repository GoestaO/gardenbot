$(document).ready(function () {
    resetPage();
});

function disableInput() {
    $('input').prop('disabled', true);
}

function enableInput() {
    $('input').prop('disabled', false);
    $("#ok_sensor").delay(5000).fadeOut();
    $("#not_ok_sensor").delay(5000).fadeOut();
    $("#ok_water").delay(5000).fadeOut();
}

function resetPage() {
    $("#loading_animation_sensor").hide();
    $("#loading_animation_water").hide();
    $("#ok_sensor").hide();
    $("#not_ok_sensor").hide();
    $("#ok_water").hide();
    $("#not_ok_water").hide();
}

function getSoilStatus() {
    var documentURL = document.URL;
    var target = documentURL.concat("status");
    $.ajax({
        type: "GET",
        url: target,
        beforeSend: function () {
            $("#loading_animation_sensor").show();
            $("#sensor").hide();
        },
        success: function (data) {
            $("#loading_animation_sensor").hide();
            if (data == 'True') {
                $("#ok_sensor").show();
            } else if (data == 'False') {
                $("#not_ok_sensor").show();
            }
            $("#ok_sensor").delay(5000).hide('fast');
            $("#sensor").delay(5100).show('fast');
        }
    });
}

function waterPlants() {
    var documentURL = document.URL;
    var target = documentURL.concat("water");
    $.ajax({
        type: "GET",
        url: target,
        beforeSend: function () {
            $("#water_can").hide();
            $("#loading_animation_water").show();
        },
        success: function (data) {
            $("#loading_animation_water").hide();
            $("#ok_water").show();
            $("#ok_water").delay(5000).hide('fast');
            $("#water_can").delay(5100).show('fast');
        }
    });
}

