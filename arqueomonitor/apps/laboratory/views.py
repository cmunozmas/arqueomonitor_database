from django.shortcuts import render
from forms import CruiseForm

# def start(request):
#     form = CruiseForm()
#     context = {'form':form,}
#     return render(request, 'index.html', context)

def start(request):
    form = CruiseForm()
    print request.GET
    context = {'form':form,}
    return render(request, 'form_cruise.html', context)

    # form = CruiseForm(request.POST or None)
    # instance = forms.save(commit=True)
    # instance.save()
    # return render(request, 'form_cruise.html', {})

def addCruise(request):
    if request.method == 'POST':
        form = CruiseForm(request.POST or None)
        if form.is_valid():
            form.save()
    context = {
        "form": form,
    }
    return render(request, 'form_cruise.html', context)
