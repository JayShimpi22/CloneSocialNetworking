from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from authentication.forms import UserForm
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.urls import reverse_lazy
from core.forms import PostCreateForm
from core.models import PostModel
# Create your views here.

class SignupView(View):
    template_name = 'authentication/signup.html'
    form_class = UserForm

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        context = {'form':form}
        return render(request,self.template_name,context)
        
        
class SigninView(View):
    template_name = 'authentication/signin.html'

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home_feed_view')
        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        email_username = request.POST.get('email_username')
        password = request.POST.get('password')
        User = get_user_model()
        
        try:
            user_obj = User.objects.get(username = email_username)
            email = user_obj.email
        except Exception as e:
            email = email_username
        
        user = authenticate(request,email=email,password=password)
        if user is None:
            # context = {'messages':['invalid details']}
            messages.error(request,"Invalid Details",extra_tags="error")
            return render(request,self.template_name)
        messages.success(request,"Thanks for Logging in!!",extra_tags="success")
        login(request,user)
        return redirect('home_feed_view')


class SignoutView(View):
    def post(self,request,*args,**kwargs):
        logout(request)
        return redirect('signin_view')

class HomeView(TemplateView):
    template_name = 'core/feed.html'
    form_class = PostCreateForm

    def get(self,request,*args,**kwargs):
        form = self.form_class()
        all_posts = PostModel.objects.all()

        context = {'form':form,'all_posts':all_posts}
        return render(request,self.template_name,context)


