from django.db import models

# Create your models here.

#* DATA MODEL

class Data(models.Model):
    address = models.TextField(verbose_name='address')
    lxp = models.IntegerField(verbose_name='LXP',default=0)
    rank = models.IntegerField(verbose_name='Rank',default=0)
    nfts = models.IntegerField(verbose_name='NFTs',default=0)

    def __str__(self):
        return (self.address)