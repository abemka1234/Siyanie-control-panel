import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    active_cards = Passcard.objects.filter(is_active = True)
    print('Активных пропусков', len(active_cards))
    # print('owner_name: ',Passcard.objects.all()[0].owner_name)
    # print('passcode: ',Passcard.objects.all()[0].passcode)
    # print('created_at: ',Passcard.objects.all()[0].created_at)
    # print('is_active: ',Passcard.objects.all()[0].is_active)
