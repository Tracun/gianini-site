from django.db import models
from datetime import datetime
from typing import Any, TypeVar, Type, cast
import dateutil.parser
from products import controller

# Create your models here.


class Product(models.Model):

    uni = [
        ('Unitario', 'Unitário'),
        ('Caixa', 'Caixa'),
        ('Peca', 'Peça'),
        ('Metro', 'Metro'),
    ]

    id = models.IntegerField(primary_key=True, blank=False)
    name = models.CharField(max_length=120, blank=False, default="")
    description = models.CharField(max_length=120, blank=False, default="")
    quant = models.IntegerField(blank=False, default=0)
    unit = models.CharField(
        max_length=10,
        choices=uni,
        default=uni[0][0],
    )
    valueHospital = models.DecimalField(max_digits=100,
                                        decimal_places=2,
                                        default=0.0)
    valueRepresentante = models.DecimalField(max_digits=100,
                                           decimal_places=2,
                                           default=0.0)
    # _image=models.ImageField(upload_to='folder')
    image = models.URLField(
        max_length=1000, default="https://firebasestorage.googleapis.com/v0/b/gianini-manutencao.appspot.com/o/noImage.gif?alt=media&token=c6cca84a-595f-4efb-9ec1-6e71d21def77")
    createAt = models.CharField(
        editable=False, default=datetime.now, max_length=120)

    def save(self, *args, **kwargs):

        product = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "quant": self.quant,
            "unit": self.unit,
            "valueHospital": str(self.valueHospital),
            "valueRepresentante": str(self.valueRepresentante),
            "image": self.image,
            "createAt": str(self.createAt),
        }

        # print(product)

        print(controller.insert(product))
        return super(Product, self).save(*args, **kwargs)

