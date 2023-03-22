from django import forms

class ContactUsForm(forms.Form):
    tracking_id = forms.UUIDField()
    email = forms.EmailField()
