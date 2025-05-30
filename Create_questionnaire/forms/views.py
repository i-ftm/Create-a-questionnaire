from rest_framework import generics, permissions
from .models import Form, Response
from .serializers import FormSerializer, ResponseSerializer

class FormListCreateView(generics.ListCreateAPIView):
    serializer_class = FormSerializer
    permission_class = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Form.objects.filter(owner=self.request.user) 
    
    def perform_creat(self, serializer):
        serializer.save(owner=self.request.user)
    

class FormDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Form.objects.filter(owner=self.request.user)

class SubmitResponseView(generics.CreateAPIView):
    serializer_class = ResponseSerializer
    permission_classes = [permissions.AllowAny]
    