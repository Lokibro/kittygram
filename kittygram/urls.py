from rest_framework.routers import SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet

router = SimpleRouter()

router.register(prefix='cats', viewset=CatViewSet)

urlpatterns = [
   path('', include(router.urls)),
]