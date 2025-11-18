from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home_page"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="Article_detail"),
    path('contact/',views.contact_register_view,name="contact"),

    
]
