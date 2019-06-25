from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CheklistForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password, )
            login(request, user)
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def index(request):
    from task.models import Task
    from django.contrib.auth.models import User
    tasks = Task.objects.all()
    f_search = request.GET.get('task_name')
    f_percent_min = request.GET.get('int_min')
    f_percent_max = request.GET.get('int_max')
    f_free_task = request.GET.get('free')
    f_my_task = request.GET.get('my')
    if f_search:
        tasks = tasks.filter(title__icontains=f_search)
    if f_percent_min:
        tasks = tasks.filter(stasus_in_percents__gte=f_percent_min)
    if f_percent_max:
        tasks = tasks.filter(stasus_in_percents__lt=f_percent_max)
    if f_free_task == 'on':
        tasks = tasks.filter(doer=User.objects.all()[1])
    if f_my_task == 'on':
        tasks = tasks.filter(doer=request.user)
    return render(request, 'Html_templates/main_template.html', {'task': tasks, })

@login_required
def show_Class_Task(request, id):
    from .models import Task

    try:
        tasks = Task.objects.get(id=id)
        if request.method == 'POST':
            form = CheklistForm(request.POST)
            if form.is_valid():
                commit = form.save(commit=False)
                commit.task = tasks
                commit.save()
                return redirect('/task/'+ str(id))
        form = CheklistForm()
    except Task.DoesNotExist:
        return render(request, 'Html_templates/404.html')
    return render(request, 'Html_templates/show_tasks.html', {'task': tasks, 'cheklist': form})


@login_required
def add_ChekList(request, id,):
    from .forms import CheklistForm
    if request.method =='POST':
        form = CheklistForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/task/'+ str(id))

@login_required
def show_ChekList(request, id, id_chek_list):
    from .models import Cheklist
    chekList = Cheklist.objects.get(id=id_chek_list)
    print(not chekList.active)
    chekList.active = not chekList.active
    print(chekList.active)
    chekList.save()
    return redirect('/task/'+ str(id))

@login_required
def delete_CheckItem(request,id, id_chek_list):
    from .models import Cheklist
    chekList = Cheklist.objects.get(id=id_chek_list)
    chekList.delete()
    return redirect('/task/' + str(id))


@login_required
def confirm_Class_Task(request, id):
    from .models import Task
    task = Task.objects.get(id=id)
    task.doer = request.user
    task.save()
    return redirect('/')

@login_required
def edit_Class_Task(request, id):
    from .forms import TaskForm, CheklistForm
    from .models import Task
    task = Task.objects.get(id=id)
    if request.method =='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)
    return render(request, 'Html_templates/form_new_task.html', {'form': form, })

@login_required
def delete_task(request, id):
    from .models import Task
    instance = Task.objects.get(id=id)
    instance.delete()
    return redirect('/')

@login_required
def add_new_task(request):
    from .forms import TaskForm
    from django.contrib.auth.models import User
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            user = User.objects.all()
            task.doer = user[1] # FREE user which share tasks
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'Html_templates/form_new_task.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('/login')
    else:
        if request.user.is_authenticated:
            messages.warning(request, 'You already logged in')
            return redirect('/')
        form = UserRegisterForm()

    return render(request, 'registration/signup.html', {'form': form})

def reset_user(request):
    return render(request, 'registration/Reset_User.html')

class MyPasswordResetView(PasswordResetForm):
  def form_valid(self, form):
      opts = {
          'use_https': self.request.is_secure(),
          'token_generator': self.token_generator,
          'from_email': self.from_email,
          'email_template_name': self.email_template_name,
          'subject_template_name': self.subject_template_name,
          'request': self.request,
          'html_email_template_name': 'registration/password_reset_email.html',
          'extra_email_context': self.extra_email_context,
      }
      form.save(**opts)
      return HttpResponseRedirect(self.get_success_url())

def send_mail():
    pass
    #from django.core.mail import send_mail
    #send_mail('Subject here', 'Here is the message.', 'url5438.taskmanager_mailservice', ['deniszaharov19981208@gmail.com',], fail_silently=False)