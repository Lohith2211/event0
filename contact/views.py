from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EventContactForm

def events_contact(request):
    if request.method == 'POST':
        form = EventContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return HttpResponse("<h1>Thank you! Your query has been submitted and stored in the database.</h1>")
    else:
        form = EventContactForm()

    return render(request, 'contact.html', {'form': form})
