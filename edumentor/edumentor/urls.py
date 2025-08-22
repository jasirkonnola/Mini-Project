from django.contrib import admin
from django.urls import path, include
from eduUsers import views as user_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('edubase.urls', 'edubase'), namespace='edubase')), 

    
    path('register/', user_view.register, name='register'),
    path('login/', LoginView.as_view(template_name='eduUsers/login.html'), name='login'),
    path('logout/', user_view.logout, name='logout'),
]
