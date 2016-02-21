from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Nombre y Apellido'}))
    sender = forms.EmailField(label='Email', max_length=100,
                             widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Mensaje',
                                       'rows': '6'}))
