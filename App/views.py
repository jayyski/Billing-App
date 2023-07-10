from django.shortcuts import render,redirect
from .forms import BillForm
from django.contrib import messages
from .models import Bill
# Create your views here.

def index(request):
    if request.method == 'GET':
        bills = Bill.objects.all()
        return render(request, 'index.html', context={ 'bills': bills })
 
def form(request):
    return render(request, 'form.html')

def create(request):
    if request.method == 'POST':
        form = BillForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'Bill has not been added')
            return render(request, 'form.html', context={'f': form.errors })
    
    form.save()
    messages.success(request, 'Bill has been added')
    return render(request, 'form.html')

def delete(request, id):
    bill = Bill.objects.get(pk=id)
    bill.delete()
    messages.success(request, 'Bill has been deleted')
    return redirect('index')
            
        
        