from django.db import models

# Create your models here.

STATE_CHOICE = (
    ('PK-JK', 'Azad Jammu & Kashmir'),
    ('PK-BA', 'Balochistan'),
    ('PK-TA', 'Federally Administered Tribal Areas'),
    ('PK-GB', 'Gilgit-Baltistan'),
    ('PK-IS', 'Islamabad'),
    ('PK-KP', 'Khyber Pakhtunkhwa'),
    ('PK-PB', 'Punjab'),
    ('PK-SD', 'Sindh')
)


class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='profile_img', blank=True)
    resume_file = models.FileField(upload_to='doc', blank=True)