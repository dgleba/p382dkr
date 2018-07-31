# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class NteNoteAdmin(admin.ModelAdmin):

    list_display = (
        'note_id',
        'note_fld',
        'tags_fld',
        'state_fld',
        'createdtime',
        'updatedtime',
        'datenote',
        'active',
    )
    list_filter = ('createdtime', 'updatedtime', 'datenote')
    #search_fields = ('note_fld', 'tags_fld')
    search_fields = ('state_fld', 'tags_fld')
    #search_fields = ( 'tags_fld')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.NteNote, NteNoteAdmin)
