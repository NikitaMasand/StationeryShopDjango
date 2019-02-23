from django.urls import path
from . import views

# '' means the root..i.e what comes as soon as you start the site. In our case it's products

urlpatterns = [
    path('', views.index, name = 'index'), # we are not calling the index function, just passing the reference. django will take care of
    #calling it when needed
    path('new',views.new),
    path('add_new/',views.add_new, name='add_new'),
    path('shoppingcart/<int:pk>/', views.shoppingcart, name='shoppingcart'),
]
# in this list we map various urls to the view functions
