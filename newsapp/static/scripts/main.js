$(document).ready(function (){
    $(".invitations").show()
    $(".discussions").hide()
    $("#invitation").css("background","#ff267e")
    $("#discussion").css("background","rgba(255,255,255,0.1)")
    $("#invitation").hover(function () {
        $(".invitations").show()
        $(".discussions").hide()
        $("#invitation").css("background","#ff267e")
        $("#invitation").css("color","white")
        $("#discussion").css("background","rgba(255,255,255,0.1)")
        $("#discussion").css("color","black")
    })

    $("#discussion").hover(function () {
        $(".discussions").show()
        $(".invitations").hide()
        $("#invitation").css("background","rgba(255,255,255,0.1)")
        $("#invitation").css("color","black")
        $("#discussion").css("background","#ff267e")
        $("#discussion").css("color","white")
    })
});