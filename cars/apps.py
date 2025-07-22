from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    # Função ready ativa o signals no app 
    def ready(self):
        import cars.signals # quando o app cars for inicializado, ele vai importar o arquivo signals

