
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from  django.conf.urls import url
from demo_app import views

urlpatterns =[
    url(r'^', views.Index),
]
#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
