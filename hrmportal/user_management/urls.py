from django.urls import path
from user_management.views import user_list_view

app_name = "user"

urlpatterns = [path("", user_list_view, name="user-list")]
