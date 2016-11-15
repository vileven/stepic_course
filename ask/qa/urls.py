from django.conf.urls import url
from qa.views import test

urlpatterns = [
	url(r'^$', test),
	url(r'^question/(?P<pk>\d+)', test),
	url(r'^login/', test),
	url(r'^ask/', test),
	url(r'^popular/', test),
	url(r'^new/', test)
]

'''
	url(r'^$', question_list, name='question_list'),
    url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
    url(r'^popular/', popular, name='popular'),
    url(r'^ask/', question_ask, name='question_ask'),
    url(r'^answer/', question_answer, name='question_answ
'''