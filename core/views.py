from django.shortcuts import render

def index(request):
    try:
        return render(request, 'index.html')
    
    except Exception as e:
        return render(request, 'layouts/error.html', {'error_message': str(e)})
