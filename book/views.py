from django.shortcuts import render

# Create your views here.
from .models import Book, Novel, News
def index(request):
	return render(request, "book/index.html")

def education(request):
	context = {
		'eposts':Book.objects.order_by('-uploaded_time')
	}
	return render(request, "book/education.html", context)

def novels(request):
	context = {
		'nposts': Novel.objects.order_by('-noveluploaded_time')
	}
	return render(request, "book/novels.html", context)

def news(request):
	context = {
		'newposts': News.objects.order_by('-newsuploaded_time')
	}
	return render(request, "book/news.html", context)