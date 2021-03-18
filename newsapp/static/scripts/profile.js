$(document).ready(function (){
    $("#inv-detail,#disc-detail,#liked-dis-detail,#liked-post-detail,#join-detail").hide()

    $("#inv").hover(function (){
        $("#inv-detail").show()
        $("#inv").css("background","rgba(255,255,255,0.8)")
    },function () {
        $("#inv-detail").hide()
        $("#inv").css("background","")
    });

    $("#disc").hover(function (){
        $("#disc-detail").show()
        $("#disc").css("background","rgba(255,255,255,0.8)")
    },function () {
        $("#disc-detail").hide()
        $("#disc").css("background","")
    });

    $("#like_discussion").hover(function (){
        $("#liked-dis-detail").show()
        $("#like_discussion").css("background","rgba(255,255,255,0.8)")
    },function () {
        $("#liked-dis-detail").hide()
        $("#like_discussion").css("background","")
    });

    $("#like_post").hover(function (){
        $("#liked-post-detail").show()
        $("#like_post").css("background","rgba(255,255,255,0.8)")
    },function () {
        $("#liked-post-detail").hide()
        $("#like_post").css("background","")
    });

    $("#join").hover(function (){
        $("#join-detail").show()
        $("#join").css("background","rgba(255,255,255,0.8)")
    },function () {
        $("#join-detail").hide()
        $("#join").css("background","")
    });


});