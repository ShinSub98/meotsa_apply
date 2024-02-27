from django.contrib import admin
from .models import Apply

#account의 admin을 참고해주세요
@admin.register(Apply)
class Applyadmin(admin.ModelAdmin):
    """"Admin View for Apply"""
    
    list_display = (
        "user",
        "is_submitted",
        "get_accepted"
    )
    #admin에서 수정할 수 없는 그러니까 오직 읽을 수만 있는 필드를 지정합니다. 
    readonly_fields = (
        "user",
        "category",
        "study_url",
        "first_q",
        "second_q",
        "third_q",
        "fourth_q",
        "created_at",
        "updated_at",
        "is_submitted",
    )

    def get_accepted(self, obj):
        return obj.user.is_accepted
    get_accepted.short_description = "합격 여부"