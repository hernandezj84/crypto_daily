from django.db import models
from django.contrib.auth.models import auth


class Client(models.Model):
    """Client model

    Args:
        models ([type]): [description]
    """
    name = models.CharField(max_length=100, unique=True)
    initial_capital = models.DecimalField(decimal_places=2, max_digits=8)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    """Transaction model

    Args:
        models ([type]): [description]
    """
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateTimeField()
    amount = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return "{} {} ${}".format(self.client.name, self.date, self.amount)


# float(Transaction.objects.filter(client=c).aggregate(Sum('amount'))["amount__sum"])