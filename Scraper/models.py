from django.db import models

# This is the model for the scraper app

class Link(models.Model):

    address = models.CharField(max_length=2000,null=True, blank=True)
    name = models.CharField(max_length=2000 ,null=True, blank=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Scrape"
