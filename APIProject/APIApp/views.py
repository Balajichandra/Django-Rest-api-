from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
class BookApiView(APIView):
    serializers_class = BookSerializer
    def get(self,request):
        allBooks = Book.objects.all().values()
        return Response({"Message":"List of books","Book List":allBooks})

    def post(self,request):
        print("Requset data is:",request.data)
        serializers_obj = BookSerializer(data=request.data)
        if (serializers_obj.is_valid()):
                Book.objects.create(id = serializers_obj.data.get("id"),
                                    title = serializers_obj.data.get("title"),
                                    author = serializers_obj.data.get("author")
                                    )
        book = Book.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Book added","Books":book})
