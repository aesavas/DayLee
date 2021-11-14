from django.shortcuts import render, redirect
from django.contrib import messages

from users.models import Profile
from .models import Diary
from .forms import DiaryCreationForm

def landing_page_view(request):
    return render(request, 'index.html')


def dashboard_view(request):
    profile = request.user.profile
    diaries = profile.diary_set.all()
    moods = {
        'happy' : diaries.filter(mood="happy").count(),
        'sad' : diaries.filter(mood="sad").count(),
        'angry' : diaries.filter(mood="angry").count(),
        'total' : diaries.count()
    }
    context = {
        'profile':profile,
        'diaries':diaries,
        'moods' :moods
    }
    return render(request, 'diary/dashboard.html', context)


def create_diary_view(request):
    form = DiaryCreationForm()
    if request.method == "POST":
        form = DiaryCreationForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.owner = request.user.profile
            diary.save()
            messages.success(request, 'Your diary has been added successfully !')
            return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request, 'diary/create_update_diary.html', context)

def update_diary_view(request, pk):
    profile = request.user.profile
    diary = profile.diary_set.get(id=pk)
    form = DiaryCreationForm(instance=diary)
    if request.method == "POST":
        form = DiaryCreationForm(request.POST, instance=diary)
        if form.is_valid():
            form.save()
            messages.success(request, 'Diary was updated successfully!')
            return redirect('dashboard')
    context = {
        'form':form,
    }
    return render(request, 'diary/create_update_diary.html', context)

def delete_diary_view(request, pk):
    profile = request.user.profile
    diary = profile.diary_set.get(id=pk)
    if request.method == "POST":
        diary.delete()
        messages.success(request, 'Diary was deleted successfully !')
        return redirect('dashboard')
    context = {
        'diary':diary
    }
    return render(request, 'diary/delete-diary.html', context)