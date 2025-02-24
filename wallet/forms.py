from dataclasses import fields
from django import forms
from .models import Card, Customer, Loan, Notification, Third_party
from .models import Currency
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Receipt
from .models import Third_party
from .models import Loan
from .models import Reward

# Use single import statement for simplicicty
# and to replace all the above codes
# from .models import *

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        
class CurrencyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = "__all__"

class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = "__all__"
        
class AccountRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = "__all__"
        
class TransactionRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Transaction
        fields = "__all__"

class ReceiptRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Receipt
        fields = "__all__"
        
class CardRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Card
        fields = "__all__"
        

class ThirdpartyRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Third_party
        fields = "__all__"
        

class NotificationRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Notification
        fields = "__all__"
        
class LoanRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Loan
        fields = "__all__"
        
class RewardRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Reward
        fields = "__all__"