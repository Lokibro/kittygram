from rest_framework.routers import DefaultRouter

from django.urls import include, path

from cats.views import CatViewSet, OwnerViewSet

router = DefaultRouter()

router.register(prefix='cats', viewset=CatViewSet)
router.register(prefix='owners', viewset=OwnerViewSet)

urlpatterns = [
   path('', include(router.urls)),
]