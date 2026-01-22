from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    categorys = models.CharField(max_length=100)
    discription = models.TextField()
    url = models.URLField()
    stackTool = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="portfolio/")


class Skill(models.Model):
    intro = models.TextField()
    categories = models.JSONField(default=list)

    def __str__(self):
        return "Skills Data"


class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} @ {self.company}"


class Education(models.Model):
    title = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    period = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    image = models.URLField()
    feedback = models.TextField()

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
