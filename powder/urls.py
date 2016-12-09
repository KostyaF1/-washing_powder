from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from powder import views
from feedbacks.views import FeedbackView, CallOrderView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'powder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^call_order/', CallOrderView.as_view(), name="call_order" ),
    url(r'^feedbacks/', FeedbackView.as_view(), name="feedback" ),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
