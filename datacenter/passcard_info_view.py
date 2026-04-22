from datacenter.models import Passcard, Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render,get_object_or_404
from django.utils.timezone import localtime

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    # Программируем здесь
    for visit in visits:
        time_MOSCOW = localtime(visit.entered_at)
        duration = get_duration(visit)
        visit_info = {
                'entered_at': time_MOSCOW,
                'duration': format_duration(duration),
                'is_strange': is_visit_long(duration, 10)
            }
        this_passcard_visits.append(visit_info)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
