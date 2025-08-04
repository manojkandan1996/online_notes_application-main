from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from notes import views as notes_views  # Your app views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth system
    path('accounts/register/', notes_views.register_view, name='register'),
    path('accounts/login/', notes_views.CustomLoginView.as_view(), name='login'),
    
    # ✅ Use Django's LogoutView safely
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Notes App URLs
    path('', notes_views.dashboard, name='dashboard'),
    path('notes/', notes_views.NoteListView.as_view(), name='note_list'),
    path('notes/create/', notes_views.NoteCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>/update/', notes_views.NoteUpdateView.as_view(), name='note_update'),
    path('notes/<int:pk>/delete/', notes_views.NoteDeleteView.as_view(), name='note_delete'),
]
