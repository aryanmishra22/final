from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.home, name='home'),
     path('register', views.register, name='register'),
     path('login', views.login, name='login'),
     path('logout', views.logout, name='logout'),
     path('post', views.post, name='post'),
     path('profile/<username>', views.profile, name='profile'),
     path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)