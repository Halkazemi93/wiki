from django.shortcuts import render
from .models import Page


def page_list(request):
	context = {
		"title": Page.objects.all(),
	}
	return render(request, 'list.html', context)


def page_detail(request, page_id):
	context = {
		"title": Page.objects.get(id=page_id),
	}
	return render(request, 'detail.html', context)
# Create your views here.
