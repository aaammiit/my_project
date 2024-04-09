from django.shortcuts import render,redirect
from django.http.response import HttpResponseRedirect
from web.models import Contact

# Create your views here.
def index (request):
    return render(request,'index.html')

def about (request):
    return render (request,'about.html')

def solutions (request):
    return render (request,'solutions.html')

def process (request):
    return render (request,'process.html')

def contact(request):
    return render (request,'contact.html')

    #Get records from table
# def ContactData(request):
#     if request.method == 'POST':
#         print(request.POST)
#         Contact.objects.create(name = request.POST.get['name'],  
#         email = request.POST.get['email'], 
#         subject = request.POST.get('subject',None),
#         message = request.POST.get['message'])  
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER','/home/'))


def ContactData(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', None)
        message = request.POST.get('message')

        # Create a new Contact object
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        # Redirect to a thank you page or any other desired page
        return redirect('index')  # Assuming 'index' is the name of your homepage URL pattern
    else:
        return render(request, 'contact.html')  # Render the contact form if the request method is not POST



def right_advise(request):
    return render(request, 'RightAdvise.html')

def right_edge(request):
    return render(request, 'RightEdge.html')

def right_edit(request):
    return render(request, 'RightEdit.html')