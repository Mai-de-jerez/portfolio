from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(attrs={"class":"field half", "placeholder":"Escribe tu nombre"})
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={"class":"field half", "placeholder":"Escribe tu email"})
    )
    content = forms.CharField(
        label="Contenido",
        required=True,
        widget=forms.Textarea(attrs={'rows': 6, "placeholder":"Escribe tu mensaje"})
    )