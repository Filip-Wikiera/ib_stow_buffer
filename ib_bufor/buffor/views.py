from django.shortcuts import render
from .forms import P1Form


# Create your views here.
def P1Page(request):
    if request.method == "POST":
        form = P1Form(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Count added!',
                "form": form
            }
            return render(request, 'P1.html', context)
        else:
            context = {
                'message': "Save error",
                "form": form
            }

    else:
        form = P1Form()
        context = {
            'message': '',
            "form": form
        }

    return render(request, "P1.html", context)