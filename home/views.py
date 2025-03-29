# Code from above
from django.http import HttpResponse
from django.contrib.auth.models import User as user
from django.contrib import messages
from home.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def index(request):
    register_form = RegisterForm()
    login_form = LoginForm()
    return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form})

# Registration view
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Account has been created successfully!! Please check your email to confirm your email address in order to activate your account.")
            return redirect('login')  # Redirect to login page
        else:
            return render(request, 'index.html', {'form': form, 'error': form.errors.as_text()})
    else:
        form = RegisterForm()  # Define the form for GET requests
        return render(request, 'index.html', {'form': form})  # No error message for GET

# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember']
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    if remember:
                        request.session.set_expiry(1209600)  # 2 weeks
                    else:
                        request.session.set_expiry(0)  # Expire on browser close
                    return redirect('index')
                else:
                    messages.error(request, 'Invalid email or password.')
            except User.DoesNotExist:
                messages.error(request, 'Invalid email or password.')
        else:
            return render(request, 'index.html', {'form': form, 'error': form.errors.as_text()})
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out...')
    return redirect('index')

def dashboard(request):
    return render(request, 'dashboard.html')