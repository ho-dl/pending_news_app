from django.shortcuts import render ,redirect
from .models import News

# Create your views here.



def index(request):
    all_news = News.objects.all()
    return render(request, 'index.html', {'all_news': all_news})


from .models import News

def add_news(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        content = request.POST.get('content')
        images = request.POST.get('images')

        news = News(heading=heading, content=content,images=images)
        news.save()

        return redirect('index')  # Redirect to news list in admin panel
    
    return render(request, 'add_news.html')
