from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from django.urls import include, path

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet

router = DefaultRouter()

router.register(prefix='cats', viewset=CatViewSet)
router.register(prefix='owners', viewset=OwnerViewSet)
router.register(prefix=r'mycats', viewset=LightCatViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.jwt')),
]
