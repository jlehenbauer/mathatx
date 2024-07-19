import re
from django import forms
from django.db import models
from os import path

# class Experience(models.Model):
#     from_year = models.DateField
#     to_year = models.DateField
#     current = models.BooleanField
#     title = models.CharField(max_length='300')
    
# class Employer(models.Model):
#     name = models.CharField(max_length='100')

def path_generator(instance, filename):
    base, extension = os.path.splitext(os.path.basename(filename))
    file_dir = f"images/{base}.{extension}"
    return file_dir

def review_star_validator(review):
    return 0 <= review.stars <= 5

def email_validator(email_address):
    return re.match("[^@]+@[^@]+\.[^@]+", email_address)

class AboutMe(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(default='')
    image = models.ImageField(default='', upload_to='images/mathatx/aboutme')

    def __str__(self):
        return self.title

class Banner(models.Model):
    text = models.CharField(max_length=500)
    image = models.ImageField(default='', upload_to='images/mathatx/banners')

    def __str__(self):
        return self.text

class Review(models.Model):
    name = models.CharField(max_length=50)
    stars = models.PositiveSmallIntegerField()
    quote = models.CharField(max_length=1000)
    #TODO: limit stars to 0-5
    source = models.URLField(default="https://maps.app.goo.gl/Xr7ZFPE7oEd7eE2PA")

    def __str__(self):
        return f"{self.name}: {self.stars} ★"

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    image = models.ImageField(default='', null='', upload_to='images/mathatx/services')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Faq(models.Model):
    question = models.CharField(max_length=2000, default='')
    answer = models.TextField(default='')

    def __str__(self):
        return self.question[:100]

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # TODO: validators for email and phone
    phone = forms.CharField(max_length=15)
    # subject = models.CharField(max_length=100)
    message = models.TextField(default='')
    info_sliding_scale = models.BooleanField(default=False)
    info_multiple_students = models.BooleanField(default=False)
    info_virtual_services = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ContactForm(forms.ModelForm):
    class Meta: 
        model = Contact
        fields = '__all__'