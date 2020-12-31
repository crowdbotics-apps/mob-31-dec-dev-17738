from rest_framework import authentication
from hgfhgfghfhf.models import Hjhgfjg
from .serializers import HjhgfjgSerializer
from rest_framework import viewsets


class HjhgfjgViewSet(viewsets.ModelViewSet):
    serializer_class = HjhgfjgSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Hjhgfjg.objects.all()
