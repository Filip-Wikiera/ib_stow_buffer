from django.shortcuts import render
from .forms import P1Form, P2Form, P3Form, P4Form, TransForm, TSOForm
from .models import P1, P2, P3, P4, Trans, TSO


# Create your views here.
def generic_floor(request, model_cls, form_cls, template_name):


    last_count = model_cls.objects.latest('time_stamp')
    form = form_cls(instance=last_count)

    context = {
            'message': '',
            "form": form,
            "last_count_date": last_count.time_stamp.strftime("%d/%m/%Y %H:%M")
        }

    if request.method == "POST":
        form = form_cls(request.POST)
        if form.is_valid():
            form.save()

            last_count = model_cls.objects.latest('time_stamp')
            form = form_cls(instance=last_count)

            context["form"] = form
            context["last_count_date"] = last_count.time_stamp.strftime("%d/%m/%Y %H:%M")
            return render(request, template_name, context)
        else:
            context["message"] = 'Save error!'

    return render(request, template_name, context)


def P1Page(request):
    return generic_floor(request, P1, P1Form, 'P1.html')
def P2Page(request):
    return generic_floor(request, P2, P2Form, 'P2.html')
def P3Page(request):
    return generic_floor(request, P3, P3Form, 'P3.html')
def P4Page(request):
    return generic_floor(request, P4, P4Form, 'P4.html')
def TransPage(request):
    return generic_floor(request, Trans, TransForm, 'Trans.html')
def TSOPage(request):
    return generic_floor(request, TSO, TSOForm, 'TSO.html')