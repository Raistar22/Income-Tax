from django.urls import path
from .views import TaxSlabList, DeductionList, TaxPlanCreate, TaxPlanList, TaxPlanDelete

urlpatterns = [
    path('tax-slabs/', TaxSlabList.as_view(), name='tax-slab-list'),
    path('deductions/', DeductionList.as_view(), name='deduction-list'),
    path('tax-plans/', TaxPlanList.as_view(), name='tax-plan-list'),
    path('tax-plans/create/', TaxPlanCreate.as_view(), name='tax-plan-create'),
    path('tax-plans/delete/<int:pk>/', TaxPlanDelete.as_view(), name='tax-plan-delete'),
]
