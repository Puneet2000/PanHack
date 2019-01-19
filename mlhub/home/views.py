from django.shortcuts import render
from home.models import ResearchPost
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def research(request):
    allposts = ResearchPost.objects.all()
    return render(request,'home/research.html',{'posts': allposts})
