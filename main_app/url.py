from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kits_index/', views.kits_index, name='kits_index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('strategies/', views.strategies_index, name='strategies_index'),
    path('strategies/<int:strategy_id>', views.strategies_detail, name='strategies_detail'),
    path('strategies/create/', views.StrategyCreate.as_view(), name='strategies_create'),
    path('kits/create/', views.KitCreate.as_view(), name='kits_create'),
    path('strategies/<int:pk>/update', views.StrategyUpdate.as_view(), name='strategies_update'),
    path('strategies/<int:pk>/delete', views.StrategyDelete.as_view(), name='strategies_delete'),
    path('kits/<int:pk>/', views.KitDetail.as_view(), name='kits_detail'),
    path('kits/<int:pk>/update', views.KitUpdate.as_view(), name='kits_update'),
    path('kits/<int:pk>/delete', views.KitDelete.as_view(), name='kits_delete'),
    path('states/add/<int:user_id>', views.add_state, name='add_state'),
    path('strategies/<int:strategy_id>/add_photo/', views.add_photo, name='add_photo'),
]