from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.user.models import User
from django.contrib.auth.models import Group
from apps.rol.mixins import ValidatePermissionRequiredMixin
from apps.rol.forms import MascotasForm
from apps.rol.models import Mascotas, Adopcion


class MascotasListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Mascotas
    template_name = 'mascotas/list.html'
    permission_required = 'view_mascotas'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                a = User.objects.get(pk=request.user.id)
                b = a.dni
                c = Group.objects.get(user=request.user.id)
                if str(c) == 'AdminVet' or str(c) == 'AdminTotal':
                    for i in Mascotas.objects.all():
                        data.append(i.toJSON())
                if str(c) == 'Adoptante':
                    aa = Adopcion.objects.get(dpi=b)
                    bb = aa.dpi
                    dd = aa.pet
                    if bb == b:
                        c = Mascotas.objects.get(name=dd)
                        data.append(c.toJSON())
                # for i in Mascotas.objects.all():
                #     data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Mascotas'
        context['create_url'] = reverse_lazy('mascotas_create')
        context['list_url'] = reverse_lazy('mascotas_list')
        context['entity'] = 'Mascotas'
        return context


class MascotasCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Mascotas
    form_class = MascotasForm
    template_name = 'Mascotas/create.html'
    success_url = reverse_lazy('mascotas_list')
    permission_required = 'add_mascotas'
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
        context['title'] = 'Creación de un Mascotas'
        context['entity'] = 'Mascotas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class MascotasUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Mascotas
    form_class = MascotasForm
    template_name = 'mascotas/create.html'
    success_url = reverse_lazy('mascotas_list')
    permission_required = 'change_mascotas'
    url_redirect = success_url


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            print(request.POST)
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
        context['title'] = 'Edición de un Mascotas'
        context['entity'] = 'Mascotas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class MascotasDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Mascotas
    template_name = 'Mascotas/delete.html'
    success_url = reverse_lazy('mascotas_list')
    permission_required = 'delete_mascotas'
    url_redirect = success_url


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        print(request.POST)
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Mascotaso'
        context['entity'] = 'Mascotasos'
        context['list_url'] = self.success_url
        return context

class MascotasReportView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Mascotas
    template_name = 'mascotas/listm.html'
    permission_required = 'view_mascotas'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                a = User.objects.get(pk=request.user.id)
                b = a.dni
                c = Group.objects.get(user=request.user.id)
                if str(c) == 'AdminVet' or str(c) == 'AdminTotal':
                    for i in Mascotas.objects.all():
                        data.append(i.toJSON())
                if str(c) == 'Adoptante':
                    aa = Adopcion.objects.get(dpi=b)
                    bb = aa.dpi
                    dd = aa.pet
                    if bb == b:
                        c = Mascotas.objects.get(name=dd)
                        data.append(c.toJSON())
                # for i in Mascotas.objects.all():
                #     data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Mascotas'
        context['create_url'] = reverse_lazy('mascotas_create')
        context['list_url'] = reverse_lazy('mascotas_list')
        context['entity'] = 'Mascotas'
        return context

