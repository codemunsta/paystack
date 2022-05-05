from django.db import models
import secrets


class Payment(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    ref = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = '-date_created'

    def __str__(self):
        return f'{self.name} payment of {self.amount}'

    def save(self, *args, **kwargs):
        while self.ref is None:
            ref = secrets.token_urlsafe(50)
            if Payment.objects.filter(ref=ref) is None:
                self.ref = ref
        super().save(*args, **kwargs)

    def amount_value(self) -> int:
        return self.amount * 100

# Create your models here.
