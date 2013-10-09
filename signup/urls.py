from django.conf.urls import patterns, url
from signup import views

urlpatterns = patterns('',
    url(r'^$', views.SignupView.as_view(), name='form'),
    url(r'^post$', views.post, name='signup_post'),
    url(r'^questions$', views.QuestionsView.as_view(), name='questions'),
    url(r'&success$', views.success, name='success')
)
