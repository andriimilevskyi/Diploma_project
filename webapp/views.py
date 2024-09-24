from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
# myapp/views.py

class IndexView(TemplateView):
    template_name = 'web/index.html'

#
# def index(request):
#     return render(request, 'web/index.html')
