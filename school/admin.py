from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Notice)
admin.site.register(Free_board)
admin.site.register(Study_board)
admin.site.register(Contest_board)
admin.site.register(Graduate_board)
admin.site.register(Club_board)
admin.site.register(Market_board)

admin.site.register(Notice_Comment)
admin.site.register(Free_Comment)
admin.site.register(Study_Comment)
admin.site.register(Contest_Comment)
admin.site.register(Graduate_Comment)
admin.site.register(Club_Comment)
admin.site.register(Market_Comment)