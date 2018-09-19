from django.shortcuts import render
from .models import Photo, Photographer
from django.db.models import Max
from django.http import HttpResponse

# Create your views here.
def index(request):
    mostliked = Photo.objects.all().aggregate(Max('likes'))
    photos = Photo.objects.filter(likes = mostliked.get('likes__max'))
    return render(request, 'index.html', {'photos' : photos})

    
def photography(request):
    photos = Photo.objects.all()
    return render(request, 'photography.html', {'photos' : photos})

def photographers(request):
    photographers = Photographer.objects.all()
    return render(request, 'photographers.html', {'photographers' : photographers})

def like_photo(request):
    photoide = request.GET.get('photoid',None)
    likes = 0
    if (photoide):
        pic = Photo.objects.get(photoid = int(photoide))
        print(pic)
        if pic is not None:
            likes = pic.likes + 1
            print(pic.likes + 1)
            pic.likes = likes
            pic.save()
    
    return HttpResponse(likes)