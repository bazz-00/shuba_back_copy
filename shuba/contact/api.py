from contact.models import Contact
from rest_framework import viewsets, permissions
from contact.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSerializer