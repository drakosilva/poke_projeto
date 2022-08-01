from ..serializers import Authorserializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_condition import Or


class AuthorViewset(ReadOnlyModelViewSet):

    serializer_class = Authorserializer
    permission_classes = [Or(IsAuthenticated)]
    queryset = get_user_model()