from datacenter.models import Passcard, Visit
from datacenter.helper_functions import get_duration, format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        time_MOSCOW = localtime(visit.entered_at)
        visit_info = {
                'who_entered': visit.passcard.owner_name,
                'entered_at': time_MOSCOW,
                'duration': format_duration(get_duration(visit)),
            }
        non_closed_visits.append(visit_info)
    
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
