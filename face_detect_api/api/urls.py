from django.urls import path
from .views import MyFileView

urlpatterns = [
    path('', MyFileView.as_view(), name='uploading'),
]
