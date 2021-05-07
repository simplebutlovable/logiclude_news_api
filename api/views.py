# Django imports
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# Rest Framework  imports
from rest_framework import generics, status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
# project imports
from api.serializers import (FullNewsSerializer,
                             ListTypeSerializer,
                             SemiFullCardSerializer,
                             ReadMoreNewsSerializer,
                             TagStyleCardSerializer,
                             )
from api.models import TestBlog, News

from datetime import timedelta


class LatestNewsView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        # "news_index" is the starting index of the object to be fetched
        news_index = self.kwargs.get("rank") - 1
        fetch_threshold = news_index + 1
        # order by date posted in descending order
        queryset = News.objects.order_by(
            "-date_posted")[news_index:fetch_threshold]
        news_data = SemiFullCardSerializer(queryset, many=True)
        if news_data.data != []:
            return Response(news_data.data, status=status.HTTP_200_OK)
        return Response({"error": "news not found"},
                        status=status.HTTP_404_NOT_FOUND)


class TrendingNewsView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        # "news_index" is the starting index of the object to be fetched
        news_index = 4
        fetch_threshold = news_index + 5
        # order by date posted in descending order
        queryset = News.objects.order_by(
            "-date_posted")[news_index:fetch_threshold]
        news_data = SemiFullCardSerializer(queryset, many=True)
        if news_data.data != []:
            return Response(news_data.data, status=status.HTTP_200_OK)
        return Response({"error": "news not found"},
                        status=status.HTTP_404_NOT_FOUND)


# List all the Top of the week news
class TopOfTheWeekView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        start_index = self.kwargs.get("start_index")
        end_index = self.kwargs.get("end_index")
        queryset = News.objects.exclude(top_of_the_week=False).filter(
            date_posted__gte=timezone.now() -
            timedelta(days=7)).order_by("-date_posted")[start_index:end_index]
        serializer = SemiFullCardSerializer(queryset, many=True)
        if serializer.data != []:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "News Not Found"},
                        status=status.HTTP_404_NOT_FOUND)


class EditorsPickView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        start_index = self.kwargs.get("start_index")
        end_index = self.kwargs.get("end_index")
        queryset = News.objects.exclude(editors_pick=False)
        news = queryset.order_by("-date_posted")[start_index:end_index]
        serializer = SemiFullCardSerializer(news, many=True)
        if serializer.data != []:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "News Not Found"},
                        status=status.HTTP_404_NOT_FOUND)



class CategorizedNewsView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        start_index = self.kwargs.get("start_index")
        end_index = self.kwargs.get("end_index")
        queryset = News.objects.filter(category=self.kwargs.get(
            "category")).order_by("-date_posted")[start_index:end_index]
        serializer = SemiFullCardSerializer(queryset, many=True)
        if serializer.data != []:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "News Not Found"},
                        status=status.HTTP_404_NOT_FOUND)




class SuggestedNewsView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        start_index = self.kwargs.get('start_index')
        end_index = self.kwargs.get('end_index')
        if self.kwargs.get("id") >= 10:
            queryset = News.objects.filter(category=self.kwargs.get(
                "category")).filter(id__lt=self.kwargs.get("id"))[start_index:end_index]
        else:
            queryset = News.objects.filter(category=self.kwargs.get(
                "category")).filter(id__gt=self.kwargs.get("id"))[start_index:end_index]

        serializer = TagStyleCardSerializer(queryset, many=True)
        if serializer.data == []:
             return Response ({"Error":"News not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response (serializer.data, status=status.HTTP_200_OK)
   


class SingleNewsDetailView (RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        queryset = News.objects.get(id=self.kwargs.get("id"))
        serializer = FullNewsSerializer (queryset)
        if serializer != "":
            return Response (serializer.data, status=status.HTTP_200_OK)
        return Response ({"Error":"News not found"},status=status.HTTP_404_NOT_FOUND)