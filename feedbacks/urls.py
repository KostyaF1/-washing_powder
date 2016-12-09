from django.conf.urls import patterns, include, url
from feedbacks import views

urlpatterns = patterns('',
    url(r'^$', views.FeedbackView.as_view(), name='feedback'),
    url(r'^$', views.CallOrderView.as_view(), name='call_order'),
)
