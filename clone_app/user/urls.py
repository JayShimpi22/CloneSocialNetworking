from django.urls import path
from django.contrib.auth.decorators import login_required
from user import views

urlpatterns = [
    path('in/<str:username>/',login_required(views.ProfileView.as_view()),name = 'profile_view'),
    path('in/<str:username>/edit',login_required(views.ProfileEditView.as_view()),name = 'profile_edit_view'),
    path('profiles/',login_required(views.AllProfilesView.as_view()),name = 'all_profiles_view'),
]
