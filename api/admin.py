from django.contrib import admin
from .models import (
    Portfolio,
    Skill,
    Experience,
    Education,
    Feedback,
    ContactMessage,
)

# -------------------- PORTFOLIO --------------------
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "title",
        "categorys",
        "date",
        "url",
    )
    search_fields = ("name", "title", "categorys", "stackTool")
    list_filter = ("categorys",)
    ordering = ("-id",)


# -------------------- SKILLS --------------------
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "intro")
    ordering = ("id",)


# -------------------- EXPERIENCE --------------------
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "period")
    search_fields = ("title", "company")
    ordering = ("-id",)


# -------------------- EDUCATION --------------------
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("title", "institution", "period")
    search_fields = ("title", "institution")
    ordering = ("-id",)


# -------------------- FEEDBACK --------------------
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")
    ordering = ("-id",)


# -------------------- CONTACT MESSAGES --------------------
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
