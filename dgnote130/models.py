from django.db import models

# Create your models here.

class NteNote(models.Model):
    note_id = models.IntegerField(primary_key=True)
    note_fld = models.TextField(blank=True)
    tags_fld = models.CharField(max_length=244, blank=True)
    state_fld = models.CharField(max_length=99, blank=True)
    createdtime = models.DateTimeField(blank=True, null=True)
    updatedtime = models.DateTimeField(blank=True, null=True)
    datenote = models.DateTimeField(blank=True, null=True)
    active = models.CharField(max_length=3, blank=True)
    #date1 = models.DateField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'nte_note'
