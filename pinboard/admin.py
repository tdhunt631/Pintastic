from django.contrib import admin
from pinboard.models import Pin, Board, Comment

class PinAdmin(admin.ModelAdmin):
	pass

class BoardAdmin(admin.ModelAdmin):
	pass

class CommentAdmin(admin.ModelAdmin):
	pass

admin.site.register(Pin, PinAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Comment, CommentAdmin)

