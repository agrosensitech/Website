from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Plant(models.Model):
    common_name = models.CharField(_("Common Name"), max_length=50)
    scientific_name = models.CharField(_("Scientific Name"), max_length=50)
    image = models.ImageField(_("image"), upload_to="images/", )
    description = models.TextField(_("Description"))
    table_data = models.JSONField()
    references = models.TextField(_("Reference"))

    def __str__(self) -> str:
        return self.common_name

class Contact(models.Model):
    name = models.CharField(_("Name"),max_length=50)
    phone_no = models.CharField(_("Phone No"),max_length=50)
    email = models.CharField(_("Email"),max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name