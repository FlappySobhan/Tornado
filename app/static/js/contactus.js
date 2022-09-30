$(document).ready(function () {
    $("#main_map").hide();
    $("#showMap").click(function () {

        $("#main_map").slideToggle(200);
        if ($("#showMap").text() === "نمایش مکان روی نقشه") {
            $("#showMap").text("عدم نمایش نقشه");
        } else {
            $("#showMap").text("نمایش مکان روی نقشه");
        }
    });
});