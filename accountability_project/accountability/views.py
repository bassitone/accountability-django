from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
# TODO: Create forms classes in a separate file.  Then import them here

# Begin homepage.  / or /index TBD
def index(request):
    greet = "Welcome!\n" # What about templates?  We'll do them later
    message = greet + "I'm Accountability.  What can I help you with?\n"
    current_time = datetime.utcnow()
    return render(request, 'accountability/index.html', {})

# Dynamic shell for user pages
