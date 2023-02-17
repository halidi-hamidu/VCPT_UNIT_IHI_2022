from django.shortcuts import render
from vcptUnit_projects.models import VcptuProjects
# Create your views here.

def projectPage(request):
    get_all_project = VcptuProjects.objects.all()
    my_empty_list = []
    distinct_year_in_list = []
    for project_year in get_all_project:
        my_empty_list.append(project_year.project_conducted_during_the_year)
        if not project_year.project_conducted_during_the_year in distinct_year_in_list:
            distinct_year_in_list.append(project_year.project_conducted_during_the_year)
    print("yers", distinct_year_in_list) 
    template_name = 'vcptUnit_projects/projectPage.html'
    context ={
        'get_all_project':get_all_project,
        'distinct_year_in_list':distinct_year_in_list
    }
    return render (request, template_name, context)

def projectDetailPage(request, proj_year ):
    
    get_project_from_specific_year = VcptuProjects.objects.filter(project_conducted_during_the_year = proj_year)
    get_all_project = VcptuProjects.objects.all()
    my_empty_list = []
    distinct_year_in_list = []
    for project_year in get_all_project:
        my_empty_list.append(project_year.project_conducted_during_the_year)
        if not project_year.project_conducted_during_the_year in distinct_year_in_list:
            distinct_year_in_list.append(project_year.project_conducted_during_the_year)
    
    template_name = 'vcptUnit_projects/projectPage.html'
    context = {
    'get_project_from_specific_year':get_project_from_specific_year,
    'distinct_year_in_list':distinct_year_in_list,
    'proj_year':proj_year,
    }

    return  render(request, template_name, context)