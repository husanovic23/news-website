from django.shortcuts import render
from requests import request
from .models import New
from django.views.generic import DetailView,ListView
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
    hamma=New.objects.order_by('-id')[0:5] 
    talim=New.objects.filter(position_id=5)
    uzb=New.objects.filter(position_id =3)
    xorij=New.objects.filter(position_id =2)
    narxoz=New.objects.filter(position_id =7) 
    context = {
        'hamma':hamma,
        'talim':talim,
        'uzb' : uzb,
        'xorijiy' : xorij,
        'narxoz':narxoz
    }

    # sport=New.objects.filter(position_id =5)
    return render(request,'index.html',context)

class BaseDetailview(DetailView):
    model=New
    template_name='detail_news.html'
    context_object_name='det_new'

class CategoryDetail(DetailView):
    model=New
    template_name='category_det.html'
    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        pk= self.kwargs['pk']
        context['category_news'] = New.objects.filter(position_id=pk)

        return context

from django.db.models import Q

class Serachview(ListView):
    model=New
    template_name='serach.html'

    def get_context_data(self, **kwargs):
        context = super(Serachview, self).get_context_data(**kwargs)
        text = self.request.GET.get('matn')
        context['serach_l'] = New.objects.filter(Q(position__title__icontains=text) | Q(news__icontains=text))
        return context