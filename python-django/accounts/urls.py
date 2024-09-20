from rest_framework.routers import DefaultRouter
from django.urls.conf import path, include
from accounts import views

router = DefaultRouter()
router.register(r'', views.AccountViewSet, basename='accounts')

urlpatterns = [
    path(r'', include(router.urls)),
]
