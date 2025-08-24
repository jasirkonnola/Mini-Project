from django.contrib import admin
from django.urls import path, include
from eduUsers import views as user_view
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('edubase.urls', 'edubase'), namespace='edubase')), 

    
    path('register/', user_view.register, name='register'),
    path('login/', LoginView.as_view(template_name='eduUsers/login.html'), name='login'),
    path('logout/', user_view.logout_view, name='logout'),

    #profile_system
    path('profile/', user_view.profile, name='profile'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    