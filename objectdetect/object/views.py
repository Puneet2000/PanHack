from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import QueryImage
from .models import Worker
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
import cv2
from .vgg import predict
# from .sentiment import predict_sentiment


def SaveImage(request):
    saved = False
    worker_name=""
    worker_email=""
    issue_id=0
    status=""

    if request.method == "POST":
        MyProfileForm = ProfileForm(request.POST, request.FILES)
        if MyProfileForm.is_valid():
            image = QueryImage(query_image=request.FILES['picture'], name = request.POST['name'],
                               long = request.POST['long'], lat = request.POST['lat'],
                               aadhar = request.POST['aadhar'] )
            image.save()

            read_image = cv2.imread('/home/jatin/codes/PanHack/objectdetect/media/' + str(image.query_image))
            confidence, _, image_type = predict(read_image)

            print("Image Type -> ", image_type)
            if image_type!="spam":
                image.category = image_type
                saved = True
                worker = Worker.objects.get(designation=image_type)
                worker_name = worker.name
                worker_email= worker.email
                image.confidence = confidence
                status = "pending"
                assign = Assigned(query=image,worker=worker,status=status)
                assign.save()
                image.save()
                issue_id = assign.id  # issue_id should be assignment id, for comments
                # print("image id ", image.id, " issue_id ", assign.id)

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
    images = sorted(images, key= lambda x: x.confidence, reverse=True)
    for i in images:
        print(i.confidence)
    return render(request, 'object/gov.html',
                    {'user_data': list(images)} )



def comments(request):
    comments = Assigned.objects.all()

    # # images = sorted(images, key= lambda x: x.confidence, reverse=True)
    # for i in images:
    #     print(i.confidence)
    return render(request, 'object/status_depend.html',
                    {'comment_data': list(comments)} )


def get_status(request, issue_id=30):
    saved=True
    image = QueryImage.objects.get(id=issue_id)
    assign = Assigned.objects.get(query=image)
    worker = assign.worker
    worker_name = worker.name
    issue_id = assign.id        # issue_id should be assignment id, for comments
    worker_email = worker.email
    status = assign.status
    image_category = image.category
    # print("image_category", image_category)
    return render(request, 'object/saved.html', locals())


def add_comments(request):
    return render(request, 'object/save_comments.html')

def save_comments(request):
    issue_id = request.POST['issue_id']
    current_comment = request.POST['comment']
    try:
        assign = Assigned.objects.get(id=issue_id)
    except:
        return HttpResponse('Invalid ID')
    # print("commented -> ", assign.logs)
    comments = assign.logs
    updated_comments = comments + '<->' + current_comment
    assign.logs = updated_comments
    assign.save()
    # print("updated comments -> ", assign.logs)
    # current_sentiment = predict_sentiment(assign.logs)
    # print("Current worker status, according to public reviews is ", assign.logs)

    return render(request, 'object/comments.html', locals())

    # response = HttpResponse('Comments successfully added')
    # return response


def worker_login(request):
    # documents = Document.objects.all()
    return render(request, 'object/worker_login.html')


def login(request):
    if request.method == 'GET':
        print(request.method)
        name = request.GET['username']
        # print(name)
        password = request.GET['password']
        print(name, password)
        obj = Worker.objects.filter(name = name, password = password)
        # print(len(obj))
        if len(obj) == 0:
            response = HttpResponse('Fail article activity update')
            return response
        else:
            response = HttpResponse('Success')
            return response


