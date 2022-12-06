from .models import *


def extra(request):
    category = Position.objects.all()[:4]




    return {
        'category_sayt':category,
    }