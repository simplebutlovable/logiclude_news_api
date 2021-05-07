from rest_framework import serializers

from api.models import TestBlog, News,Emails


# Dummy Serializer for testing purpose ONLY!
class TestBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestBlog
        fields = "__all__"

class FullNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

class ListTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title','id', 'date_posted')


class SemiFullCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title','id', 'category', 'author','date_posted', 'display_image')


class TagStyleCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title','id', 'author','date_posted', 'display_image')








class ReadMoreNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title','id','date_posted', 'display_image')


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emails
        fields = "__all__"