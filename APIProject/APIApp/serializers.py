from rest_framework import serializers
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(label = "Enter Book Id")
    title = serializers.CharField(label = "Enter  book title")
    author = serializers.CharField(label = "Enter author name")