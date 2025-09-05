# from django.db import models
from mongoengine import Document, StringField, EmailField, BooleanField, DateTimeField
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class MongoUser(Document):
    meta = {
        "collection": "users",
        "indexes": [
            {"fields": ["email"], "unique": True},
            {"fields": ["username"], "unique": True},
        ],
    }

    email = EmailField(required=True, unique=True)
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    first_name = StringField(max_length=150)
    last_name = StringField(max_length=150)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    date_joined = DateTimeField(default=timezone.now)

    def set_password(self, raw_password: str):
        self.password = make_password(raw_password)

    def check_password(self, raw_password: str):
        return check_password(raw_password, self.password)

    @property
    def is_authenticated(self):
        return True

    @property
    def pk(self):
        return str(self.id)

    def get_full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip()

    def get_short_name(self):
        return self.first_name or self.username