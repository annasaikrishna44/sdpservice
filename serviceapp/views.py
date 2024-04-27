from django.shortcuts import render,get_object_or_404,redirect
from .models import *

# Create your views here.
def servicepost(request):
    return render(request,'serviceapp/servicepost.html')

def add_job_details(request):
    if request.method == 'POST':
        work_title = request.POST.get('workTitle')
        salary_offered = request.POST.get('salaryOffered')
        job_type = request.POST.get('jobType')
        benefits = request.POST.get('benefits')
        education = request.POST.get('education')
        work_location = request.POST.get('workLocation')


        service_details = ServiceDetails(
            work_title = work_title,
            salary_offered = salary_offered,
            job_type = job_type,
            benefits =benefits,
            education =education,
            work_location =work_location,
        )
        service_details.save()
        return render(request, 'serviceapp/datainserted.html')
    return render(request, 'servicehomepage.html')

def view_job_details(request):
    job_details_list = ServiceDetails.objects.all()
    return render(request, 'serviceapp/view_job_details.html', {'job_details_list':job_details_list})

def edit_job_details(request, job_id):
    job_details = get_object_or_404(ServiceDetails, id= job_id)
    if request.method == 'POST':
        job_details.work_title = request.POST.get('workTitle')
        job_details.salary_offered = request.POST.get('salaryOffered')
        job_details.job_type = request.POST.get('jobType')
        job_details.benefits = request.POST.get('benefits')
        job_details.education = request.POST.get('education')
        job_details.work_location = request.POST.get('workLocation')
        job_details.save()
        return redirect('serviceapp:view_job_details')
    return render(request, 'serviceapp/edit_job_details.html', {'job_details':job_details})


def delete_job_details(request, job_id):
    job_details = get_object_or_404(ServiceDetails, id=job_id)
    if request.method == 'POST':
        job_details.delete()
        return redirect('serviceapp:view_job_details')
    return render(request, 'serviceapp/edit_job_details.html', {'job_details': job_details})
