from django.contrib import admin
from api.models import Client, Transaction
from django.db.models import Q



def get_summary(client, current_date, amount):
    criterion1 = Q(date__lt=current_date)
    criterion2 = Q(client=client)
    summary = client.initial_capital + amount
    query = Transaction.objects.filter(criterion1 & criterion2)
    if query:
        summary = sum([x.amount for x in query]) + client.initial_capital + amount
    return summary

class TransactionAdmin(admin.ModelAdmin):
    """TransacionAdmin model

    Args:
        admin ([type]): [description]
    """
    list_display = ('client', 'date', 'initial_capital', 'profit_loss', "summary")
    search_fields = ['client__name', 'date', 'amount']
    ordering = ('-date',)
    # readonly_fields=('summary', )

    def initial_capital(self, obj):
        return "$ {}".format(obj.client.initial_capital)
    
    def profit_loss(self, obj):
        return "$ {}".format(obj.amount)

    def summary(self, obj):
        return "$ {}".format(get_summary(obj.client, obj.date, obj.amount))

admin.site.register(Client)
admin.site.register(Transaction, TransactionAdmin)
admin.site.site_header = 'Crypto-Daily admin'

