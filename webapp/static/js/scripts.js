$( document ).ready(function() {
    $("#loadingAnimation").hide();
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
            $('#status').html(data);
        }
    });
}

