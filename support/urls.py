from django.urls import path, include
from .views import InquiryList


urlpatterns = [
    path('all/', InquiryList.as_view())
]