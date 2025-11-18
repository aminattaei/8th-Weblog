from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Article(models.Model):
    categories = models.ManyToManyField(Category, verbose_name=_("categories"))
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, verbose_name=_("articles"), on_delete=models.CASCADE
    )
    created_time = models.DateField(
        _("date to create"), auto_now=False, auto_now_add=True
    )
    updated_time = models.DateField(
        _("date t update"), auto_now=True, auto_now_add=False
    )
    picture = models.ImageField(upload_to="Articles/Pictures/")

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Article_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user_name = models.CharField(max_length=50) 
    user_email = models.EmailField(max_length=254)
    user_comment = models.TextField()
    is_agree = models.BooleanField(_("agree to send comment"), default=False)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.user_name or self.user_email


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField(_("Your messages"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})
