/**
 * Unicorn Admin Template
 * Diablo9983 -> diablo9983@gmail.com
**/
$(document).ready(function(){
	var current_id; // 声明一个全局变量，记录当前聊天的对象id
	var my_id; // 自己的id
	var image = $('#myicon').attr("class"); // 自己的头像
	var msg_template = '<p><span class="msg-block"><strong></strong><span class="time"></span><span class="msg"></span></span></p>';

	$('.chat-message button').click(function(){
		var input = $(this).siblings('span').children('input[type=text]');
		if(input.val() != ''){
			var time = new Date();
			console.log("myicon: "+image)
			$.post('/sendnew',{
				'receiver_id': current_id,
				'text': input.val()
			}).done(function (state) {
				console.log(state['state']);
				add_message('You',image,time,input.val(),true);
			});
		}
	});

	$('.chat-message input').keypress(function(e){
		if(e.which == 13) {
			if($(this).val() != ''){
				var time = new Date();
				$.post('/sendnew',{
				'receiver_id': current_id,
				'text': $(this).val()
			}).done(function (state){
				console.log(state['state']);
				add_message('You',image,time,$(this).val(),true);
				});
			}
		}
	});

	$('.online').click(function () {
        $(this).find('span').eq(1).css('display', 'none')
		console.log('Post start');
		current_id = $(this).attr("id");
		console.log('click_id: '+current_id);
		$('#chat-messages-inner').html(''); // 先清空
		var id = $(this).attr("id");
		var name = $(this).find('span').first().text(); // find()向下寻找所有子元素
		var img = $(this).find('img').attr("alt"); // 获取点击用户头像
		console.log('img:'+img);
		console.log('username:'+name);
		$.post('/current_user').done(function (user){
			my_id = user['id']
			console.log("id:"+my_id)
		})
		$.post('/shownews', {
			'user_id': id
		}).done(function (news) {
			// 输出当前用户的所有消息
			for (var i=0;i < news.length;i++){
				var text = news[i]['text']
				var time = news[i]['timestamp']
				if( news[i]['sender_id']==my_id){
					add_message('You', image, time, text, true)
				}else{
					add_message(name, img, time, text, true)
				}
			}
			//add_message(name, img, time, text, true)
		});
		console.log('finish');
	})

    
	/* 消息自动刷新，未实现
	setInterval(function(){
		var list = $('.online')
		for (l in list){
			var refresh_id = l.attr("id")
			$.post('/refreshnew',{
				'refresh_id': refresh_id
			}).done(function(result){
				var number = result['number']
				l.children('span').first().html(number)
			})
		}
	}, '1000'); */




	/* setTimeout(function(){
			add_message('Neytiri','/static/images/av2.jpg','I have a problem. My computer not work!')
		},'6000');
	setTimeout(function(){
			add_message('Cartoon Man','/static/images/av3.jpg','Turn off and turn on your computer then see result.')
		},'11000');
	setTimeout(function(){
            remove_user('neytiri','Neytiri')
        },'13500'); */
   	var i = 0;
	function add_message(name,img,time, msg,clear) {
		i = i + 1;
		var  inner = $('#chat-messages-inner');
		var time = new Date(time); // 先转化才能调用函数
		var year = time.getFullYear();
		var month = time.getMonth();
		var day = time.getDate();
		var hours = time.getHours();
		var minutes = time.getMinutes();
		if(month < 10) month = '0' + month
		if(hours < 10) hours = '0' + hours;
		if(minutes < 10) minutes = '0' + minutes;
		var datetime = year+'-'+month+'-'+day+' '+hours+':'+minutes;
		var id = 'msg-'+i;
        var idname = name.replace(' ','-').toLowerCase();
		inner.append('<p id="'+id+'" class="user-'+idname+'"><img src="'+img+'" alt="" />'
										+'<span class="msg-block"><strong>'+name+'</strong> <span class="time">- '+datetime+'</span>'
										+'<span class="msg">'+msg+'</span></span></p>');
		$('#'+id).hide().fadeIn(800);
		if(clear) {
			$('.chat-message input').val('').focus();
		}
		$('#chat-messages').animate({ scrollTop: inner.height() },1000);
	}
    function remove_user(userid,name) {
        i = i + 1;
        $('.contact-list li#user-'+userid).addClass('offline').delay(1000).slideUp(800,function(){
            $(this).remove();
        });
        var  inner = $('#chat-messages-inner');
        var id = 'msg-'+i;
        inner.append('<p class="offline" id="'+id+'"><span>User '+name+' left the chat</span></p>');
        $('#'+id).hide().fadeIn(800);
    }
});
