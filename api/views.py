from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # Requires authentication 【2314.8, type: source】 

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user) # Filters notes by authenticated user 【2397.359, type: source】 

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user) # Sets the author to the current user 【2545.599, type: source】 
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # Requires authentication 【2627.8, type: source】 

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user) # Ensures users can only delete their own notes 【2702.92, type: source】