
# Signals mais utilizados:
# from django.db.models.signals import pre_save, pre_delete, post_save, post_delete

from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from openai_api.client import get_car_ai_bio

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate( # o aggregate retorna uma campo personalizado na query (um campo que não existe)
        total_value=Sum('value')
    )['total_value'] # o aggregate retorna um dicionario, e com a chave total_value vai trazer o valor
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )

@receiver(pre_save, sender=Car) # receiver = escutador (fica atento/ouvindo ao salvar a model Car para executar a função)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ai_bio = get_car_ai_bio(
            instance.model, instance.brand, instance.model_year
        )
        # instance.bio = "Bio gerada automaticamente"
        instance.bio = ai_bio


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()



@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()



# # sender, instance, **kwargs são parametros obrigatorios para o signals
# @receiver(pre_save, sender=Car) # receiver = escutador (fica atento/ouvindo ao salvar a model Car para executar a função)
# def car_pre_save(sender, instance, **kwargs):
#     print('### pre-save ###')
#     print(instance)
#     # instance contem os dados do carro, é uma instancia do carro que o usuario quer inserir no banco de dados
#     # sender é o model (quem esta enviando esse evento para o signal), no caso a model Car
#     # O que é uma função com o receiver? é uma função que esta ouvindo os eventos que estão chegando em uma determinada tabela

#     # essa função vai estar ouvindo tudo o que acontece na tabela de carros em um evento pre-save


# @receiver(post_save, sender=Car)
# def car_post_save(sender, instance, **kwargs):
#     print('### post-save ###')
#     print(instance)

# @receiver(pre_delete, sender=Car)
# def car_pre_delete(sender, instance, **kwargs):
#     print('### pre-delete ###')
#     print(instance)

# @receiver(post_delete, sender=Car)
# def car_post_delete(sender, instance, **kwargs):
#     print('### post-delete ###')
#     print(instance)