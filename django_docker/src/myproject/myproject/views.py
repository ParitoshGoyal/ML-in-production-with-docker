from django.http import HttpResponse
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import NameForm
from .forms import NameForm
from .gpt2_text_generator import *
#import .gpt2_text_generator as gpt2

def current_datetime(request=1):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:


            complete_sentence = generated_text(str(form.cleaned_data['input_prompt']))
            #complete_sentence = type(form.cleaned_data['your_name'])
            #return HttpResponseRedirect('/thanks/')
            return get_response(complete_sentence)
            #return HttpResponseRedirect('/results')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})

def get_response(response):
    #now = datetime.datetime.now()
    html = "<html><body>The completed sentence from hugging face is---------- <p style='color:red'>%s</p></body></html>" % response
    return HttpResponse(html)