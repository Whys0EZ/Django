from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.http import Http404
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import User_List
# Create your views here.
@login_required
def main(request):
    mymember = Member.objects.all().order_by('-firstname').values()
    template = loader.get_template('index.html')
    # return HttpResponse("Hello Word!")
    context  = {
            'profiles':profile,
            'member': mymember
        }
    return HttpResponse(template.render(context,request))


def error(request, exception):
    return render(request, 'error.html', {'message': exception})

def serach_info(request):
    if request.method == 'POST':
        # form = SearchForm(request.POST)
        search_query = request.POST.get('search_query', '').strip()
        if search_query:
            results = User_List.objects.filter(username__icontains=search_query)
        else:
            results = User_List.objects.none()
        return render(request, 'search.html', {'query':search_query, 'results':results})
    else:
        return render(request, 'search.html')


def user_login(request):
    # form = LoginForm()
    # Nếu người dùng đã đăng nhập, chuyển hướng họ đến trang chủ
    if request.user.is_authenticated:
        return redirect('index')  # Hoặc trang mà bạn muốn chuyển hướng đến
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # username = request.POST['username']
            # password = request.POST['password']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate( username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
                # return HttpResponseRedirect('/')
            else:
                # Return an 'invalid login' error message.
                form.add_error(None, 'Tên người dùng hoặc mật khẩu không đúng.')
    else:
        form = LoginForm()
        
    return render(request,'login.html',{'form': form})
    # template = loader.get_template('login.html')
    # return HttpResponse(template.render())

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form': form})

def profile(request,id):
    try:
        profile = get_object_or_404(User,id=id)
        # template = loader.get_template('profile.html')
        context  = {
            'profiles':profile
        }
    except:
        raise Http404("Not Found !!!")
    # return HttpResponse(template.render(context, request))
    return render(request, 'profile.html', context)

def member(request):
    mymember = Member.objects.all().order_by('-firstname').values()
    template = loader.get_template('all_member.html')
    context  = {
        'mymembers': mymember,
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    try:

        mymember = Member.objects.get(id=id)
        template = loader.get_template('details.html')
        context  = {
            'mymember':mymember
        }
    except:
        raise Http404("Not Found !!!")
    return HttpResponse(template.render(context, request))
