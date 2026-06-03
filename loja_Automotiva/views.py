from django.shortcuts import render
#from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
import datetime

def home(request):
    # Context data to pass to the HTML template (optional)
    context = {
        "user_name": "Alex"
    }
    # Render takes: request, template path, and optional context
    return render(request, "home/index.html", context)


def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)
