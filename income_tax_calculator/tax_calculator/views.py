from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TaxSlab, TaxPlan
from .serializers import TaxPlanSerializer
import json

class GetTaxSlabsView(APIView):
    def get(self, request, year):
        slabs = TaxSlab.objects.filter(year=year)
        slabs_data = [{"start": slab.slab_start, "end": slab.slab_end, "rate": slab.rate} for slab in slabs]
        return Response(slabs_data)

class CalculateTaxView(APIView):
    def post(self, request):
        data = request.data
        year = data.get("year")
        income = data.get("income")
        deductions = data.get("deductions", {})

        # Get tax slabs
        slabs = TaxSlab.objects.filter(year=year)
        tax = calculate_tax(income, slabs)

        # Apply deductions
        total_deductions = sum(deductions.values())
        taxable_income = max(0, income - total_deductions)
        tax = calculate_tax(taxable_income, slabs)

        tax_plan = TaxPlan.objects.create(
            user=request.user,
            year=year,
            income=income,
            deductions=deductions,
            tax=tax
        )

        serializer = TaxPlanSerializer(tax_plan)
        return Response(serializer.data)

def calculate_tax(income, slabs):
    tax = 0
    for slab in slabs:
        if income > slab.slab_start:
            taxable_amount = min(income, slab.slab_end) - slab.slab_start
            tax += taxable_amount * slab.rate / 100
        else:
            break
    return tax

class TaxPlanView(APIView):
    def post(self, request):
        data = request.data
        year = data.get("year")
        income = data.get("income")
        deductions = data.get("deductions", {})

        # Calculate tax logic
        tax = calculate_tax(income, year)  # Add logic to fetch slabs and calculate

        # Save tax plan
        tax_plan = TaxPlan.objects.create(
            user=request.user,
            year=year,
            income=income,
            deductions=deductions,
            tax=tax
        )

        return Response({"message": "Tax plan saved successfully", "tax_plan_id": tax_plan.id})

    # Implement the DELETE method for deleting tax plans if required
    def delete(self, request, pk):
        try:
            tax_plan = TaxPlan.objects.get(pk=pk, user=request.user)
            tax_plan.delete()
            return Response({"message": "Tax plan deleted successfully"})
        except TaxPlan.DoesNotExist:
            return Response({"error": "Tax plan not found"}, status=status.HTTP_404_NOT_FOUND)
