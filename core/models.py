from django.db import models


class Shipment(models.Model):
    tracking_number = models.CharField(max_length=100)
    carrier = models.CharField(max_length=100)
    sender_address = models.CharField(max_length=255)
    receiver_address = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    weather_condition = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['tracking_number']),
            models.Index(fields=['carrier']),
        ]


    @property
    def current_address(self):
        if self.status == 'in-transit' or self.status =='transit':
            return 'unknown'
        if self.status == 'delivery':
            return self.receiver_address
        if self.status == 'scanned' or self.status =='inbound-scan':
            return self.sender_address

class Article(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='articles')
    article_name = models.CharField(max_length=100)
    article_quantity = models.PositiveIntegerField()
    article_price = models.DecimalField(max_digits=10, decimal_places=2)
    SKU = models.CharField(max_length=100)
