from django.db import models

from tagify.models import TagField


class People(models.Model):
    name = models.CharField(max_length=30)
    languages = TagField(verbose_name='languages',delimiters=',', sort_values=False)
    test = TagField(enforce_whitelist = True, 
                    data_list = ["a", "b", "c"], 
                    duplicates=True, 
                    blank=True, 
                    tooltip_texts="{notAllowed : 'mag niet!'}", 
                    suggestions_chars=0, 
                    dropdown_include_selected=True)
