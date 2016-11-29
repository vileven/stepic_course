from django.conf.urls import url
from qa.views import question, popular_questions, index, ask_question, \
                                    question_answer,user_signup,user_login,user_logout

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^question/(?P<pk>\d+)/', question, name='question'),
    url(r'^popular/', popular_questions, name='popular_questions'),
    url(r'^ask/', ask_question, name='ask_question'),
    url(r'^answer/', question_answer, name='question_answer'),
    url(r'^signup/', user_signup, name='signup'),
    url(r'^login/', user_login, name='login'),
    url(r'^logout/', user_logout, name='logout'),
]
