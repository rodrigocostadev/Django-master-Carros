
# Signals mais utilizados:
# from django.db.models.signals import pre_save, pre_delete, post_save, post_delete

from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car

# sender, instance, **kwargs são parametros obrigatorios para o signals
@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print('### pre-save ###')
    print(instance)
    # instance contem os dados do carro, é uma instancia do carro que o usuario quer inserir no banco de dados
    # sender é o model (quem esta enviando esse evento para o signal), no caso a model Car
    # O que é uma função com o receiver? é uma função que esta ouvindo os eventos que estão chegando em uma determinada tabela

    # essa função vai estar ouvindo tudo o que acontece na tabela de carros em um evento pre-save


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print('### post-save ###')
    print(instance)

@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print('### pre-delete ###')
    print(instance)

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('### post-delete ###')
    print(instance)