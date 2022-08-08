# from turtle import end_fill
from django import forms
from django.forms.widgets import NumberInput
class student_form(forms.Form):
    enrollment_number=forms.IntegerField(label='Enrollment number ',min_value=200000000)
    first_name = forms.CharField(label='name of student ')
    date= forms.DateField(widget=NumberInput(attrs={'type': 'date'}))