from django.urls import path
from .views import (
    LaboratorioListView,
    LaboratorioCreateView,
    LaboratorioUpdateView,
    LaboratorioDeleteView
)

urlpatterns = [
    path('mostrar/', LaboratorioListView.as_view(), name='laboratorio_list'),
    path('ingresar/', LaboratorioCreateView.as_view(), name='laboratorio_create'),
    path('modificar/<int:pk>/', LaboratorioUpdateView.as_view(),
         name='laboratorio_update'),
    path('eliminar/<int:pk>/', LaboratorioDeleteView.as_view(),
         name='laboratorio_delete'),
]
