$( document ).ready(function() {
    $("#loadingAnimation").hide();
    $("#ok").hide();
    $("#not_ok").hide();
});

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
            $("#status").hide();
            $("#loadingAnimation").show();
        },
        success: function (data) {
            $("#loadingAnimation").hide();
            if(data = 'True'){
                $("#ok").show();
            }else {
                $("#not_ok").show();
            }
            $('#status').html(data);
        }
    });
}

