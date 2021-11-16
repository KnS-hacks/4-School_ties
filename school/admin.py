from django.contrib import admin
from .models import Notice, Free_board, Study_board, Club_board, Contest_board, Graduate_board, Market_board

# Register your models here.
admin.site.register(Notice)
admin.site.register(Free_board)
admin.site.register(Study_board)
admin.site.register(Contest_board)
admin.site.register(Graduate_board)
admin.site.register(Club_board)
admin.site.register(Market_board)