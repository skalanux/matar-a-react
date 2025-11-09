import random
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import F
from django.middleware.csrf import get_token
from .models import SheepCounter


def generate_positions(count):
    all_positions = [(i * 20, j * 20) for i in range(3) for j in range(3)]
    random.shuffle(all_positions)
    return all_positions[:count]


def index(request):
    counter, created = SheepCounter.objects.get_or_create(id=1, defaults={"count": 0})
    sheep_positions = generate_positions(counter.count)
    return render(
        request,
        "counter/index.html",
        {
            "count": counter.count,
            "csrf_token": get_token(request),
            "sheep_list": list(range(counter.count)),
            "sheep_positions": sheep_positions,
        },
    )


@require_POST
def count_sheep(request):
    counter = get_object_or_404(SheepCounter, id=1)
    counter.count = F("count") + 1
    counter.save()
    counter.refresh_from_db()
    sheep_positions = generate_positions(counter.count)
    return render(
        request,
        "counter/partials/counter.html",
        {
            "count": counter.count,
            "sheep_list": list(range(counter.count)),
            "sheep_positions": sheep_positions,
        },
    )
