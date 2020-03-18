from django.urls import path
from .views import home, bloghome

urlpatterns = [
    path('', home, name="home"),
    path('blog/', bloghome, name="bloghome"),
]