from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Penssylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),                          
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

# Create your models here.
class Strategy(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class Kit(models.Model):
    date = models.DateField()
    strategy = models.ManyToManyField(Strategy)
        
class State(models.Model):
    name = models.CharField(max_length = 30)
    confirmed = models.IntegerField()
    death = models.IntegerField()
    lat = models.CharField(max_length = 10)
    long = models.CharField(max_length = 10)

    def __str__(self):
        return f"{self.name}"

class CustomUser(AbstractUser):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for strategy_id: {self.strategy} @{self.url}"
