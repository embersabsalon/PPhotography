from django.shortcuts import render
from .models import Photo, Photographer
from django.db.models import Max


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
    photoid = requests.GET.get('photoid',None)
    likes = 0
    if (photoid):
        pic = Photo.objects.get(id = int(photoid))
        if pic is not None:
            likes = photoid.likes + 1
            pic.likes = likes
            pic.save
    
    return HttpResponse(likes)