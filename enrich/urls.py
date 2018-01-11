from django.urls import include, path
from . import views, api_views

app_name = 'enrich'

urlpatterns = [
    path('token/', views.TokenQuery.as_view(), name='token'),
    path('synset/', api_views.synset, name='synset'),

]
