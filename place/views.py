from django.shortcuts import render, get_object_or_404
from .models import VisitingPlace, State, District

def add_page(request):
    states = State.objects.all()
    districts = District.objects.all()
    dist = None
    st = None
    if request.method == 'POST':
        dist = request.POST.get('district')
        st = request.POST.get('state')
        if st:
            districts = districts.filter(state_id=st)

        visiting_place_name = request.POST.get('visiting_place_name')
        popularity = request.POST.get('popularity')
        image = request.FILES.get('image')
        if visiting_place_name and popularity and dist :
            district = District.objects.get(id=dist)

            print(district)
            print(type(district))
            print(district.id)
            print(type(district.id))
            print(district.name)
            print(type(district.name))

            VisitingPlace.objects.create(
                district=district,
                name=visiting_place_name,
                popularity=int(popularity),
                image=image
            )

    return render(request, 'add_visiting_place.html', {
        'states': states,
        'districts': districts,
        'dist': int(dist) if dist else None,
        'st': int(st) if st else None,
    })

def display(request):
    states = State.objects.all()
    districts = District.objects.all()
    places = VisitingPlace.objects.all()
    dist = None
    st = None

    if request.method == 'POST':
        dist = request.POST.get('district')
        st = request.POST.get('state')

        if st:
            districts = districts.filter(state_id=st)

        if dist :
            places = places.filter(district_id=dist)
        elif st:
            places = places.filter(district__state_id=st)

    return render(request, 'displaying_visiting_place.html', {
        'places': places,
        'states': states,
        'districts': districts,
        'dist': int(dist) if dist else None,
        'st': int(st) if st else None,
    })












