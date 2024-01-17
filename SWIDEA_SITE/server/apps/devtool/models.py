from django.db import models


class Devtool(models.Model):
    dev_name = models.CharField(max_length=24)
    dev_type = models.CharField(max_length=24)
    dev_content = models.CharField(max_length=24)

    def __str__(self):
        return self.dev_name 