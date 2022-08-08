from django.shortcuts import HttpResponse,render
from .form_filds import  student_form
# Create your views here.
def studentform(request):
    fo=student_form()
    return render(request,'formfild.html',{'from_layout':fo})
