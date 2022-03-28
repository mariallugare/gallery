from django.shortcuts import render
from .models import Category, Photo

# Create your views here.

def gallery(request):
    categories=Category.objects.all()
    photos = Photo.objects.all()
    context ={'categories':categories,'photos':photos}
    return render(request,'gallery.html',context)

def viewPhoto(request,*args, **kargs):
    photo_id=kargs.get('id')
    photo = Photo.objects.get(id= photo_id)
    # print(id)
    context ={'photo':photo}
    return render(request,'photo.html',context)


def addPhoto(request):
    def addPhoto(request):
     user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')


   
def location(request):
    return render(request,'location.html')

    
