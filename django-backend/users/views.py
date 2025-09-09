from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class RegisterView(APIView):
    def get(self, request):
        return Response({'detail': 'Please use POST to register a new user.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data.copy()
        username = data.get('username')
        email = data.get('email')
        if CustomUser.objects.filter(username=username).exists():
            return Response({'detail': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if CustomUser.objects.filter(email=email).exists():
            return Response({'detail': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        data['password'] = make_password(data.get('password'))
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            # Issue JWT token after registration
            from rest_framework_simplejwt.tokens import RefreshToken
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'detail': 'User registered successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
