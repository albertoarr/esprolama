from django.contrib import admin
from django.db.models import Model

from . import models

# Register your models here.

# Bucle que registra todos los modelos en localhost/admin/
for model_name, model in models.__dict__.items():
    if isinstance(model, type) and issubclass(model, Model):
        admin.site.register(model)