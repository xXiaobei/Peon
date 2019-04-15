// 轮训发布
function publish_all() {
    let ser_id = 1;
    //$SCRIPT_ROOT +
    $.getJSON(
         '/publish',
        {server_id: ser_id},
        function (data) {

        }
    );
}

$(function () {
    $("#publish_all").on("click", publish_all);
})



