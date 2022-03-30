from django.apps import AppConfig


class OrderproductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orderProducts'

    def ready(self):
        import orderProducts.signals

