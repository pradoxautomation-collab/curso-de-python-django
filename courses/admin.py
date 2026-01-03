from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import Course
from .models import About
from .models import ConctactMessage

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'original_price', 'discounted_price')
    name = 'courses'
    verbose_name = 'cursos'

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    name = 'about'
    verbose_name = 'sobre'

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

@admin.register(ConctactMessage)
class ConctactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')
    name = 'conctact_message'
    verbose_name = 'mensagem de contato'