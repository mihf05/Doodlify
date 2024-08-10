from django.shortcuts import render
from .models import PostDoodle
from .forms import PostDoodleForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import FileResponse, Http404
from django.conf import settings
import os

# Create your views here.
def home(request):
    return render(request, 'illustrations/index.html')

def artists(request):
    return render(request, 'illustrations/artists.html')

def contact(request):
    return render(request, 'illustrations/contact.html')

def illustrations(request):
    post_doodle = PostDoodle.objects.all()
    return render(request, 'illustrations/illustrations.html', {'post_doodle': post_doodle})

@login_required
def create_doodle(request):
    if request.method == "POST":
        form = PostDoodleForm(request.POST, request.FILES)
        if form.is_valid():
            post_doodle = form.save(commit=False)
            post_doodle.user = request.user
            post_doodle.save()
            return redirect('illustrations')
    else:
        form = PostDoodleForm()
    return render(request, 'illustrations/create_doodle.html', {'form': form})

@login_required
def delete_doodle(request, doodle_id):
    post_doodle = get_object_or_404(PostDoodle, pk=doodle_id, user=request.user)
    if request.method == "POST":
        post_doodle.delete()
        return redirect('illustrations')
    return render(request, 'illustrations/doodle_confirm_delete.html', {'post_doodle': post_doodle})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
def serve_image(request, image_name):
    file_path = os.path.join(settings.MEDIA_ROOT, 'photos', image_name)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='image/jpeg')
    raise Http404("Image does not exist")
