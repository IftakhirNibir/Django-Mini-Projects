from django.shortcuts import render
# Create your views here.

def home(request):
    person = [
        {'name':"Arif", 'age': 25},
        {'name':"Ifty", 'age': 23},
        {'name':"Nuha", 'age': 17}
    ]

    text = "ইসলামিক বিশেষজ্ঞরা বলছেন, মক্কায় প্রতি বছরই কোরবানি দেয়া হতো। কিন্তু তখন মক্কার বাসিন্দার বিভিন্ন দেবদেবীর নামে সেগুলো কোরবানি দিতেন। ফলে ইসলামের নবী সেই সময় মক্কায় থাকলেও তিনি এই রীতি অনুসরণ করতেন না। নবুয়ত প্রাপ্তির প্রায় তের বছর পরে মদিনায় হিজরত করার পর আনুষ্ঠানিকভাবে কোরবানি দেয়ার রীতি চালু হয়।"

    fruits = ['apple','mango','banana']
    return render(request,'index.html', context = {'person':person, 'text':text, 'fruits':fruits})





