from django.shortcuts import render
from .forms import CustomerRegistrationForm
from .forms import CurrencyRegistrationForm
from .forms import WalletRegistrationForm
from .forms import AccountRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import ReceiptRegistrationForm
from .forms import CardRegistrationForm
from .forms import ThirdpartyRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import LoanRegistrationForm
from .forms import RewardRegistrationForm

# use from .forms import *
# also

# Create your views here.


def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request, 'wallet/register_customer.html',
                  {"form": form})


def register_currency(request):
    form = CurrencyRegistrationForm()
    return render(request, 'wallet/register_currency.html',
                  {"form": form})


def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request, 'wallet/register_wallet.html',
                  {"form": form})


def register_account(request):
    form = AccountRegistrationForm()
    return render(request, 'wallet/register_account.html',
                  {"form": form})


def register_transaction(request):
    form = TransactionRegistrationForm()
    return render(request, 'wallet/register_transaction.html',
                  {"form": form})


def register_receipt(request):
    form = ReceiptRegistrationForm()
    return render(request, 'wallet/register_transaction.html',
                  {"form": form})


def register_card(request):
    form = CardRegistrationForm()
    return render(request, 'wallet/register_card.html',
                  {"form": form})


def register_thirdparty(request):
    form = ThirdpartyRegistrationForm()
    return render(request, 'wallet/register_thirdparty.html',
                  {"form": form})


def register_notification(request):
    form = NotificationRegistrationForm()
    return render(request, 'wallet/register_notification.html',
                  {"form": form})


def register_loan(request):
    form = NotificationRegistrationForm()
    return render(request, 'wallet/register_loan.html',
                  {"form": form})


def reward_register(request):
    form = NotificationRegistrationForm()
    return render(request, 'wallet/reward_register.html',
                  {"form": form})
