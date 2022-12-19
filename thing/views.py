from django.shortcuts import render
from .models import Thing
from .permissions import OwnerOnly
# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ThingSerializer

class ThingListCreateView(ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    

class ThingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer  
    permission_classes=[OwnerOnly]
