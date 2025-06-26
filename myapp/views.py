import requests
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


session_results = []

def index(request):
    global session_results
    session_results = []
    context = {}
    
    if request.method == 'POST':
        queries = request.POST.get('queries')
        api_key = 'a1589726ba91bf2d5ce0199a49bf774feac8cbd97237501d524a12ab2ca74090'

        if not queries:
            messages.error(request, "Please enter at least one query.")
            return render(request, 'index.html')

        query_list = [q.strip() for q in queries.split('\n') if q.strip()]
        all_results = []

        for query in query_list:
            try:
                response = requests.get('https://serpapi.com/search.json', params={
                    'q': query,
                    'engine': 'google',
                    "api_key" : 'a1589726ba91bf2d5ce0199a49bf774feac8cbd97237501d524a12ab2ca74090'

                })

                data = response.json()
                results = data.get('organic_results', [])

                for item in results:
                    all_results.append({
                        'query': query,
                        'title': item.get('title'),
                        'link': item.get('link'),
                        'snippet': item.get('snippet'),
                    })

            except Exception as e:
                messages.error(request, f"Error fetching data for '{query}': {e}")
        
        session_results = all_results
        context['results'] = all_results

    return render(request, 'index.html', context)


def download_csv(request):
    global session_results
    if not session_results:
        return HttpResponse("No data available to download.")

    df = pd.DataFrame(session_results)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="search_results.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response
