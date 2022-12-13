from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from . import models
from . import forms
from .alert import mailSender
from hidden import mail_pass

# Create your views here.


def index(request):
    p_detail = models.Profile.objects.all()
    print(p_detail)
    context = {'p_detail':p_detail[0]}
    return render(request, 'index.html', context)

def about(request):
    p_detail = models.Profile.objects.all()
    services = models.Service.objects.all()
    context = {
        'p_detail':p_detail[0],
        'services':services
        }
    return render(request, 'about.html', context)


def project(request):
    projects = models.Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects.html', context)

def testmoin(request):
    return render(request, 'Testmoin_news.html')


def contact(request):

    if request.method == 'POST':
        cform = forms.ContactForm(request.POST)
        if cform.is_valid():
           name = cform.cleaned_data['name']
           email = cform.cleaned_data.get('email')
           msg = cform.cleaned_data.get('message')
           
           full_msg = f"Name: {name} and Email: {email}, Message: {msg}"
           
           mailSender(
               'contact from website', 
                full_msg,
               'tradevolatile@gmail.com',
               ['nwaspecialg@gmail.com', 'sirgreatspecial@gmail.com'],
               mail_pass,
           )
           messages.add_message(request, messages.INFO, "your message was sent")
           return redirect('.')
    else:
        cform = forms.ContactForm()
        
    context = {'cform':cform}
    return render(request, 'contact.html', context)


# def download_file(request, path):
#     fl_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(fl_path):
#         with open(fl_path, 'rb') as f:
#             response = HttpResponse(
#                 f.read(),
#                 content_type="application/cv"
#                 )
#             response['Content-Disposition'] = 'inline;filename='+os.path.basename(fl_path)
#             return response
#     else:
#         raise Http404