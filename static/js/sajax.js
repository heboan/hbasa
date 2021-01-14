/**
 * Created by heboan on 2018/7/10.
 */
// 对jquery的ajax的封装

'use strict';

function getCookie(name) {
     var cookieValue = null;
     if (document.cookie && document.cookie != '') {
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
             var cookie = jQuery.trim(cookies[i]);
             // Does this cookie string begin with the name we want?
             if (cookie.substring(0, name.length + 1) == (name + '=')) {
                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                 break;
             }
         }
     }
     return cookieValue;
 };


var sajax = {
	'get':function(args) {
		args['method'] = 'get';
		this.ajax(args);
	},
	'post':function(args) {
		args['method'] = 'post';
		this.ajax(args);
	},
	'ajax':function(args) {
		// 设置csrftoken
		this._ajaxSetup();
		$.ajax(args);
	},
	'_ajaxSetup': function() {
		$.ajaxSetup({
			'beforeSend':function(xhr,settings) {
				if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"))
                }
			}
		});
	}
};