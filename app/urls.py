
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view_teste, CarsListView, NewCarView
# from cars.views import cars_view_teste, CarsView, NewCarView,
# from cars.views import cars_view_teste, cars_view, new_car_view
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name="logout"),
    path('cars-teste/', cars_view_teste),
    # path('cars/', cars_view, name='cars_list'),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    # path('cars/', CarsView.as_view(), name='cars_list'),
    path('new_car/', NewCarView.as_view(), name='new_car'),
    # path('new_car/', new_car_view, name='new_car'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
