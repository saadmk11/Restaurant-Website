from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True, label='email')
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
        )
