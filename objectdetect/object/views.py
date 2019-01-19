from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import QueryImage
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
import logging
import json
from PIL import Image

def SaveImage(request):
    saved = False
    worker_name=""
    worker_email=""
    issue_id=0
    status=""

    if request.method == "POST":
        MyProfileForm = ProfileForm(request.POST, request.FILES)
        if MyProfileForm.is_valid():
            image = QueryImage(query_image=request.FILES['picture'], name = request.POST['name'], long = request.POST['long'], lat = request.POST['lat'], aadhar = request.POST['aadhar'] )
            image.save()
            """
            read_image = cv2.imread('/home/puneet/PanHack/objectdetect/media/' + str(image.query_image))
            confidence, _, image_type = predict(read_image)
            """
            image_type="garbage"
            if image_type!="spam":
                image.category = image_type
                saved = True
                worker = Worker.objects.get(designation=image_type)
                worker_name = worker.name
                issue_id= image.id
                worker_email= worker.email
                status = "pending"
                assign = Assigned(query=image,worker=worker)
                assign.save()
                image.save()

            else:
                image.delete()
                saved = False


    else:
        MyProfileForm = ProfileForm()
    return render(request, 'object/saved.html', locals())

def upload(request):
    # documents = Document.objects.all()
    return render(request, 'object/upload_image.html')


def welcome(request):

    images = QueryImage.objects.all()
    return render(request, 'object/gov.html',
                    {
                    'user_data': list(images)
                    })


def get_status(request,issue_id=30):
    saved=True
    image = QueryImage.objects.get(id=issue_id)
    assign = Assigned.objects.get(query=image)
    worker = assign.worker
    worker_name = worker.name
    issue_id = image.id
    worker_email = worker.email
    status = "pending"
    return render(request, 'object/saved.html', locals())