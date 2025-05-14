from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage



# Create your views here.
def contact(request):
    contact_form = ContactForm() 
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get("name", "")
            email=request.POST.get("email", "")
            content=request.POST.get("content", "")
            email = EmailMessage(
                "Portfolio Mai: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["mainen1985@gmail.com"], 
                reply_to=[email]
            )
            try:
                email.send()
                # En caso de éxito, redirigimos a la misma página con un mensaje de éxito
                return redirect(reverse('contact')+ '?ok')

            except:
                # En caso de error, redirigimos a la misma página con un mensaje de error
                print("Error al enviar el correo")
                return redirect(reverse('contact')+ '?fail')

    return render(request, "contact/contact.html", {"form": contact_form})

         

   