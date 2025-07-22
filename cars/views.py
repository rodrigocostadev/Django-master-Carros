from django.shortcuts import render, redirect
from django.http import HttpResponse
from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# CLASS BASED VIEW:

# # Usando a View
# class CarsView(View):

#     def get(self,request):
#         cars = Car.objects.all().order_by('brand__name')     
#         search = request.GET.get('search') 
#         if search:
#             cars = Car.objects.filter(model__icontains=search)        

#         return render(request, 'cars.html', {'cars': cars})
    
# Melhorando a CarsView utilizando ListView
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    # Usado para filtrar
    def get_queryset(self):
        queryset =  super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search) 
        return queryset   
    
class CarDetailView(DetailView):
    model = Car
    template_name = 'car-detail.html'
    


# class NewCarView(View):

#     def get(self, request):
#         new_car_form = CarModelForm()
#         return render (request, 'new-car.html', {'new_car_form':new_car_form})
    
#     def post(self,request):
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#         return render (request, 'new-car.html', {'new_car_form':new_car_form})
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new-car.html'
    success_url = '/cars/' # manda o usuario pra lista de carros, success_url é como se fosse o return redirect


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car-update.html'
    # success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car-delete.html'
    success_url = '/cars/'




# FUNCTION BASED VIEW:

# def cars_view(request):    
#     cars = Car.objects.all().order_by('brand__name')     
#     search = request.GET.get('search') 
#     if search:
#         cars = Car.objects.filter(model__icontains=search)        

#     return render(request, 'cars.html', {'cars': cars})





# def new_car_view(request):
#     if request.method == 'POST':
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#     else:
#         new_car_form = CarModelForm()
#     return render (request, 'new-car.html', {'new_car_form':new_car_form})




















def cars_view_teste(request):
    # return HttpResponse("<h1>Teste</h1>")
    
    cars = Car.objects.all().order_by('brand__name')       # mostra todos os carros disponiveis no banco de dados com as marcas em ordem alfabetica 
     
    search = request.GET.get('search') # Pega o valor da chave search, que é digitado pelo usuario na barra de urls ( requisição )
    
    # cars = Car.objects.filter(brand='2')     # Mostra a marca que tem o id = 2 (chave estrangeira)  ---  ( vai mostrar os carros da marca Chevrolet )
    
    ## O uso do "__" indica que estou acessando um campo da minha classe (ou coluna do meu banco de dados). 
    ## Como foi feito abaixo, estou acessando o campo brand do meu banco de dados e filtrando a palavra Fiat
    # cars = Car.objects.filter(brand__name='Fiat')    # Mostra todos os carros com a marca Fiat
    
    # cars = Car.objects.filter(model='Passat ls 1.5') # Mostra somente o carro especificado (precisa ser exatamente igual, não pode ter erros)
    
    ## O uso do "__" indica que estou acessando um campo da minha classe (ou coluna do meu banco de dados). 
    ## Como foi feito abaixo, estou acessando o campo model do meu banco de dados e filtrando todos os moodelos de carros com a letra p
    # cars = Car.objects.filter(model__contains='p') # Vai mostrar todos os modelos de carros que contem a letra "p", vai mostrar Passat ls e passat ts
    
    if search:
        # Na barra de busca utilizar depois de /cars/  ((    ?search=marea  )) para filtrar e mostrar apenas o marea
        cars = Car.objects.filter(model__icontains=search) # O icontains ignora se as letras estão em caixa alta ou em caixa baixa
        

    return render(request, 'cars-teste.html', {'cars': cars})





