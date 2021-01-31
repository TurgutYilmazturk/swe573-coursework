from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from . import models
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.

# Create your views here.

class AnalysisView(generic.TemplateView):

    template_name='analysis/analysis.html'

class HistoryView(generic.ListView):
    context_object_name='h_analysis'
    model=models.Analysis
