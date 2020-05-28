from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login 
from .models import Company
from .forms import CompanyForm



# Create your views here.
@login_required
def index(request):
    companies = Company.objects.filter(user__username__exact=request.user)
    return render(request, 'main_page/index.html',{'companies':companies})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # ユーザーインスタンスを作成
        if form.is_valid():
            new_user = form.save() # ユーザーインスタンスを保存
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            # フォームの入力値で認証できればユーザーオブジェクト、できなければNoneを返す
            new_user = authenticate(username=input_username, password=input_password)
            # 認証成功時のみ、ユーザーをログインさせる
            if new_user is not None:
                # loginメソッドは、認証ができてなくてもログインさせることができる。→上のauthenticateで認証を実行する
                login(request, new_user)
                return redirect('main_page:index')
    else:
        form = UserCreationForm()
    return render(request, 'main_page/signup.html', {'form': form})
    
def done(request):
    return render(request, 'main_page/logout.html')


@login_required
def company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect('main_page:company_detail',pk=company.pk)
    else:
        form = CompanyForm()
    return render(request, 'main_page/company.html', {'form': form})


@login_required
def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect('main_page:company_detail', pk=company.pk)
    else:
        form = CompanyForm(instance=company)
    return render(request, 'main_page/company.html', {'form': form})



@login_required
def company_detail(request,pk):
    user = request.user
    companies = get_object_or_404(Company,pk=pk)
    username = user.username
    return render(request, 'main_page/company_detail.html', {'user':user,'companies':companies})


@login_required
def company_delete(request,pk):
    try:
        company = get_object_or_404(Company, pk=pk)
    except models.Company.DoesNotExist:
        raise Http404
    company.delete()
    return redirect('main_page:index')


def delete_comfirm(request,pk):
    user = request.user
    companies = get_object_or_404(Company, pk=pk)
    return render(request, 'main_page/delete_comfirm.html',{'companies':companies})



