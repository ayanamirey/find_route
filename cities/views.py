from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from cities.forms import HtmlForm, CityForm
from cities.models import City

__all__ = (
    'home', 'CityDetailView', 'CityCreateView', 'CityUpdateView'
)


def home(request, pk=None):
    # if pk:
    #     # city = City.objects.filter(pk=pk).first()
    #     city = get_object_or_404(City, pk=pk)
    #     context = {'object': city}
    #     return render(request, 'cities/detail.html', context)

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm()
    qs = City.objects.all()
    context = {'objects_list': qs, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')


# class CityDeleteView(DeleteView):
#     model = City
#     # template_name = 'cities/delete.html'

#     success_url = reverse_lazy('cities:home')
#
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)


def post_delete(request, pk=None):
    post = get_object_or_404(City, pk=pk).delete()
    return redirect('cities:home')

