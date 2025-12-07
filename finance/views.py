from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm, CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("transaction_list")
    return render(request, "finance/register.html", {"form": form})


@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(owner=request.user)
    return render(request, "finance/transaction_list.html", {"transactions": transactions})


@login_required
def add_transaction(request):
    form = TransactionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        tr = form.save(commit=False)
        tr.owner = request.user
        tr.save()
        return redirect("transaction_list")
    return render(request, "finance/add_transaction.html", {"form": form})
