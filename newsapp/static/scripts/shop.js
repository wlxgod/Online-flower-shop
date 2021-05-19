$(document).ready(function (){
    var root=0;
    var root2=0;
    $('.quick_view_button').click(function () {

        root = this.parentNode.parentNode.parentNode.parentNode;
        $("#flowerName").html(root.childNodes[3].childNodes[1].childNodes[1].innerHTML);

        $("#currentPrice").html(root.childNodes[3].childNodes[3].childNodes[1].innerHTML);
        $("#originalPrice").html(root.childNodes[3].childNodes[3].childNodes[3].childNodes[0].innerHTML);
        $("#flowerNum").html(root.childNodes[3].childNodes[3].childNodes[5].innerHTML+" in stock now")
        $("#flowerIntro").html(root.childNodes[3].childNodes[3].childNodes[7].innerHTML)

        $("#target_image1").attr("src",root.childNodes[1].childNodes[1].childNodes[1].src);
        $("#target_image_bottom1").attr("src",root.childNodes[1].childNodes[1].childNodes[1].src);

        $("#target_image2").attr("src",root.childNodes[1].childNodes[1].childNodes[3].src);
        $("#target_image_bottom2").attr("src",root.childNodes[1].childNodes[1].childNodes[3].src);
    });

    $('.product-list-item').click(function () {
        root2 = this;
        $("#flowerName").html(root2.childNodes[3].childNodes[1].childNodes[0].innerHTML);
        $("#currentPrice").html(root2.childNodes[3].childNodes[3].childNodes[1].innerHTML);
        $("#originalPrice").html(root2.childNodes[3].childNodes[3].childNodes[3].childNodes[0].innerHTML);
        $("#flowerNum").html(root2.childNodes[5].innerHTML+" in stock now")
        $("#flowerIntro").html(root2.childNodes[3].childNodes[5].innerHTML)

        $("#target_image1").attr("src",root2.childNodes[1].childNodes[1].childNodes[1].src);
        $("#target_image_bottom1").attr("src",root2.childNodes[1].childNodes[1].childNodes[1].src);
        $("#target_image2").attr("src",root2.childNodes[1].childNodes[1].childNodes[3].src);
        $("#target_image_bottom2").attr("src",root2.childNodes[1].childNodes[1].childNodes[3].src);
    })
})
