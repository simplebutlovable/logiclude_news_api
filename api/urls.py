from django.urls import path

from api.views import (
    LatestNewsView,
    TopOfTheWeekView,
    CategorizedNewsView,
    TrendingNewsView,
    EditorsPickView,
    SuggestedNewsView,
    SingleNewsDetailView,
)

app_name = "api"

urlpatterns = [
#Latest News Component
    path("news/latest/<int:rank>/", LatestNewsView.as_view(), name="LatestNews"),
# Trending Component
    path("news/trending/", TrendingNewsView.as_view(), name="RandomNews"),
# Single News Page
    path("news/details/<int:id>/", SingleNewsDetailView.as_view(), name="SingleNewsDetails"),
#Top of the Week Component
    path("news/topoftheweek/<int:start_index>/<int:end_index>/", TopOfTheWeekView.as_view(), name="TopOfTheWeek"),
# Editors Choice Component
    path("news/editorspick/<int:start_index>/<int:end_index>/",
         EditorsPickView.as_view(), name="EditorsPick"),
#Categorized Page
    path("news/category/<str:category>/<int:start_index>/<int:end_index>/",
         CategorizedNewsView.as_view(), name="CategorizedNews"),
#Read More Component and Also Read Component
    path("news/suggested/<str:category>/<int:id>/<int:start_index>/<int:end_index>/",
         SuggestedNewsView.as_view(), name="Suggested"),



]
