import email
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import paycheck, worker
from .models import User, Profile
from .forms import SignUpForm, LoginForm, EditProfileForm
from core.models import invites


def signup(request):
    if request.user.is_authenticated:
        return redirect('core:home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    #    is_private = request.GET['full_name']


        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "Congratulations, you are now a registered user!")
            is_private = request.POST['is_private']
            is_privates = request.POST['PHONE']
            is_invite = request.POST['inviter']

            try:
             save_ = invites(user_mail=is_invite,inviter_mail=is_invite)
             save_.save()
            except:
                pass
                
            try:
             numbers = User.objects.get(id=request.user.id)
             numbers.number = is_private
             numbers.phone = is_privates
             numbers.save()
            except:
                pass
            #return render('http://127.0.0.1/')
        else:
             form = SignUpForm()
          #   messages.success(request, "")
             messages.success(request, 'Username is already taken.')
             mess = 'Change username or password.'
             return render(request, 'users/signup.html', {'form': form})
             
        return redirect('core:home')

    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def log_in(request):
    if request.user.is_authenticated:
        return redirect('core:home')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
         email = form.cleaned_data["email"]
         password = form.cleaned_data["password"]
         if "@" in email:
            email = form.cleaned_data["email"]  
             # print(email)1wwwwwwwwwwwwwwws
            password = form.cleaned_data["password"]
            # We check if the data is correct
            user = authenticate(email=email, password=password)
            if user:  # If the returned object is not None
                login(request, user)  # we connect the user
                return redirect('core:home')
            else:  # otherwise an error will be displayed
                messages.error(request, 'Invalid email or password')
         else:
            # is_privates = request.POST['email']
          #   password2 = request.POST['password']
            user = authenticate(email=email+'@gmail.com', password=password)
           # print('mmmmuuu')
            if user:  # If the returned object is not None
                login(request, user)  # we connect the user
                return redirect('core:home')
        else:
         print('ggggggg')
    else:
     form = LoginForm()
    messages.error(request, 'Log in with valid credentials')
    return render(request, 'users/login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect(reverse('users:login'))


@login_required
def profile(request, username):
    current_user = request.user.email
    number = invites.objects.filter(inviter_mail=request.user.email).count()
    print(number)
    if worker.objects.filter(email=current_user).exists():
        wages = paycheck.objects.get(reciver=current_user)
        pass_wages = wages.money
        money = float(pass_wages)
        two = round(money,3)
        name = 'welcome worker'
    else:
        two = ''
        name = ''
   
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user) 
    return render(request, 'users/profile.html', {'profile': profile,'invites':number, 'user': user,'wage':two,'name':name})

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.user.username,
                               request.POST, request.FILES)
        if form.is_valid():
            about_me = form.cleaned_data["about_me"]
            username = form.cleaned_data["username"]
            image = form.cleaned_data["image"]

            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            user.username = username
            user.save()
            profile.about_me = about_me
            if image:
                profile.image = image
            profile.save()
            return redirect("users:profile", username=user.username)
    else:
        form = EditProfileForm(request.user.username)
    return render(request, "users/edit_profile.html", {'form': form})


