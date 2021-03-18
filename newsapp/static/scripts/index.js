$(document).ready(function (){
    aa(0);
    $("li").mouseover(function (){
        clearInterval(timePlay);

        index = $(this).index();
        $(this).addClass("active").siblings().removeClass("active");
        $(".images img").eq(index).show().siblings().hide();
    }).mouseout(function (){
        aa(index);
    });
    var time;
    function aa(t){
        time = t;
        timePlay = setInterval(function (){
            time++;
            $("ul li").eq(time%6).addClass("active").siblings().removeClass("active");
            $(".images img").eq(time%6).show().siblings().hide();
        },1500);
    }

    $(".left").click(function (){
        clearInterval(timePlay);
        time--;
        console.log(time);
        if(time<0){
            aa(5);
        }
        else{
            $("ul li").eq(time%6).addClass("active").siblings().removeClass("active");
            $(".images img").eq(time%6).show().siblings().hide();
            aa(time)
        }
    })

     $(".right").click(function (){
        clearInterval(timePlay);
        time++;
        $("ul li").eq(time%6).addClass("active").siblings().removeClass("active");
        $(".images img").eq(time%6).show().siblings().hide();
        aa(time)
    })
});

