from django.db import models

# Create your models here.
class Notice_board_details(models.Model):
    uni_name = models.TextField(null=False, blank= False)
    uni_category = models.TextField(null=False, blank= False)
    uni_url = models.TextField(null= False, blank= False)

    def __str__(self):
        return str(self.uni_name)