from django.contrib import admin
from movies.models import Ticket, Account, Movie

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Account)
admin.site.register(Movie)
