"""blogicum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

)
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
import django.contrib.auth.forms
from django.views.generic.edit import CreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('auth/login/', 
         LoginView.as_view(template_name='registration/login.html'), 
         name='login'),

    # Выход
    path('auth/logout/', 
         LogoutView.as_view(template_name='registration/logged_out.html'), 
         name='logout'),

    # Изменение пароля
    path('auth/password_change/', 
         PasswordChangeView.as_view(template_name='registration/password_change_form.html'), 
         name='password_change'),

    # Страница успешного изменения пароля
    path('auth/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('auth/password_reset/done/', PasswordResetDoneView.as_view(), name='password_change_done'),
    path('auth/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('auth/reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path(
        'auth/registration/', 
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=django.contrib.auth.forms.UserCreationForm,
            success_url=reverse_lazy('blog:index'),
        ),
        name='registration',
    ),
    path('edit/profile/', user_views.edit_profile, name='edit_profile'),
    path('logout/', LogoutView.as_view(template_name='logged_out.html'),
         name='logout',
     ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
handler403 = 'pages.views.csrf_error'