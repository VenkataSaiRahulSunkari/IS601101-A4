from django.shortcuts import render

def calculate_tip(request):
    if request.method == 'POST':
        # Get the bill amount and tip percentage from the form
        bill_amount = float(request.POST.get('bill_amount', 0))
        tip_percent = float(request.POST.get('tip_percent', 0))

        # Calculate the total bill
        tip_amount = (tip_percent / 100) * bill_amount
        total_bill = bill_amount + tip_amount

        # Render the result in the template
        return render(request, 'result.html', {'bill_amount': bill_amount, 'tip_percentage': tip_percent, 'tip_amount': tip_amount, 'total_bill': total_bill})

    return render(request, 'index.html')
