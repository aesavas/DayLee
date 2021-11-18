from django.shortcuts import render, redirect
from django.contrib import messages

from users.models import Profile
from users.utils import check_master_password

from .models import Diary
from .forms import DiaryCreationForm
from .utils import encrypt_diary, decrypt_diary

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
            diary.diary = encrypt_diary(request, diary.diary)
            diary.save()
            messages.success(request, 'Your diary has been added successfully and secretly !')
            return redirect('dashboard')
    context = {
        'form':form,
    }
    return render(request, 'diary/create_update_diary.html', context)

def update_diary_view(request, pk):
    profile = request.user.profile
    diary = profile.diary_set.get(id=pk)
    diary.diary = decrypt_diary(request, diary.diary)
    form = DiaryCreationForm(instance=diary)
    if request.method == "POST":
        form = DiaryCreationForm(request.POST, instance=diary)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.diary = encrypt_diary(request, diary.diary)
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


def detail_diary_view(request, pk):
    profile = request.user.profile
    diary = profile.diary_set.get(id=pk)
    diary.diary = decrypt_diary(request, diary.diary)
    context = {
        'diary': diary
    }
    return render(request, 'diary/detail_diary.html', context)