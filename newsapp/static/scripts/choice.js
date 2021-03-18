$(document).ready(function (){
    $(".discussionOl").show()
    $(".invitationOl").hide()
    $(".discussionPart").css("background","#ff267e")
    $(".invitationPart").css("background","rgba(255,255,255,0.1)")
    $(".invitationPart").hover(function () {
        $(".invitationOl").show()
        $(".discussionOl").hide()
        $(".discussionPart").css("background","rgba(255,255,255,0.1)")
        $(".invitationPart").css("background","#ff267e")
    })

    $(".discussionPart").hover(function () {
        $(".discussionOl").show()
        $(".invitationOl").hide()
        $(".discussionPart").css("background","#ff267e")
        $(".invitationPart").css("background","rgba(255,255,255,0.1)")
    })
});