from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatThread, Message
from django.contrib.auth.models import User
from ads.models import Ad
from django.utils import timezone

@login_required
def chat_detail(request, thread_id):
    thread = get_object_or_404(ChatThread, id=thread_id, users=request.user)
    other_user = thread.users.exclude(id=request.user.id).first()
    
    # Oznacz wiadomości jako przeczytane
    Message.objects.filter(
        thread=thread,
        is_read=False
    ).exclude(
        sender=request.user
    ).update(
        is_read=True,
        read_at=timezone.now()
    )

    if request.method == "POST":
        text = request.POST.get("message")
        if text:
            Message.objects.create(
                thread=thread,
                sender=request.user,
                text=text
            )
        # Odświeżenie strony po wysłaniu wiadomości
        return redirect('chat_detail', thread_id=thread.id)
    
    # pobieramy wszystkie czaty użytkownika (listę po lewej stronie)
    threads = ChatThread.objects.filter(users=request.user)
    threads_with_other = [
        (t, t.users.exclude(id=request.user.id).first())
        for t in threads
    ]
    messages = thread.messages.all().order_by("timestamp")
    
    # Lista wątków po lewej stronie
    threads = ChatThread.objects.filter(users=request.user)
    threads_with_other = [(t, t.users.exclude(id=request.user.id).first()) for t in threads]
    
    return render(request, "chat/chat_detail.html", {
        "thread": thread,
        "messages": messages,
        "other_user": other_user,
        "threads_with_other": threads_with_other
    })

@login_required
def start_chat(request, user_id):
    user2 = get_object_or_404(User, id=user_id)

    # Nie pozwalamy tworzyć czatu z samym sobą
    if user2 == request.user:
        return redirect("chat_list")

    # szukamy istniejącego wątku
    thread = (
        ChatThread.objects
        .filter(users=request.user)
        .filter(users=user2)
        .first()
    )

    # jeśli nie istnieje — tworzymy
    if not thread:
        thread = ChatThread.objects.create()
        thread.users.add(request.user, user2)

    return redirect("chat_detail", thread_id=thread.id)

@login_required
def chat_list(request):
    threads = ChatThread.objects.filter(users=request.user)
    
    # Tworzymy listę w formie (thread, other_user)
    threads_with_other = []
    for t in threads:
        # Pobierz "drugiego użytkownika" w wątku
        other = t.users.exclude(id=request.user.id).first()
        threads_with_other.append((t, other))
    
    return render(request, "chat/chat_list.html", {"threads_with_other": threads_with_other})