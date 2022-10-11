from django.urls import path
from . import views

app_name='app_urls'

urlpatterns = [
	# path('userdata/',views.userdata,name='userdata'),
	# path('ajax_proc_first/',views.ajax_proc_first,name='ajax_proc_first'),
	# path('ajax_proc_after/',views.ajax_proc_after,name='ajax_proc_after'),
	# トップページ
	path('v1/',views.input_v1,name='input'),
	# チャット取得
	path('ajax_proc_aa/',views.ajax_proc_test01,name='ajax_proc_aa'),
	# プレビュー、範囲選択
	path('chat_data/',views.ajax_proc_dd,name='ajax_proc_dd'),
]