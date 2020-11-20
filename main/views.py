from django.shortcuts import render
from upload.models import Animal,AnimalImages,Volunteer,Stories,Contact
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'main/home.html')

def adoption(request):
    return render(request,'main/adoption.html')

def volunteer(request):
    volunteers = Volunteer.objects.all()
    return render(request,'main/volunteer.html',{'volunteers':volunteers})

def stories(request):
    stories = Stories.objects.all()
    return render(request,'main/stories.html',{'stories':stories})

def storydetails(request,pk):
    ref = int(pk)
    story = get_object_or_404(Stories,id = ref)
    return render(request,'main/storydetails.html',{'story':story})

def donation(request):
    return render(request,'main/donation.html')

def about(request):
    return render(request,'main/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        message = request.POST['message']
        email = request.POST['email']
        if not name or not message or not email:
            messages.error(request, 'Complete all the necessary fields')
        else:
            c = Contact(name = name,email = email,message = message)
            c.save()
            messages.success(request, 'Suggestion is submitted successfully')
    return render(request,'main/contact.html')

def checklist(request):
    return render(request,'main/checklist.html')

def help(request):
    return render(request,'main/help.html')

def faq(request):
    return render(request,'main/faq.html')

def adoption_dog(request):
    anim = Animal.objects.all()
    dogs = []
    li = []
    for i in anim:
        if i.species == 'Dog':
            dogs.append(i)
            particular_anim = get_object_or_404(Animal,reference_no = i.reference_no)
            photos = AnimalImages.objects.filter(animal = particular_anim)
            li.append(photos[0].image.url)
            print(li)
    zipped_list = zip(dogs,li)
    return render(request,'main/adoption_dog.html',{"zipped_list":zipped_list})

def details(request, pk):
    ref = int(pk)
    particular_anim = get_object_or_404(Animal,reference_no = ref)
    photos = AnimalImages.objects.filter(animal = particular_anim)
    li = []
    for i in photos:
        li.append(i.image.url)
    print(li)
    return render(request,'main/details.html',{'particular_anim':particular_anim,'photos':photos,'li':li})

def adoption_cat(request):
    anim = Animal.objects.all()
    cats = []
    li = []
    for i in anim:
        if i.species == 'Cat':
            cats.append(i)
            particular_anim = get_object_or_404(Animal,reference_no = i.reference_no)
            photos = AnimalImages.objects.filter(animal = particular_anim)
            li.append(photos[0].image.url)
    zipped_list = zip(cats,li)
    return render(request,'main/adoption_cat.html',{"zipped_list":zipped_list})

def adoption_others(request):
    anim = Animal.objects.all()
    others = []
    li = []
    for i in anim:
        if i.species == 'Other':
            others.append(i)
            particular_anim = get_object_or_404(Animal,reference_no = i.reference_no)
            photos = AnimalImages.objects.filter(animal = particular_anim)
            li.append(photos[0].image.url)
    zipped_list = zip(others,li)
    return render(request,'main/adoption_others.html',{'zipped_list':zipped_list})
