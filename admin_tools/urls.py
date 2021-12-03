from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('home/<str:category>', views.home, name='home'),
    path('logout/', views.logout_view, name='logout')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
