from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=50,unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, verbose_name=_("articles"), on_delete=models.CASCADE)
    created_time = models.DateField(_("date to create"), auto_now=False, auto_now_add=True)
    updated_time = models.DateField(_("date t update"), auto_now=True, auto_now_add=False)
    picture = models.ImageField(upload_to='Articles/Pictures/')

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Article_detail", kwargs={"pk": self.pk})

