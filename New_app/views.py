from django.shortcuts import render, redirect
from New_app.models import Todo_content
from New_app.forms import TodoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up(request):
    user = None
    Error_message = None
    if request.POST:
        u_name = request.POST['username']
        p_word = request.POST['password']
        e_mail = request.POST['email']
        try:
            user = User.objects.create_user(username = u_name, password = p_word, email = e_mail)
            return redirect('login')
        except Exception as e:
            Error_message = str(e)
    return render(request, 'signup.html', {'user':user, 'error_message':Error_message})

def login_view(request):
    error_message = None
    if request.POST:
        n_name = request.POST.get('username')
        e_mail = request.POST.get('email')
        p_word = request.POST.get('password') 
        user = authenticate(username = n_name, email = e_mail, password = p_word)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid data!!!"
    return render(request, 'login.html', {'error_message':error_message})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    todo = Todo_content.objects.all()
    return render(request, 'index.html', {'todo' : todo})

def add_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print("Invalid data")
            return redirect('delete_view')
    form = TodoForm()
    return render(request, 'add.html', {'form' : form})

def update_view(request, id):
    form = Todo_content.objects.get(id = id)
    return render(request, 'update.html', {'form':form})

def update_record(request, id):
    form = Todo_content.objects.get(id = id)
    form.Todo_title = request.POST['title']
    form.Todo_description = request.POST['description']
    form.Todo_status = request.POST['status']
    form.save()
    return redirect('home')

def delete_view(request, id):
    form = Todo_content.objects.get(id=id)
    form.delete()
    return redirect('home')

def delete_page(request, id):
    form = Todo_content.objects.get(id=id)
    return render(request, 'delete.html', {'form': form})
