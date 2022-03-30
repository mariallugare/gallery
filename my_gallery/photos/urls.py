from django.urls import path,include
from photos import views


urlpatterns =[

    path('',views.gallery,name='gallery',),
    path('photos/<int:id>/',views.viewPhoto,name='photo',),
    path('add/',views.addPhoto,name='add',)
]