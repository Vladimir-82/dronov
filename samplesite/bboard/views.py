from django.shortcuts import render

from .models import Bd

def index(request):
    bbs = Bd.objects.order_by('-published')
    content = {"bbs": bbs}
    return render(request, 'index.html', content)
