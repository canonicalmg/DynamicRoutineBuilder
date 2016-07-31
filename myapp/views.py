from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.models import User

from django.http import HttpResponse


# Create your views here.

def index(request):
    if request.user.is_authenticated():
        #send them to /home
        template = loader.get_template('index.html')
        context = {
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect("signin")

@csrf_exempt
def incomingPOSTAndroid(request):
    if request.method == "POST":
        print "entered incomingPOSTAndroid"
        print "post data = ", request.POST
        print "date = ", request.POST.get("date")
        print "addr = ", request.POST.get("addr")
        thisUser = User.objects.get(username = "admin")
        try:
            currentMessage = textMessage.objects.get(msgId=request.POST.get("id"))
        except:
            newMessage = textMessage(msgId=request.POST.get("id"), addr=request.POST.get("addr"), date=request.POST.get("date"), user=thisUser)
            newMessage.save()

        return HttpResponse("done and send")