from django.urls import path
from .views import ArtisteCreate, ArtisteDelete, ArtisteDetail, ArtisteList, ArtisteUpdate, MorceauDetail, MorceauList, MorceauCreate, MorceauUpdate, MorceauDelete, morceau_detail
from musiques import views

#app_name = 'musiques' # Encapsule les urls de ce module dans le namespace musique

urlpatterns = [
    path('morceaux', MorceauList.as_view(), name='morceaux'),
    path('morceau/<int:pk>', MorceauDetail.as_view(), name='morceau'),
    path('<int:pk>', morceau_detail, name='morceau-detail'),
    path('morceau/create', MorceauCreate.as_view(), name='morceau-create'),
    path('morceau/update/<int:pk>', MorceauUpdate.as_view(), name='morceau-update'),
    path('morceau/delete/<int:pk>', MorceauDelete.as_view(), name='morceau-delete'),

    path('artistes/', ArtisteList.as_view(), name='artistes'),    
    path('artiste/<int:pk>', ArtisteDetail.as_view(), name='artiste'),
    path('artiste/create/', ArtisteCreate.as_view(), name='artiste-create'),
    path('artiste/update/<int:pk>', ArtisteUpdate.as_view(), name='artiste-update'),
    path('artiste/delete/<int:pk>', ArtisteDelete.as_view(), name='artiste-delete'),
    
]