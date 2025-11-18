from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.contrib import messages
from django.views import generic

from .models import Article,Comment
from .forms import CommentForm,ContactForm

class HomePageView(generic.ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'articles'

class ArticleDetailView(generic.DetailView):
    model = Article
    context_object_name = 'article'
    template_name = "articles_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = Comment.objects.filter(article=self.object, is_agree=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object   
            comment.save()

            messages.success(request, "نظر شما با موفقیت ثبت شد و پس از تایید نمایش داده می‌شود.")
            return redirect(request.path)

        messages.error(request, "خطایی رخ داد! لطفاً دوباره تلاش کنید.")
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)



def contact_register_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"با تشکر از شما")
        else:
            messages.error(request,"خطایی در برقراری ارتباط وجود دارد دوباره تلاش کنید یا با تیم پشتیبانی با شماره 09123456789 در ارتباط باشید.")
    else:
        form = ContactForm()
    return render(request,"contact.html",{'form':form})    