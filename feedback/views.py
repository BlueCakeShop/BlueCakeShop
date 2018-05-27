
from django.shortcuts import render, get_object_or_404
from .forms import Subscriberform
from .models import *
from .models import *

# Create your views here.

def feedback(request):
    form = Subscriberform(request.POST or None)
    questions = subscriber.objects.all()
    #form = subscriberform(request)
    if request.method == "POST" and form.is_valid():
        try:
            # print(form.cleaned_data)
            new_form = form.save()
            # form = Subscriberform()
            return HttpResponseRedirect('')
        except Exception as e:
            exs = e
    return render(request,'feedback/feedback.html', locals())
