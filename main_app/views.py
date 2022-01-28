import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .forms import KitForm, StrategyForm, UserForm, StateForm
import uuid
import boto3
from .models import CustomUser, Strategy, Kit, State, Photo
User = get_user_model()
# Create your views here.
def home(request):
    return render(request, 'home.html')

def kits_index(request):
    kits = Kit.objects.all()
    states = State.objects.all()
    google_api_key = os.environ['GOOGLE_API_KEY']
    state_form = StateForm()
    return render(request, 'covidtracker/index.html', {
            'kits': kits, 
            'states': states, 
            'google_api_key': google_api_key,
            'state_form': state_form 
        })

def strategies_index(request):
    strategies = Strategy.objects.all()
    return render(request, 'main_app/strategies_index.html', { 'strategies': strategies })
def strategies_detail(request, strategy_id):
    strategy = Strategy.objects.get(id=strategy_id)
    return render(request,'main_app/strategies_detail.html', {'strategy': strategy})
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
          
            user = form.save()
            login(request, user)
            return redirect('kits_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def add_state(request, user_id):
    user = User.objects.filter(id = user_id)[0]
    user.state = State.objects.filter(id = request.POST['state']).first()
    user.save()
    return redirect('kits_index')

class StrategyCreate(CreateView):
    model = Strategy
    fields = '__all__'
    success_url = '/strategies/'
class StrategyUpdate(UpdateView):
    model = Strategy
    fields = ['rating', 'type']
    
class StrategyDelete(DeleteView):
    model = Strategy
    success_url = '/strategies/'
    
# @login_required
def kits_detail(request, kit_id):
    if request.user.kit_set.filter(id=kit_id).exists():
        kits = Kit.objects.get(id=kit_id)
        return render(request, 'kits/detail.html')
@login_required
def create_kit(request, user_id):
    form = KitForm(request.POST)
    if form.is_valid():
        new_kit = form.save(commit=False)
        new_kit.user_id = user_id
        new_kit.save()
    return redirect('detail', user_id=user_id)
def add_photo(request, strategy_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, strategy_id=strategy_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('strategies_detail', strategy_id=strategy_id)
    
class KitCreate (LoginRequiredMixin, CreateView):
    model = Kit
    fields = '__all__'
    success_url = '/kits_index/'

class KitDetail(LoginRequiredMixin, DetailView):
    model = Kit
class KitUpdate(LoginRequiredMixin, UpdateView):
    model = Kit
    fields = '__all__'
class KitDelete(LoginRequiredMixin, DeleteView):
    model = Kit
    success_url = '/kits_index/'
def some_function(request):
    secret_key = os.environ['SECRET_KEY']