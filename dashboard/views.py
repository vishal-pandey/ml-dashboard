from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dashboard.forms import DatasetForm
from dashboard.models import Dataset

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import json



def sizeof_fmt(num, suffix='B'):
	for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
		if abs(num) < 1024.0:
			return "%3.1f %s%s" % (num, unit, suffix)
		num /= 1024.0
	return "%.1f%s%s" % (num, 'Yi', suffix)


@login_required
def index(request):
	return render(request, 'dashboard/index.html')

@login_required
def upload_dataset(request):
	if request.method == 'POST':
		dataset_form = DatasetForm(request.POST, request.FILES)
		print("Hello")
		print(dataset_form.errors)
		if dataset_form.is_valid():
			print("Hi")
			dataset = dataset_form.save(commit=False)
			if 'dataset' in request.FILES:
				print('found it')
				dataset.user = request.user
				dataset.dataset = request.FILES['dataset']
				dataset.name = request.FILES['dataset']
				dataset.size = sizeof_fmt(request.FILES['dataset'].size)
			dataset.save()
			return HttpResponseRedirect(reverse('dashboard:list_dataset'))
	else:
		dataset_form = DatasetForm()
	return render(request, 'dashboard/upload.html', {'dataset_form':dataset_form})

@login_required
def list_dataset(request):
	datasets = Dataset.objects.all().filter(user = request.user)
	return render(request, 'dashboard/datasetlist.html', {'datasets': datasets})
	




