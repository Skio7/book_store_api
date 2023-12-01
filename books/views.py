# books/views.py
from django.shortcuts import render
import requests

def book_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')

        # Set the maximum number of results you want
        max_results = 25

        # Make a request to the Google Books API
        api_key = 'AIzaSyBUBwEh8IFXh26H6Naballr5wEf7ujCckg'
        url = f'https://www.googleapis.com/books/v1/volumes?q={search_query}&maxResults={max_results}&key={api_key}'
        response = requests.get(url)
        data = response.json()

        # Extract relevant information from the API response
        books = []
        if 'items' in data:
            for item in data['items']:
                book_info = item['volumeInfo']
                title = book_info.get('title', 'N/A')
                authors = ', '.join(book_info.get('authors', ['Unknown']))
                description = book_info.get('description', 'No description available')
                thumbnail = book_info['imageLinks']['thumbnail'] if 'imageLinks' in book_info else None

                books.append({
                    'title': title,
                    'authors': authors,
                    'description': description,
                    'thumbnail': thumbnail,
                })

        return render(request, 'books/book_search.html', {'books': books, 'search_query': search_query})

    return render(request, 'books/book_search.html')
