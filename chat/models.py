from django.db import models
from django.contrib.auth.models import User

class ChatThread(models.Model):
    users = models.ManyToManyField(User, related_name="chat_threads")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wątek {self.id}"


class Message(models.Model):
    thread = models.ForeignKey(ChatThread, related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.sender}: {self.text[:20]}"
