from django.shortcuts import render, redirect
from . forms import DocumentForm
from .models import Document
from .model import Finder
import numpy as np

def index(request):
    documents = Document.objects.all()
    return render(request, 'object/index.html', {'documents': documents})


def responses(request):
    print("hi")
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image = Document.objects.filter().latest('uploaded_at')
            rel_path = image.document.name
            act_path = "media/" + str(rel_path)
            object_detector = Finder(act_path)
            ans = object_detector.predict()
            return render(request, 'object/predict.html', {'id': ans})
    else:
        form = DocumentForm()
    return render(request, 'object/responses.html', {
        'form': form
    })

