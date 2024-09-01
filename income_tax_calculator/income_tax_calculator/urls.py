from django.contrib import admin
from django.urls import path, include
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import GetTaxSlabsView, CalculateTaxView, TaxPlanListView, DeleteTaxPlanView
from .views import ExportTaxPlanPDFView
from .views import CompareTaxPlansView
from your_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tax_calculator.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/calculate-tax/', views.CalculateTaxView.as_view(), name='calculate_tax'),
    path('api/tax-plan/<int:tax_plan_id>/export-pdf/', ExportTaxPlanPDFView.as_view(), name='export_tax_plan_pdf'),
    path('api/tax-plans/compare/', CompareTaxPlansView.as_view(), name='compare_tax_plans'),
    path('api/tax-slabs/<int:year>/', GetTaxSlabsView.as_view(), name='get_tax_slabs'),
    path('api/calculate-tax/', CalculateTaxView.as_view(), name='calculate_tax'),
    path('api/tax-plans/', TaxPlanListView.as_view(), name='tax_plan_list'),
    path('api/tax-plan/<int:tax_plan_id>/delete/', DeleteTaxPlanView.as_view(), name='delete_tax_plan'),

]
