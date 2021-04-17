$(document).ready(function (){
    mouse = "dash";
    $("#dashboardLi").css({"background":"#ca7101", "color": "white"});
    $("#dashboardLi img").attr('src',"../static/images/dashboardW.png");
    $("#dashboard").show();
    $("#order").hide();
    $("#changeP").hide();

    $("#dashboardLi").on("click",function (){
        $("#dashboard").show();
        $("#order").hide();
        $("#changeP").hide();

        mouse = "dash";

        $("#dashboardLi").css({"background":"#ca7101", "color": "white"});
        $("#orderLi").css({"background":"", "color": ""});
        $("#changePLi").css({"background":"", "color": ""});

        $("#dashboardLi img").attr('src',"../static/images/dashboardW.png");
        $("#orderLi img").attr('src',"../static/images/order.png");
        $("#changePLi img").attr('src',"../static/images/changePassword.png");
    });
    $("#orderLi").click(function (){
        $("#dashboard").hide();
        $("#order").show();
        $("#changeP").hide();

        mouse = "order";

        $("#dashboardLi").css({"background":"", "color": ""});
        $("#orderLi").css({"background":"#ca7101", "color": "white"});
        $("#changePLi").css({"background":"", "color": ""});

        $("#dashboardLi img").attr('src',"../static/images/dashboard.png");
        $("#orderLi img").attr('src',"../static/images/orderW.png");
        $("#changePLi img").attr('src',"../static/images/changePassword.png");
    });
    $("#changePLi").click(function (){
        $("#dashboard").hide();
        $("#order").hide();
        $("#changeP").show();

        mouse = "change";


        $("#dashboardLi").css({"background":"", "color": ""});
        $("#orderLi").css({"background":"", "color": ""});
        $("#changePLi").css({"background":"#ca7101", "color": "white"});

        $("#dashboardLi img").attr('src',"../static/images/dashboard.png");
        $("#orderLi img").attr('src',"../static/images/order.png");
        $("#changePLi img").attr('src',"../static/images/changePW.png");
    });

    $("#dashboardLi").hover(function (){
        if(mouse !== "dash"){
            $("#dashboardLi img").attr('src',"../static/images/dashboardW.png");
        }

    },function () {
        if(mouse !== "dash"){
            $("#dashboardLi img").attr('src',"../static/images/dashboard.png");
        }
    });

    $("#orderLi").hover(function (){
        if(mouse !== "order"){
            $("#orderLi img").attr('src',"../static/images/orderW.png");
        }

    },function () {
        if(mouse !== "order"){
            $("#orderLi img").attr('src',"../static/images/order.png");
        }
    });
    $("#changePLi").hover(function (){
        if(mouse !== "change"){
            $("#changePLi img").attr('src',"../static/images/changePW.png");
        }

    },function () {
        if(mouse !== "change"){
            $("#changePLi img").attr('src',"../static/images/changePassword.png");
        }
    });
});