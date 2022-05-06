from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.rol.mixins import ValidatePermissionRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView, ValidatePermissionRequiredMixin):
    template_name = 'dashboard.html'
    success_url = reverse_lazy('user_list')
    #permission_required = 'view_mascotas'
    url_redirect = success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de Administrador'
        return context

    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request,*args, *kwargs)