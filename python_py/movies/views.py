from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from movies.models import Movie
from movies.forms import TicketForm
from movies.filters import MovieFilter
from django.views.generic.list import ListView
from django_filters.views import FilterView


class MovieListView(FilterView):
    model = Movie
    template_name = "movies/movie_list.html"
    context_object_name = "object_list"
    filterset_class = MovieFilter


# def movie_list(request):
#     movie_filter = MovieFilter(request.GET, queryset=Movie.objects.all())
#     return render(request, 'movies/movie_list.html', {'filter': movie_filter})

@login_required
def book_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_confirmation')
    else:
        form = TicketForm()
    return render(request, 'movies/book_ticket.html', {'form': form})

def ticket_confirmation(request):
    return render(request, 'movies/ticket_confirmation.html')

from django.shortcuts import render

def movie_list(request):
    return render(request, 'movies/movie_list.html')

from django.shortcuts import render, redirect
from .forms import TicketForm

def book_ticket(request):
    if request.method == "POST":
        # Here we process the form submission
        # If your form uses Django's form classes:
        form = TicketForm(request.POST)
        if form.is_valid():
            # Process the valid form data here, for example:
            # Save to the database or generate ticket, etc.
            return redirect('ticket_confirmation')  # Redirect to confirmation page
    else:
        form = TicketForm()  # Empty form for GET requests

    return render(request, 'movies/book_ticket.html', {'form': form})

import qrcode
from io import BytesIO
import base64
from django.shortcuts import render

def ticket_confirmation(request):
    # Example booking details or URL
    qr_data = "https://example.com/your-booking-details"  # Replace with actual booking info

    # Generate the QR code
    qr = qrcode.make(qr_data)
    qr_image = BytesIO()
    qr.save(qr_image)
    qr_image.seek(0)  # Rewind to the beginning of the image

    # Convert the image to base64 encoding
    qr_code_url = base64.b64encode(qr_image.getvalue()).decode('utf-8')

    # Debugging: Print the base64 QR code to check its value
    print("Generated QR code base64:", qr_code_url[:50])  # Print the first 50 characters of the base64 string

    # Pass the QR code data URL to the template
    return render(request, "movies/ticket_confirmation.html", {"qr_code_url": qr_code_url})
