from django.contrib import admin
from cars.models import Car, Brand



class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
    

# essa classe vai conter todas as configuações da minha sessão de administração dos meus carros
class CarAdmin(admin.ModelAdmin):
    # list_display são as colunas de dados que vão aparecer na tela de admin de todos os itens cadastrados
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    
    # search_fields é o campo de busca que vai aparecer na tela de admin de todos os itens cadastrados. ( VAI PROCURAR PELO MODELO )
    search_fields = ('model','brand')



admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin) # pede 2 argumentos (modelo e configurações de admin pra esse modelo )






