$(document).ready(function () {
    $('.quickllook').on('click',function (event) {
        var rootLi = event.target.parentNode.parentNode.parentNode;

        var target_img = rootLi.children[0].children[0].src;
        var target_intro = rootLi.children[1].children[0].innerHTML;
        var target_name = rootLi.children[1].children[2].innerHTML;
        var target_number = rootLi.children[1].children[1].innerHTML;
        var target_price = rootLi.children[1].children[4].innerHTML;
        console.log(target_img);
        console.log(target_intro);
        console.log(target_name);
        console.log(target_number);
        console.log(target_price);
        $('#target-name').html(target_name);
        $('#target-image').attr('src',target_img);
        $('#target-number').html(target_number);
        $('#target-price').html(target_price);
        $('#tabDes').html(target_intro);
    })
    $('.quickllook2').on('click',function (event) {
        var rootLi = event.target.parentNode.parentNode;
        var target_img = rootLi.children[0].children[0].src;
        var target_intro = rootLi.children[1].children[1].innerHTML;
        var target_name = rootLi.children[1].children[0].innerHTML;
        var target_number = rootLi.children[1].children[2].innerHTML;
        var target_price = rootLi.children[2].innerHTML;
        console.log(target_img);
        console.log(target_intro);
        console.log(target_name);
        console.log(target_number);
        console.log(target_price);
        $('#target-name').html(target_name);
        $('#target-image').attr('src',target_img);
        $('#target-number').html(target_number);
        $('#target-price').html(target_price);
        $('#tabDes').html(target_intro);
    })
})