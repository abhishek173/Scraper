from django.shortcuts import render
from django.http import JsonResponse
from .script import scrape_imdb_news
from .models import News
# Create your views here.


def run_scraper(request):
    scrape_imdb_news()
    return JsonResponse({
        "status": True,
        "message": "Scraper Executed.."
    })

def index(request):

    return render(request,'index.html',context={
        "news_data":News.objects.all()
    })