from django import forms


class UploadVideoForm(forms.Form):
    title = forms.CharField(max_length=255)
    tags = forms.CharField(max_length=255)
    files = forms.FileField()
