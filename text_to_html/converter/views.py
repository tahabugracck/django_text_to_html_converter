from django.shortcuts import render
from .forms import TextForm
from .models import TextToHTML

def convert_text_to_html(request):
    form = TextForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        
        # HTML dönüşümü
        html_text = ''.join(f'<p>{line}</p>' for line in text.splitlines() if line.strip())
        
        # Veritabanına kaydet
        record = TextToHTML.objects.create(text=text, html=html_text)
        
        return render(request, 'result.html', {'html_text': html_text, 'record_id': record.id})
    
    return render(request, 'index.html', {'form': form})
