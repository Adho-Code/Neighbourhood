  
from django import forms
from .models import *

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields = ('user_id','location_id')

class MakePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image_path','image_description')

class UploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =('user','email_address','neighborhood_id')

class BizForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude=['']

class ActivForm(forms.ModelForm):
    class Meta:
        model = Activities
        exclude=['']