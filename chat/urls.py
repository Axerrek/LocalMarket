from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_list, name="chat_list"),
    path("<int:thread_id>/", views.chat_detail, name="chat_detail"),
    path("start/user/<int:user_id>/", views.start_chat, name="start_chat"),
]