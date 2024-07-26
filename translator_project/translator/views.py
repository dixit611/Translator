# translator/views.py

import json
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse
from googletrans import Translator
from django.urls import reverse

translator = Translator()

def voice_command(request):
    return render(request, 'translator/voice_command.html')


def home(request):
    messages = [
        ("left", "राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम राम ", "red"),
        ("right", "राधे राधे राधे राधे राधे राधे राधे राधे राधे राधे राधे राधेराधे राधे राधेराधे राधे राधे राधे राधे राधे राधे राधे राधे राधे राधे राधे राधे राधे राधे राधे राधे राधेराधे राधे राधेराधे राधे राधे", "red"),
    ]
    context = {
        'messages': messages,
    }
    return render(request, 'translator/home.html',context)

def about(request):
    return render(request, 'translator/about.html')

def send_email(request):
    try:
        subject = 'Subject here'
        message = 'Here is the message.'
        from_email = 'dixitaman611@gmail.com'
        recipient_list = ['dixitaman611@gmail.com', 'kalilinuxforaman611@gmail.com']

        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Email sent')
    except BadHeaderError as e:
        return HttpResponse('Invalid header found.')

def contact(request):
    if request.method == 'POST':
        # Process form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        state = request.POST.get('state')
        
        # Do something with the data, e.g., save to database, send an email, etc.
        
        return HttpResponseRedirect(reverse('contact_success'))  # Redirect after POST

    states = [
        ("AP", "Andhra Pradesh"),
        ("AR", "Arunachal Pradesh"),
        ("AS", "Assam"),
        ("BR", "Bihar"),
        ("CG", "Chhattisgarh"),
        ("GA", "Goa"),
        ("GJ", "Gujarat"),
        ("HR", "Haryana"),
        ("HP", "Himachal Pradesh"),
        ("JK", "Jammu and Kashmir"),
        ("JH", "Jharkhand"),
        ("KA", "Karnataka"),
        ("KL", "Kerala"),
        ("MP", "Madhya Pradesh"),
        ("MH", "Maharashtra"),
        ("MN", "Manipur"),
        ("ML", "Meghalaya"),
        ("MZ", "Mizoram"),
        ("NL", "Nagaland"),
        ("OR", "Odisha"),
        ("PB", "Punjab"),
        ("RJ", "Rajasthan"),
        ("SK", "Sikkim"),
        ("TN", "Tamil Nadu"),
        ("TG", "Telangana"),
        ("TR", "Tripura"),
        ("UP", "Uttar Pradesh"),
        ("UK", "Uttarakhand"),
        ("WB", "West Bengal"),
        ("AN", "Andaman and Nicobar Islands"),
        ("CH", "Chandigarh"),
        ("DN", "Dadra and Nagar Haveli and Daman and Diu"),
        ("DL", "Delhi"),
        ("LD", "Lakshadweep"),
        ("PY", "Puducherry"),
    ]
    context = {
        'states': states,
    }
    return render(request, 'translator/contact.html', context)

def contact_success(request):
    return render(request, 'translator/contact_success.html')

def translate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text')
        src_lang = data.get('src_lang')
        dest_lang = data.get('dest_lang')
        
        if not text or not src_lang or not dest_lang:
            return JsonResponse({'error': 'Invalid input'}, status=400)
        
        try:
            translation = translator.translate(text, src=src_lang, dest=dest_lang)
            translated_text = translation.text
            return JsonResponse({'translated_text': translated_text})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

def convert_text_to_speech(request):
    if request.method == 'POST':
        # Assuming voice input is sent as base64 encoded audio or similar
        audio_data = request.POST.get('audio_data')  # Replace with actual field name
        
        # Implement logic to convert audio_data to text (using speech recognition)
        # For example, using a hypothetical function `convert_audio_to_text(audio_data)`
        try:
            text = convert_audio_to_text(audio_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
        # Assuming you have extracted the language from the voice input
        src_lang = 'auto'  # Adjust based on actual implementation
        
        dest_lang = 'en'  # Assuming default destination language
        
        try:
            translation = translator.translate(text, src=src_lang, dest=dest_lang)
            translated_text = translation.text
            return JsonResponse({'translated_text': translated_text})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)



