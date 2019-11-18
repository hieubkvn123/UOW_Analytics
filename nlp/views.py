from django.shortcuts import render
from .summarization import summarize
from .forms import TextSummarization

# Create your views here.
def nlp_text_summarization(response):
    # Check if there is any users loggin in:
    if(response.method == 'POST'):
        form = TextSummarization(response.POST)
        if(form.is_valid()):
            text = form.cleaned_data['text']
            original_charcount = len(text)
            original_wordcount = len(text.split(' '))

            summary = summarize(text)
            summary_wordcount = len(summary.split(' '))
            summary_charcount = len(summary)
            form = TextSummarization() # new form
            return render(response, 'nlp/summarization.html',{'original':text,
             'summary':summary,'original_wordcount':original_wordcount,
             'original_charcount':original_charcount,
             'summary_charcount':summary_charcount,
             'summary_wordcount':summary_wordcount,'form' : form})
    else:
        if(response.session['username'] == None or response.session['fullname'] == None):
            return render(response, 'nlp/error.html',{})
        else:
            form = TextSummarization()
            return render(response, 'nlp/summarization.html', {'form':form})
