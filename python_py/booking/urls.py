from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # For login

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin
    path('movies/', include('movies.urls')),  # Routes for the `movies` app
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login page
]
