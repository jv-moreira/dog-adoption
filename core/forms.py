from django import forms
from django.core.mail.message import EmailMessage
from .models import Dog


class DogModelForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'age', 'breed', 'sex', 'image']


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    subject = forms.CharField(label='Subject', max_length=120)
    message = forms.CharField(label='Message', widget=forms.Textarea())

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        mail = EmailMessage(
            subject='Email sent from Dog Adoption',
            body=content,
            from_email='dog_adoption@gmail.com',
            to=['adm_dog_adoption@gmail.com'],
            headers={'Reply-To': email}
        )

        mail.send()
