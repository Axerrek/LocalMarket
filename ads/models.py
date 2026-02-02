from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ad(models.Model):
    
    REGIONS = [
        ("DS", "Dolnośląskie"),
        ("KP", "Kujawsko-pomorskie"),
        ("LU", "Lubelskie"),
        ("LB", "Lubuskie"),
        ("LD", "Łódzkie"),
        ("MA", "Małopolskie"),
        ("MZ", "Mazowieckie"),
        ("OP", "Opolskie"),
        ("PK", "Podkarpackie"),
        ("PD", "Podlaskie"),
        ("PM", "Pomorskie"),
        ("SL", "Śląskie"),
        ("SK", "Świętokrzyskie"),
        ("WN", "Warmińsko-mazurskie"),
        ("WP", "Wielkopolskie"),
        ("ZP", "Zachodniopomorskie"),
    ]
    blank=True,   # może być puste w formularzu
    null=True     # może być NULL w bazie
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    region = models.CharField(max_length=2, choices=REGIONS)  # tutaj województwo
    image = models.ImageField(upload_to='items_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title