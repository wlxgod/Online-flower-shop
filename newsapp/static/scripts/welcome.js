$(document).ready(function (){
    $('#enBlock').hide();
    $('#chBlock').hide();
    $('#enDiv').hover(function () {
        $('#enDiv').css('background','rgba(255,255,255,0.4)');
        $('#enBlock').show();
    },
        function () {
        $('#enDiv').css({'background-image':'url("./images/welcomeEn.webp")',background:''});
        $('#enBlock').hide();
    });
    $('#chDiv').hover(function () {
        $('#chDiv').css('background','rgba(255,255,255,0.4)');
        $('#chBlock').show();
    },
        function () {
        $('#chDiv').css({'background-image':'url("./images/welcomeCh.webp")',background:''});
        $('#chBlock').hide();
    });
});