from django.shortcuts import render, get_object_or_404
from vcptUnit_team.models import VcptuTeamModal
# Create your views here.
def teamPage(request):
    get_all_vcptu_staff = VcptuTeamModal.objects.all().order_by('-updated_at')
    template_name = 'vcptUnit_team/teamPage.html'
    context = {
        'get_all_vcptu_staff':get_all_vcptu_staff
    }
    return render(request, template_name, context)


def detailView(request, id ):
    get_staff_detail = get_object_or_404(VcptuTeamModal, id = id)
    
    template_name = 'vcptUnit_team/detailView.html'
    context = {
        'get_staff_detail':get_staff_detail
    }
    return render(request, template_name, context)
