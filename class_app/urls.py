
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Booklistview.as_view(), name='booklist'),
    path('createview/',views.Bookcreateview.as_view(), name='createbook'),
    path('detailview/<int:pk>/',views.Bookdetailview.as_view(),name='details'),
    path('updateview/<int:pk>/',views.Bookupdateview.as_view(),name='update'),
    path('delete/<int:pk>/',views.Bookdeleteview.as_view(),name='delete'),
]
