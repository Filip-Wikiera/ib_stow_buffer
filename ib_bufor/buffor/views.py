from django.shortcuts import render
from .forms import P1Form, P2Form, P3Form, P4Form, TransForm, TSOForm
from .models import P1, P2, P3, P4, Trans, TSO, closest_count
from datetime import datetime, timedelta
from .TimePoint_Buffer import TimePoint_Buffer
import re

def extract_id(input_string):
    pattern = r'id="([^"]+)"'
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
        return None

# Create your views here.
def generic_floor(request, model_cls, form_cls, template_name):

    last_count = model_cls.objects.latest('time_stamp')
    form = form_cls(instance=last_count)

    context = {
            'message': '',
            "form": form,
            "last_count_date": last_count.time_stamp.strftime("%d/%m/%Y %H:%M")
        }

    context["form_clean"] = ''

    for x in form:
        id = extract_id(str(x))
        context["form_clean"] += f'<div class="clear_label" onclick=\'clear_form("{id}")\'>X</div><br>'

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


def TotalPage(request):
    context = {
            'message': ''
        }
    now = datetime.now()
    context['buffor_now'] = TimePoint_Buffer(now)
    context['trans_nyr'] = TimePoint_Buffer(now).trans_nyr()

    date_backtrack = now.replace(minute=0, second=0, microsecond=0)
    context['buffor_old'] = ""

    for x in range(12):
        old_buffer = TimePoint_Buffer(date_backtrack)
        context['buffor_old'] += str(old_buffer)
        date_backtrack = date_backtrack - timedelta(hours=1)


    return render(request, "total.html", context)
