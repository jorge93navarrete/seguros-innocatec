from django.urls import path
from django.conf.urls import url, include
from .views import SeguroList, SeguroDetail, SeguroCreate

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('seguros/', SeguroList.as_view(), name="seguro"),
    path('seguros/', SeguroCreate.as_view(), name="seguro"),
    path('seguros/<int:pk>/', SeguroDetail.as_view()),

    url(r'^', include(router.urls)),
]