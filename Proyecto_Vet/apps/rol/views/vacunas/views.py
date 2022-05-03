from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.rol.forms import VacunasForm
from apps.rol.models import Vacunas
from apps.rol.mixins import ValidatePermissionRequiredMixin


class VacunasListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Vacunas
    template_name = 'vacunas/list.html'
    permission_required = 'view_vacunas'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Vacunas.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Vacunas'
        context['create_url'] = reverse_lazy('vacunas_create')
        context['list_url'] = reverse_lazy('vacunas_list')
        context['entity'] = 'Vacunas'
        return context



class VacunasCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Vacunas
    form_class = VacunasForm
    template_name = 'vacunas/create.html'
    success_url = reverse_lazy('vacunas_list')
    permission_required = 'add_vacunas'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregando Vacunas'
        context['entity'] = 'Vacunas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class VacunasUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Vacunas
    form_class = VacunasForm
    template_name = 'vacunas/create.html'
    success_url = reverse_lazy('vacunas_list')
    permission_required = 'change_vacunas'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición una Vacuna'
        context['entity'] = 'Vacunas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class VacunasDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Vacunas
    template_name = 'vacunas/delete.html'
    success_url = reverse_lazy('vacunas_list')
    permission_required = 'delete_vacunas'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Vacuna'
        context['entity'] = 'Vacunas'
        context['list_url'] = self.success_url
        return context
