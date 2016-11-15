from django.conf.urls import url
from qa.views import test

urlpatterns = [
	url(r'^$', test),
	url(r'^question/(?P<pk>\d+)/', test),
	url(r'^login/', test),
	url(r'^ask/', test),
	url(r'^popular/', test),
	url(r'^new/', test),
	url(r'^signup/',test),
]
