from django.shortcuts import render
from .models import Photo, Photographer
from django.db.models import Max
from django.http import HttpResponse

# Create your views here.
def index(request):
    mostliked = Photo.objects.all().aggregate(Max('likes'))
    mostrecent = Photo.objects.all().aggregate(Max('photoid'))
    likedphotos = Photo.objects.filter(likes = mostliked.get('likes__max'))
    recentphotos = Photo.objects.filter(photoid = mostrecent.get('photoid__max'))
    print("Liked: ",likedphotos)
    print("Recent: ",recentphotos)
    print("Returned ", {'likedphotos' : likedphotos , 'recentphotos' : recentphotos})
    return render(request, 'index.html', {'likedphotos' : likedphotos , 'recentphotos' : recentphotos})

    
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