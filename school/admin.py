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

admin.site.register(No_comment)
admin.site.register(Fr_comment)
admin.site.register(St_comment)
admin.site.register(Co_comment)
admin.site.register(Gr_comment)
admin.site.register(Cl_comment)
admin.site.register(Ma_comment)