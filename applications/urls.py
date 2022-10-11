from django.urls import path
from . import views

app_name='app_urls'

urlpatterns = [
	path('v1/',views.input_v1,name='input'),
	path('userdata/',views.userdata,name='userdata'),
	path('ajax_proc_first/',views.ajax_proc_first,name='ajax_proc_first'),
	path('ajax_proc_after/',views.ajax_proc_after,name='ajax_proc_after'),
	#
	path('ajax_proc_aaa/',views.ajax_proc_test01,name='ajax_proc_aaa'),
	#
	path('ajax_proc_dd/',views.ajax_proc_dd,name='ajax_proc_dd'),
]