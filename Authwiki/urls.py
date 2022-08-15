# Authwiki/urls.py
from django.urls import path
#from Authwiki import views
from .views import (AuthwikiListView, AuthwikiListView, AuthwikiUpdateView, AuthwikiDetailView,   AuthwikiDeleteView, AuthwikiCreateView)
urlpatterns = [
path('<int:pk>/edit/', AuthwikiUpdateView.as_view(), name='authwiki_edit'), # new
path('<int:pk>/detail/', AuthwikiDetailView.as_view(), name='authwiki_detail'), 
path('<int:pk>/delete/', AuthwikiDeleteView.as_view(), name='authwiki_delete'), # new
path('new/', AuthwikiCreateView.as_view(), name='authwiki_new'),
#path('<int:pk>/detail/', views.authwiki, name='authwiki_detail'), 
path('', AuthwikiListView.as_view(), name='authwiki_list'),
]


