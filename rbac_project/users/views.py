from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Role
from .serializers import RoleSerializer,UserSerializer
from django.shortcuts import render
from users.permissions import has_permission
from django.http import JsonResponse
# Create your views here.


class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class RoleManagementView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_role = request.user.role.name if request.user.role else "No Role Assigned"
        return Response({"message": f"Hello {request.user.username}, you have the role: {user_role}"})
    



def api_tester(request):
    return render(request,'users/index.html')


@has_permission('can_view_data')
def tester_view(request):
    return JsonResponse({'message':'you have access to this view'})