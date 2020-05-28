from django.shortcuts import render,redirect
from users.forms import CustomersForm
from users.models import Customers

# Create your views here.
def register(request):
    if request.method == "POST":
        form=CustomersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/items")
            except:
                pass
    else:
        form=CustomersForm()
    return render(request,"reg.html",{'form':form})

def items(request):
    # mo = Customers
    return render(request, "Home.html")