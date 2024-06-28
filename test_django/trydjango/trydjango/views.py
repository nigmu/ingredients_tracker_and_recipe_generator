# To render html web pages
from django.http import HttpResponse

from django.template.loader import render_to_string
from articles.models import Article


def home_view(request, id=None, *args, **kwargs):
    # Take in a request(Django sends the request)
    # Return HTML as a response(We pick the return response)

    # print(100000*5463546)

    # print(id)

    # from the database ??
    article_obj = Article.objects.latest('id')
    article_queryset = Article.objects.all()
    context = {
        "object_list" : article_queryset,
        "object" : article_obj, #if you dont want to use context dictionary
        "title" : article_obj.title,
        "id" : article_obj.id,
        "content" : article_obj.content
    }

    # Django Templates
    HTML_STRING = render_to_string("home_view.html", context=context)

    # article_title = article_obj.title
    # article_content = article_obj.content

    # name = "Nigam"
    # HTML_STRING = "<h1>{title}({id})</h1> <h3>{content}</h3>".format(**context)

    return HttpResponse(HTML_STRING)
