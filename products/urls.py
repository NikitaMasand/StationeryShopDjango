from django.urls import path
from . import views

# '' means the root..i.e what comes as soon as you start the site. In our case it's products

urlpatterns = [
    path('', views.index), # we are not calling the index function, just passing the reference. django will take care of
    #calling it when needed
    path('new',views.new)
]
# in this list we map various urls to the view functions
