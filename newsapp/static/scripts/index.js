$(document).ready(function (){
    $('.quick_view_button').click(function () {
        root = this.parentNode.parentNode.parentNode.parentNode;
        // alert("image1"+root.childNodes[1].childNodes[1].childNodes[3].className);
        // alert("image2"+root.childNodes[1].childNodes[1].childNodes[5].className);
        // alert("name"+);
        // alert("currentPrice: "+);
        // alert("originPrice: "+);
        // alert("intro"+);
        // alert("number"+);
        $("#flowerName").html(root.childNodes[3].childNodes[1].childNodes[1].innerHTML);
        $("#currentPrice").html(root.childNodes[3].childNodes[3].childNodes[1].innerHTML);
        $("#originalPrice").html(root.childNodes[3].childNodes[3].childNodes[3].childNodes[0].innerHTML);
        $("#flowerNum").html(root.childNodes[3].childNodes[1].childNodes[4].innerHTML+" in stock now")
        $("#flowerIntro").html(root.childNodes[3].childNodes[1].childNodes[3].innerHTML)
    })
})
