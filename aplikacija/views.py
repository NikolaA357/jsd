from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

from .models import Country
from .models import Cars
from .models import Price
from .models import EnginePower

class CountryCreateView(CreateView):
	template_name='.html'
	model=Country
	fields = ['Id', 'Name', 'Zip_Code']
	success_url=reverse_lazy('')


class CountryUpdateView(UpdateView):
	template_name='.html'
	model=Country
	fields = ['Id', 'Name', 'Zip_Code']


class CountryDeleteView(DeleteView):
	template_name='.html'
	model=Country
	success_url=reverse_lazy('')


class CountryListView(generic.ListView):
	template_name = '.html'
	context_object_name = 'all_Country'
	def get_queryset(self):
		return Country.object.all


class CarsCreateView(CreateView):
	template_name='.html'
	model=Cars
	fields = ['Country', 'Mark', 'Type', 'Models', 'Price', 'Email', 'Color', 'EnginePower']
	success_url=reverse_lazy('')


class CarsUpdateView(UpdateView):
	template_name='.html'
	model=Cars
	fields = ['Country', 'Mark', 'Type', 'Models', 'Price', 'Email', 'Color', 'EnginePower']


class CarsDeleteView(DeleteView):
	template_name='.html'
	model=Cars
	success_url=reverse_lazy('')


class CarsListView(generic.ListView):
	template_name = '.html'
	context_object_name = 'all_Cars'
	def get_queryset(self):
		return Cars.object.all


class PriceCreateView(CreateView):
	template_name='.html'
	model=Price
	fields = ['price']
	success_url=reverse_lazy('')


class PriceUpdateView(UpdateView):
	template_name='.html'
	model=Price
	fields = ['price']


class PriceDeleteView(DeleteView):
	template_name='.html'
	model=Price
	success_url=reverse_lazy('')


class PriceListView(generic.ListView):
	template_name = '.html'
	context_object_name = 'all_Price'
	def get_queryset(self):
		return Price.object.all


class EnginePowerCreateView(CreateView):
	template_name='.html'
	model=EnginePower
	fields = ['Power', 'Capacity', 'Torque']
	success_url=reverse_lazy('')


class EnginePowerUpdateView(UpdateView):
	template_name='.html'
	model=EnginePower
	fields = ['Power', 'Capacity', 'Torque']


class EnginePowerDeleteView(DeleteView):
	template_name='.html'
	model=EnginePower
	success_url=reverse_lazy('')


class EnginePowerListView(generic.ListView):
	template_name = '.html'
	context_object_name = 'all_EnginePower'
	def get_queryset(self):
		return EnginePower.object.all

