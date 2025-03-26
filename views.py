from django.shortcuts import render, redirect # type: ignore
from .models import Appointments # type: ignore
from django.contrib import messages # type: ignore

def appointment(request):
    if request.method == "POST":
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        person_name = request.POST.get('person_name')
        person_dob = request.POST.get('person_dob')
        person_phone = request.POST.get('person_phone')
        person_email = request.POST.get('person_email')
        remarks = request.POST.get('remarks')
        meet_person_name = request.POST.get('meet_person_name')

        Appointments.objects.create(
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            person_name=person_name,
            person_dob=person_dob,
            person_phone=person_phone,
            person_email=person_email,
            remarks=remarks,
            meet_person_name=meet_person_name
        )

        messages.success(request, "Appointment booked successfully!")
        return redirect('/index/')

    return render(request, 'index.html')
