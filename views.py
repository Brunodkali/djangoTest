# views.py em menu app

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import MenuItem, Reservation

def menu_items(request):
    items = MenuItem.objects.all().values('id', 'name', 'description')
    return JsonResponse(list(items), safe=False)

@login_required
def book_table(request):
    return JsonResponse({'message': 'Table Booked'})
