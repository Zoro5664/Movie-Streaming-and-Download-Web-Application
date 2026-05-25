from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User,auth
import mysql.connector as c
from requests import request
from M_downloader import settings
from .models import m_details
from django.contrib import messages
from django.contrib.auth import logout,login
import smtplib


# Create your views here.
def index(request):
    details = m_details.objects.all()
    if 'uname' in request.session:
        return render(request,"home.html",{'movies':details,'uname':'uname'})
    else:
        return render(request,"index.html",{'movies':details})
    # return HttpResponse("This is homepage")
def about(request):
    return HttpResponse("This is  about homepage")

def login(request):
    return render(request,"login.html")

def signup(request):
        return render(request,"signup.html")

def home(request):
    if 'uname' in request.session:
        details = m_details.objects.all()
        return render(request,"home.html",{'movies':details,'uname':'uname'})
    else:
        return render(request,"login.html")

def movie(request):
    return render(request,"movies.html")


def register(request):
    if request.method=="POST":
        name = request.POST['name']
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                return HttpResponse("username already taken")
            else:
                user=User.objects.create_user(username=username,email=email,first_name=name,password=password)
                user.save()
                print("party now  "+name)
                return redirect("/")
        else:
            return HttpResponse("pass do not match")

    else:
        return render(request,"signup.html")

def loginn(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            request.session['uname']=username
            return redirect("home")
        else:
            messages.error(request,"Invalid credentials")
            return redirect("/login.html")
        



    else:
        return render(request,'login.html')
    

def logoutt(request):
    logout(request)
    return redirect("/")


from PIL import Image
from io import BytesIO

def add(request):
    if request.method == "POST":
        prod = m_details()
        prod.name = request.POST.get('mname')
        prod.description = request.POST.get('desc')
        prod.tlink = request.POST.get('tlink')
        prod.mlink = request.FILES['mlink']
        prod.category = request.POST.get('cat')
        image = request.FILES['img']
        
        # Use Pillow to resize the image to 4:3 aspect ratio
        img_data = BytesIO(image.read())
        img = Image.open(img_data)
        width, height = img.size
        target_width = int(height * 5 / 4)
        target_height = height
        if width > target_width:
            target_height = int(width * 5 / 4)
            target_size = (target_width, target_height)
        else:
            target_size = (width, height)
        img = img.resize(target_size)
        
        # Save the resized image to a new BytesIO object
        output_data = BytesIO()
        img.save(output_data, format='JPEG')
        
        # Save the image to the model
        prod.image.save(image.name, output_data)
        prod.save()
        
    
    return render(request,"add_movie.html")



def player(request, tlink,name,description):
    context = {'tlink': tlink,'name':name,'description':description}
    return render(request,'player.html', context)

def contact(request):
    return render(request,"contact.html")
    
def send_email(request):
    if request.method=='POST':

        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('sumitpawar0759@gmail.com', 'jctxzxbzdglluxls')
        # Get the recipient, subject, and message from the form
        to = "arjun98999899+contact@gmail.com"
        name=request.session['uname']
        subject = request.POST['emaill']
        message = request.POST['message']

        # Send the email
        msg = f'Subject: {name}\n\n{subject}\n\n{message}'
        server.sendmail('sumitpawar0759@gmail.com', to, msg)

        # Close the server
        server.quit()
        messages.success(request,"sent")
        return redirect("contact")
    


def video_player(request,mlink,name,description):
    # video_url = '/static/movies/Snap x Baarishen - Mashup (Full Version) - Gravero & TP.mp4' # change this to the URL of your video file
    video_url = "/Images/" + str(mlink)
    context = {'video_url': video_url,'name':name,'description':description}
    return render(request, 'mplayer.html', context)
