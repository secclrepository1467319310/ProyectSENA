from rest_framework import viewsets
from .models import report
from .serializer import reportSerializers


class reportViewSet(viewsets.ModelViewSet):
    queryset = report.objects.all()
    serializer_class = reportSerializers