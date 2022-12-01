from django.shortcuts import render
from requests import request
from .models import New
from django.views.generic import DetailView
# Create your views here.
def base(request):
    return render(request,'index.html')
def category(request):
    return render(request,'category.html')
def contact(request):
    return render(request,'contact.html')
def single(request):
    return render(request,'single.html')

def main(request):
    a=New.objects.all()
    tibbiyot=New.objects.order_by('-id')[0:5] 
    talim=New.objects.filter(position_id=5)
    uzb=New.objects.filter(position_id =3)
    xorij=New.objects.filter(position_id =4)
    
    context = {
        'tibbiyot':tibbiyot,
        'talim':talim,
        'uzb' : uzb,
        'xorijiy' : xorij
    }

    # sport=New.objects.filter(position_id =5)
    return render(request,'index.html',context)

class BaseDetailview(DetailView):
    model=New
    template_name='detail_news.html'
    context_object_name='det_new'



