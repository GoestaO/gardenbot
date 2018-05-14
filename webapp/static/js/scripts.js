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
    $("#loading_animation_water_level").hide();
    $("#ok_sensor").hide();
    $("#not_ok_sensor").hide();
    $("#ok_water").hide();
    $("#not_ok_water").hide();
    $("#positive").hide();
    $("#negative").hide();
    $("#sensordata_table").hide();
    $("#history_chart").hide();
    $("#loading_animation_history").hide();
}

function getSensorData() {
    resetPage();
    var documentURL = document.URL;
    var target = documentURL.concat("sensordata");
    $.ajax({
        type: "GET",
        url: target,
        beforeSend: function () {
            $("#sensordata_table").hide();
            $("#loading_animation_sensor").show();
            $("#sensor").hide();
        },
        success: function (data) {
            $("#loading_animation_sensor").hide();
            $("#sensor").show('fast');
            setSensorResults(data);
            $("#sensordata_table").show();
        }
    });
}

function setSensorResults(data) {
    var temperature = Math.round(data['temperature']);
    $("#temperature_value").text(temperature + " °C");
    $("#humidity_value").text(data['moisture'] + " %")
    $("#fertility_value").text(data['conductivity'])
    $("#light_value").text(data['light'])
}

function renderSensorDataTable(data) {
    $('#sensordata_table').append(
        "<tr>",
        "<td>Light: </td>",
        "<td>" + data['light'] + "</td>",
        "</tr>",
        "<tr>",
        "<td>Moisture: </td>",
        "<td>" + data['moisture'] + "</td>",
        "</tr>",
        "<tr>",
        "<td>Fertility: </td>",
        "<td>" + data['conductivity'] + "</td>",
        "</tr>"
    );
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
            $("#not_ok_sensor").delay(5000).hide('fast');
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

function enoughWater() {
    var documentURL = document.URL;
    var target = documentURL.concat("waterstatus");
    $.ajax({
        type: "GET",
        url: target,
        beforeSend: function () {
            $("#water_level").hide();
            $("#loading_animation_water_level").show();
        },
        success: function (data) {
            $("#loading_animation_water_level").hide();
            if (data == 'True') {
                $("#positive").show();
            } else if (data == 'False') {
                $("#negative").show();
            }
            $("#positive").delay(5000).hide('fast');
            $("#negative").delay(5000).hide('fast');
            $("#water_level").delay(5100).show('fast');
        }
    });
}

function getWaterHistory() {
    resetPage();
    var documentURL = document.URL;
    var target = documentURL.concat("history");
    $.ajax({
        type: "GET",
        url: target,
        beforeSend: function () {
            $("#history").hide();
            $("#loading_animation_history").show();
        },
        success: function (data) {
            generateHistoryChart(data);
            $("#history_chart").show();
            $("#loading_animation_history").hide();
            $("#history").show();
        }
    });
}


function generateHistoryChart(data) {
    var series = [{
        data: data, showInLegend: false,
    }];

    Highcharts.chart('history_chart', {
        chart: {
            backgroundColor: '#DCDCDC',
            type: 'column'
        },
        title: {
            text: null
        },

        yAxis: {
            title: {
                text: 'Number of waterings'
            },
            tickInterval: 1,
        },
        xAxis: {
            type: 'datetime',
            tickInterval: 24 * 3600 * 1000,
        },
        series: series,
        tooltip: {
            formatter: function () {
                return Highcharts.dateFormat('%d.%m.%Y',
                    new Date(this.x)) + ': ' + this.y;
            }
        },
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
            }]
        },

    });
}


