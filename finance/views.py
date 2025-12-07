from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm, CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


def user_login(request):
    message = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("transaction_list")
            else:
                # User not found → show message
                message = "User not found. Please register first."
        else:
            message = "Invalid credentials. Please register if you are not registered."
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"form": form, "message": message})


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


@login_required
def edit_transaction(request, id):
    tr = get_object_or_404(Transaction, id=id, owner=request.user)
    form = TransactionForm(request.POST or None, instance=tr)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("transaction_list")
    return render(request, "finance/add_transaction.html", {"form": form})

@login_required
def delete_transaction(request, id):
    tr = get_object_or_404(Transaction, id=id, owner=request.user)
    if request.method == "POST":
        tr.delete()
        return redirect("transaction_list")
    return render(request, "finance/confirm_delete.html", {"transaction": tr})
