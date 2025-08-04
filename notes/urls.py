from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from notes import views as note_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', note_views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', note_views.dashboard, name='dashboard'),
    path('note/create/', note_views.note_create, name='note_create'),
    path('note/<int:pk>/edit/', note_views.note_update, name='note_update'),
    path('note/<int:pk>/delete/', note_views.note_delete, name='note_delete'),
]
