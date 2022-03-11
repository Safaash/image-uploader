from django.shortcuts import redirect, render
from .forms import ImageForm
from.models import Image
# Create your views here.
def home(request):

    fm=ImageForm()
    img=Image.objects.all()
    return render(request,'home.html',{'fm':fm,'img':img})


def delete(request,id):
    img=Image.objects.get(pk=id)
    img.delete()
    return redirect("/")

def upload(request):
     if request.method=='POST':
        
        for file in request.FILES.getlist('images'):
            inst=Image(photo=file)
            inst.save()
    
     return redirect("/")