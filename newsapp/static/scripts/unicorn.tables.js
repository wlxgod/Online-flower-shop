/**
 * Blizzard OrderDisplay Table
 * Ranger -> 403331475@qq.com
**/
Date.prototype.format = function(fmt) {
     var o = {
        "M+" : this.getMonth()+1,                 //月份
        "d+" : this.getDate(),                    //日
        "h+" : this.getHours(),                   //小时
        "m+" : this.getMinutes(),                 //分
        "s+" : this.getSeconds(),                 //秒
        "q+" : Math.floor((this.getMonth()+3)/3), //季度
        "S"  : this.getMilliseconds()             //毫秒
    };
    if(/(y+)/.test(fmt)) {
            fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
    }
     for(var k in o) {
        if(new RegExp("("+ k +")").test(fmt)){
             fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
         }
     }
    return fmt;
}


$(document).ready(function(){


	status_dic={};
	status_dic['Transporting'] = 3;
	status_dic['配送中'] = 3;
	status_dic['已完成'] = 2;
	status_dic['Completed'] = 2;
	status_dic['已超时'] = 4;
	status_dic['Lated'] = 4;
	status_dic['紧急件'] = 5;
	status_dic['Urgent'] = 5;

	function ReLoadDate(){
		var oTab = document.getElementById('main');

			var arr = [];

			for (var i = 0; i < oTab.tBodies[0].rows.length; i++) {
				arr[i] = oTab.tBodies[0].rows[i];
				arr[i].cells[1].innerHTML=new Date(arr[i].cells[1].innerHTML).format("yyyy/MM/dd hh:mm:ss");
			}

			// console.dir(arr[2].cells[1].innerHTML);
			// arr[2].cells[1].innerHTML='manchangheiye';

			for (var i = 0; i < arr.length; i++) {
				oTab.tBodies[0].appendChild(arr[i]);
			}

	};

	function initialRanking(){
		var oTab = document.getElementById('main');

		var arr = [];

		for (var i = 0; i < oTab.tBodies[0].rows.length; i++) {
			arr[i] = oTab.tBodies[0].rows[i];
		}
		arr.sort(function (tr1, tr2) {
			var n1 = status_dic[tr1.cells[4].innerHTML];
			var n2 = status_dic[tr2.cells[4].innerHTML];

			if (n1 - n2 != 0) {
				return n2 - n1;
			} else {
				var d1 = parseInt(tr1.cells[0].innerHTML);
				var d2 = parseInt(tr2.cells[0].innerHTML);
				return d1 - d2;
			}
		});
		for (var i = 0; i < arr.length; i++) {
			oTab.tBodies[0].appendChild(arr[i]);
		}
	}

	initialRanking();
	ReLoadDate();


	var AddActive = document.querySelector('#ODSide');
	AddActive.className = 'active';
	//为啥这个不能用？   该死  看来我的jQuery 也得补课了   明白了，要加个[0]就可以了    嘻嘻嘻
	$('#Price')[0].onclick = function () {
		var oTab = document.getElementById('main');
		var arr = [];

		for (var i = 0; i < oTab.tBodies[0].rows.length; i++) {
			arr[i] = oTab.tBodies[0].rows[i];
		}
		arr.sort(function (tr1, tr2) {
			var n1 = parseInt(tr1.cells[3].innerHTML.slice(1));
			var n2 = parseInt(tr2.cells[3].innerHTML.slice(1));
			console.log(n1);

			return n2 - n1;
		});
		for (var i = 0; i < arr.length; i++) {
			oTab.tBodies[0].appendChild(arr[i]);
		}
	}

		var AddActive = document.querySelector('#ODSide');
		AddActive.className = 'active';
		//为啥这个不能用？   该死  看来我的jQuery 也得补课了   明白了，要加个[0]就可以了    嘻嘻嘻
		// {#$('#ChartSide').className = 'active';#}
		$('#Price')[0].onclick = function () {
			var oTab = document.getElementById('main');

			var arr = [];

			for (var i = 0; i < oTab.tBodies[0].rows.length; i++) {
				arr[i] = oTab.tBodies[0].rows[i];
			}
			arr.sort(function (tr1, tr2) {
				var n1 = parseInt(tr1.cells[3].innerHTML.slice(1));
				var n2 = parseInt(tr2.cells[3].innerHTML.slice(1));

				return n2 - n1;
			});
			for (var i = 0; i < arr.length; i++) {
				oTab.tBodies[0].appendChild(arr[i]);
			}
		}

		$('#Oid')[0].onclick = function () {
			var oTab = document.getElementById('main');

			var arr = [];

			for (var i = 0; i < oTab.tBodies[0].rows.length; i++) {
				arr[i] = oTab.tBodies[0].rows[i];
			}
			arr.sort(function (tr1, tr2) {
				var n1 = parseInt(tr1.cells[0].innerHTML);
				var n2 = parseInt(tr2.cells[0].innerHTML);

				return n1 - n2;
			});
			for (var i = 0; i < arr.length; i++) {
				oTab.tBodies[0].appendChild(arr[i]);
			}
		}


		$('#Datetime')[0].onclick = function () {
			var oTab = document.getElementById('main');

			var arr = [];

			for (var i = 0; i < oTab.tBodies[0].rows.length; i++) {
				arr[i] = oTab.tBodies[0].rows[i];
			}
			arr.sort(function (tr1, tr2) {
				var d1 = new Date(tr1.cells[1].innerHTML);
				var d2 = new Date(tr2.cells[1].innerHTML);
				// console.log(d1);
				return d1 - d2;
			});
			for (var i = 0; i < arr.length; i++) {
				oTab.tBodies[0].appendChild(arr[i]);
			}
		}


		$('#status')[0].onclick = function () {
			var oTab = document.getElementById('main');

			var arr = [];

			for (var i = 0; i < oTab.tBodies[0].rows.length; i++) {
				arr[i] = oTab.tBodies[0].rows[i];
			}
			arr.sort(function (tr1, tr2) {
				var n1 = status_dic[tr1.cells[4].innerHTML];
				var n2 = status_dic[tr2.cells[4].innerHTML];

				if (n1 - n2 != 0) {
					return n2 - n1;
				} else {
					var d1 = new Date(tr1.cells[1].innerHTML);
					var d2 = new Date(tr2.cells[1].innerHTML);
					return d1 - d2;
				}
			});
			for (var i = 0; i < arr.length; i++) {
				oTab.tBodies[0].appendChild(arr[i]);
			}
		}


	
	$('.data-table').dataTable({
		"bJQueryUI": true,
		"sPaginationType": "full_numbers",
		"sDom": '<""l>t<"F"fp>'
	});
	
	$('input[type=checkbox],input[type=radio],input[type=file]').uniform();
	
	$('select').select2();
	
	$("span.icon input:checkbox, th input:checkbox").click(function() {
		var checkedStatus = this.checked;
		var checkbox = $(this).parents('.widget-box').find('tr td:first-child input:checkbox');		
		checkbox.each(function() {
			this.checked = checkedStatus;
			if (checkedStatus == this.checked) {
				$(this).closest('.checker > span').removeClass('checked');
			}
			if (this.checked) {
				$(this).closest('.checker > span').addClass('checked');
			}
		});
	});	
});
