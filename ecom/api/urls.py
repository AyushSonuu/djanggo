from django.urls import path , include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path("", home, name='api.home'),
    # path("category/", admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/',include('api.urls')),
]

