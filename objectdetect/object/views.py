from django.shortcuts import render, redirect
# from . forms import DocumentForm
    # from .models import Document
# from .model import Finder


# -*- coding: utf-8 -*-
from .forms import ProfileForm
from .models import QueryImage


def SaveImage(request):
    saved = False

    if request.method == "POST":
        # Get the posted form

        print(request.POST['name'])
        MyProfileForm = ProfileForm(request.POST, request.FILES)
        # print(MyProfileForm.errors)
        if MyProfileForm.is_valid():
            # name = request.POST['name_image']

            image = QueryImage(query_image=request.FILES['picture'], name = request.POST['name'])

            # image.uploaded_at = MyProfileForm.cleaned_data["uploaded_at"]
            image.save()
            saved = True
    else:
        MyProfileForm = ProfileForm()

    return render(request, 'object/saved.html', locals())

def upload(request):
    # documents = Document.objects.all()
    return render(request, 'object/upload_image.html')




