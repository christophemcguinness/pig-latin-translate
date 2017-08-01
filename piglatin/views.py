from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def translate(request):

    orginal = request.GET['orginalText']

    translation = ''

    for words in orginal.split():
        if words[0].lower() in ('a', 'e', 'i', 'o', 'u'):
            #vowel
            translation += words[1:]
            translation += words[0]
            translation += 'yay '
        else:
            #consonant
            translation += words[1:]
            translation += words[0]
            translation += 'way '

    return render(request, 'translate.html', {'orginal': orginal, 'translation': translation})

def about(request):
    return render(request, 'about.html')
