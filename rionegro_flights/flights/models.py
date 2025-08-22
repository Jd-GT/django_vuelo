class Flight(models.Model):
    FLIGHT_TYPE_CHOICES = [
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=FLIGHT_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name