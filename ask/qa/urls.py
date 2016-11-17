from django.conf.urls import url
from ask.qa.views import question, popular_questions, index

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^question/(?P<pk>\d+)/', question, name='question'),
    url(r'^popular/', popular_questions, name='popular_questions'),
]
