from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Mail', 'Mail'),
    ('Female', 'Female'),
]

JOB_CITY_CHOICE = [
    ('Lahore', 'Lahore'),
    ('Islamabad', 'Islamabad'),
    ('Multan', 'Multan'),
    ('Karachi', 'Karachi'),
    ('Rawalpindi', 'Rawalpindi'),
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(
        label='Preferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = ('name', 'dob', 'gender', 'locality', 'city',
                  'pin', 'state', 'mobile', 'email', 'job_city', 'profile_img', 'resume_file')

        labels = {'name': 'Full Name', 'dob': 'Date of Birth',
                  'gender': 'Gender', 'locality': 'Locality',
                  'city': 'City', 'pin': 'Pin Code',
                  'mobile': 'Mobile No.',
                  'email': 'Email ID', 'profile_img': 'Profile Image',
                  'resume_file': 'Resume'}

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
