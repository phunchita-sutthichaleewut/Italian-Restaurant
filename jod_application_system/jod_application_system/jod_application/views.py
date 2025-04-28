from django.shortcuts import render, redirect, get_object_or_404
from .models import JodApplication
from .forms import JodApplicationForm
from django.db.models import Q
from datetime import datetime
# Create your views here.


# Create your views here.
def home(request):
    applications = JodApplication.objects.all()
    return render(request, 'home.html', {'applications': applications})

def about(request):
    return render(request, "about.html")

def add_application(request):
    if request.method == 'POST':
        form = JodApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JodApplicationForm()
    return render(request, 'add_application.html', {'form': form})

def edit_application(request, pk):
    application = get_object_or_404(JodApplication, pk=pk)
    if request.method == 'POST':
        form = JodApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JodApplicationForm(instance=application)
    return render(request, 'edit_application.html', {'form': form, 'application': application})

def delete_application(request, pk):
    application = get_object_or_404(JodApplication, pk=pk)
    application.delete()
    return redirect('home')

def search_application(request):
    query = request.GET.get('q', '')
    applications = JodApplication.objects.none()

    if query:
        try:
            # พยายามแปลง query เป็นวันที่
            date_obj = datetime.strptime(query, '%Y-%m-%d').date()
            applications = JodApplication.objects.filter(
                Q(first_name__icontains=query) |
                Q(phone_number__icontains=query) |
                Q(booking_date=date_obj)
            )
        except ValueError:
            # ถ้าแปลงเป็นวันที่ไม่ได้ ให้ใช้แค่ field ที่เป็นข้อความ
            applications = JodApplication.objects.filter(
                Q(first_name__icontains=query) |
                Q(phone_number__icontains=query)
            )

    return render(request, 'search_application.html', {
        'applications': applications,
        'query': query
    })