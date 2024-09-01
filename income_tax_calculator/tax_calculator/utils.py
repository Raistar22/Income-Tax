from .models import TaxSlab

def calculate_tax(income, year, slab_type, deductions):
    slabs = TaxSlab.objects.filter(year=year, slab_type=slab_type).order_by('income_from')
    total_tax = 0
    remaining_income = income

    for slab in slabs:
        if slab.income_to is None or remaining_income > slab.income_to:
            taxable_income = slab.income_to - slab.income_from if slab.income_to else remaining_income - slab.income_from
        else:
            taxable_income = remaining_income - slab.income_from

        if taxable_income > 0:
            total_tax += (taxable_income * slab.rate) / 100
            remaining_income -= taxable_income

    for deduction, amount in deductions.items():
        total_tax -= amount

    return max(total_tax, 0)  # Ensure tax is not negative
