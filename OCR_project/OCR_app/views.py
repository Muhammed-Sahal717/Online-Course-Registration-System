from django.shortcuts import render, redirect, get_object_or_404
from .models import CourseRegistration
from .forms import CourseRegistrationForm


def home(request):
    return render(
        request,
        'home.html'
    )


def register(request):

    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(
                'registrations'
            )

    else:
        form = CourseRegistrationForm()

    return render(
        request,
        'form_register.html',
        {'form': form}
    )


def registrations(request):
    registrations = CourseRegistration.objects.all()
    return render(
        request,
        'list_registrations.html', 
        {'registrations': registrations}
    )

def registration_detail(request, pk):
    registration = get_object_or_404(CourseRegistration, pk=pk)
    return render(
        request,
        'detail_registration.html',
        {'registration': registration}
    )