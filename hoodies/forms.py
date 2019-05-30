from django import forms
from .models import *

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields = ('user_id','hoodies_name','location_id')

class MakePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image_path','image_description','hoodies_id')

class UploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =('user','email_address','neighborhood_id')

class ActiForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields =('activity_name','user','neighborhood_id','business_email')