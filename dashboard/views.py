from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dashboard.forms import DatasetForm

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import json

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
			dataset.save()
	else:
		dataset_form = DatasetForm()
	return render(request, 'dashboard/upload.html', {'dataset_form':dataset_form})

