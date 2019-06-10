from django.shortcuts import render


def home(request):
    return render(request, 'djangoproject/index.html')
    
def about(request):
    return render(request, 'djangoproject/about.html')
    
def result(request):
    text = request.GET['fulltext']
    words = text.split(" ")
    word_dictionary = {}
    
    for word in words:
        if word in word_dictionary:
            #1증가
            word_dictionary[word]+=1 
        else:
            #새롭게 1 생성
            word_dictionary[word]=1 
    
        
    return render(request, 'djangoproject/result.html', {'full' : text, 'total_t' : len(text),'total_w' : len(words), 'dictionary' : word_dictionary.items()})