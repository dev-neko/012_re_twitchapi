// --------------------------------
// ---- Ajax前のおまじない start ----
// --------------------------------
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
	beforeSend: function (xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});
// --------------------------------
// ----- Ajax前のおまじない end -----
// --------------------------------



// --------------------------------
// ajax_form用ajax STR
// --------------------------------
// formの操作を検知する
// input→変化があり次第、submit→submitボタンが押され次第
$('#ajax_form').on('submit', function(e) {
	// フォーム送信の通信を止めるためにpreventDefault()を使用
	e.preventDefault();
	// 取得中はボタンを無効化する
	$("#run_btn").prop("disabled", true).text('取得中…');
	// サーバに送信するリクエストの設定
	$.ajax({
		// リクエストを送信するURLを指定
		// propメソッドを用いればformの内容を引き継げるのでjsを外部に設置可能
		'url': $('#ajax_form').prop("action"),
		// HTTPメソッドのGET通信かPOST通信を指定
		'method': $('#ajax_form').prop("method"),
		// サーバに送信するデータの指定
		'data': {
			'videoids':$('#videoids').val(),
		},
		// データ形式(ここではjson)を指定
		'dataType': 'json'
	})
	// 通信成功時の処理
	// views.pyから受け取ったJSONデータをページに表示
	.done(function(response){
		// append→後ろに追加、prepend→前に追加、replaceWith→置換
		// 取得中の欄
		$('#result_table tbody').replaceWith('<tbody><tr><td>'+response.videoids+'</td><td><div class="progress"><div class="progress-bar progress-bar-striped progress-bar-animated" style="width:'+response.progress+'%" role="progressbar" aria-valuenow="'+response.progress+'" aria-valuemin="0" aria-valuemax="100">'+response.progress+'%</div></div></td></tr></tbody>');
		// トークン
		$('#next_token').replaceWith('<input type="hidden" id="next_token" class="form-control" value="'+response.next_token+'">');
		// 再帰呼び出し
		//after_ajax(response.videoids,response.next_token,response.video_length,response.ts_chat_dist);
		after_ajax(response.videoids,response.next_token,response.video_length);
	})
	// 通信失敗時の処理
	.fail(function(){
		window.alert("error");
	});
});

// ajaxを自分で呼び出して再帰的に実行する
//function after_ajax(videoids,next_token,video_length,ts_chat_dist){
function after_ajax(videoids,next_token,video_length){
	// フォーム送信の通信を止めるためにpreventDefault()を使用
	// e.preventDefault();
	// サーバに送信するリクエストの設定
	$.ajax({
		// リクエストを送信するURLを指定
		// propメソッドを用いればformの内容を引き継げるのでjsを外部に設置可能
		'url': $('#ajax_form').prop("action"),
		// HTTPメソッドのGET通信かPOST通信を指定
		'method': $('#ajax_form').prop("method"),
		// サーバに送信するデータの指定
		'data': {
			'videoids':videoids,
			'next_token':next_token,
			'video_length':video_length,
			//'ts_chat_dist':ts_chat_dist,
		},
		// データ形式(ここではjson)を指定
		'dataType': 'json'
	})
	// 通信成功時の処理
	// views.pyから受け取ったJSONデータをページに表示
	.done(function(response){
		// append→後ろに追加、prepend→前に追加、replaceWith→置換
		// 取得中の欄
		$('#result_table tbody').replaceWith('<tbody><tr><td>'+response.videoids+'</td><td><div class="progress"><div class="progress-bar progress-bar-striped progress-bar-animated" style="width:'+response.progress+'%" role="progressbar" aria-valuenow="'+response.progress+'" aria-valuemin="0" aria-valuemax="100">'+response.progress+'%</div></div></td></tr></tbody>');
		// トークン
		$('#next_token').replaceWith('<input type="hidden" id="next_token" class="form-control" value="'+response.next_token+'">');
		// next_tokenがNoneでなければ再帰呼び出し
		if (response.next_token != 'None') {
			//after_ajax(response.videoids,response.next_token,response.video_length,response.ts_chat_dist);
			after_ajax(response.videoids,response.next_token,response.video_length);
		// next_tokenがNoneならプログレスバーを100%にして終了
		} else {
			// 更新が速すぎて99%とかが見れないので少しスリープ→機能しないようなので保留
			// setTimeout(function(){},1000);
			$('#result_table tbody').replaceWith('<tbody><tr><td>'+response.videoids+'</td><td><div class="progress"><div class="progress-bar progress-bar-striped progress-bar-animated" style="width:100%" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">100%</div></div></td></tr></tbody>');
			// リロードする
			location.reload();
		}
	})
	// 通信失敗時の処理
	.fail(function(){
		window.alert("error");
	});
}
// --------------------------------
// ajax_form用ajax END
// --------------------------------



// --------------------------------
// ajax_dd_form用ajax STR
// --------------------------------
// input→変化があり次第、submit→submitボタンが押され次第、ボタンIDを直接指定する場合はclick、
$('#db_action_delete').on('click', function(e) {
	e.preventDefault();

	// チェックされている値を配列に格納
	// https://agohack.com/getting-checkbox-with-map-and-each-in-jquery/
	var videoids = $('[name="videoids"]:checked').map(function(){
		// 値を返す
		return $(this).val();
	// オブジェクトを配列に変換するメソッド
	}).get();

	$.ajax({
		'url': $('#ajax_dd_form').prop("action"),
		'method': $('#ajax_dd_form').prop("method"),
		'data': {
			'videoids':videoids,
			'db_action':'delete',
		},
		'dataType': 'json'
	})
	// 通信成功時の処理
	.done(function(response){
		//videoidでループして要素を削除する
		$(response.videoids).each(function(index,value){
			$("#"+value+"_div").remove();
		});
	})
	.fail(function(){
		window.alert("error");
	});
});
// --------------------------------
// ajax_dd_form用ajax END
// --------------------------------

//form内のinput hiddenの内容をボタンごとに書き換えてsubmitすることでajaxでもボタンによって処理を分けられる
//https://technote925.com/106
//ボタンが複数ある場合は不明
//$(function(){
//	$('#db_action_save').click(function() {
//		$('#db_action').attr('value', 'save');
//		$('#ajax_dd_form').submit();
//	});
//	$('#db_action_delete').click(function() {
//		$('#db_action').attr('value', 'delete');
//		$('#ajax_dd_form').submit();
//	});
//});
