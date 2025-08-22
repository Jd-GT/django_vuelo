def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights/flight_list.html', {'flights': flights})

def flight_form(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'flights/flight_form.html', {'form': form})

def flight_stats(request):
    total_flights = Flight.objects.count()
    nacional_flights = Flight.objects.filter(type='Nacional').count()
    internacional_flights = Flight.objects.filter(type='Internacional').count()
    return render(request, 'flights/flight_stats.html', {
        'total_flights': total_flights,
        'nacional_flights': nacional_flights,
        'internacional_flights': internacional_flights,
    })