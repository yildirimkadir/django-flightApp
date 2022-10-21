from django.shortcuts import render
from .permissions import IsStafforReadOnly
from .serializers import FlightSerializer, ReservationSerializer, StaffFlightSerializer
from rest_framework import viewsets
from .models import Flight, Passenger, Reservation
# Create your views here.
class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStafforReadOnly,)
    
class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer