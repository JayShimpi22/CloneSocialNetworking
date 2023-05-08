from django.urls import include, path
from authentication import views
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordResetDoneView,PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


urlpatterns = [
    path('',views.SigninView.as_view(),name='signin_view'),
    path('signup/',views.SignupView.as_view(),name='signup_view'),
    path('signout/',views.SignoutView.as_view(),name='signout_view'),

    path('password/reset/',PasswordResetView.as_view(
    template_name = 'authentication/password_reset.html',
    email_template_name = 'authentication/password_reset_email.html'),
    name='password_reset'),

    path('password/reset/done/',PasswordResetDoneView.as_view(
    template_name = 'authentication/password_reset_done.html'
    ),name='password_reset_done'),

    path('password/reset/complete/',PasswordResetCompleteView.as_view(
    template_name = 'authentication/password_reset_complete.html'
    ),name='password_reset_complete'),

    path('password/reset/confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(
    template_name = 'authentication/password_reset_confirm.html'
    ),name='password_reset_confirm'),

    path('password/change/',PasswordChangeView.as_view(
        template_name = 'authentication/password_change.html',
        success_url = reverse_lazy('password_change_done_view')
    ),name='password_change_view'),

    path('password/change/done',PasswordChangeDoneView.as_view(
        template_name = 'authentication/password_change_done.html'
    ),name='password_change_done_view'),

    path('home_feed/',login_required(views.HomeView.as_view()),name='home_feed_view'),
]
 