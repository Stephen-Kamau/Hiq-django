from django.shortcuts import render,redirect

from signup.models import signup_user
from .forms import loginfrm
from events.models import events_list
import datetime
# Create your views here.
def login(request):
    form = loginfrm(request.POST)
    error_var = ""
    sess = ""
    alredylog=""
    try:
        events_list.objects.filter(eventup_date__lte = datetime.datetime.now()).delete()

    except Exception as e:
        pass


    if request.method == 'POST':
        try:

            form = loginfrm(request.POST)
            logstats = signup_user.objects.get(Email = request.POST['email'])

        except:

            error_var = "no user with name exists"

            form = loginfrm(request.POST)
            return render (request , "./login/login.html" , context = {"form": form , "error":error_var ,"sess":sess , "alredy":alredylog})

        else:

            form = loginfrm(request.POST)

            if logstats.Password == request.POST["password"]:

                # if logstats.logstatus:
                #     alredylog = r"This account is already logged in, Please try again...."
                #
                # else:
                request.session["username"] = logstats.First_Name

                logstats.logstatus = True
                logstats.save()
                    # print()

                # request.session["email"] = signup_user.objects.get(Email = request.POST['email'])


                # set the username of the currrent user
                sess = request.session["username"]
                # set the session variable email address
                request.session["email"] = request.POST['email']

                # Expires immediately th user exits the browser
                request.session.set_expiry(0)

                # redirect users to their profile page
                return redirect("/")


            else:
                error_var = "Wrong credentials Please try again"
                return render (request , "./login/login.html" , context = {"form": form , "error":error_var ,"sess":sess , "alredy":alredylog})



    else:
        form = loginfrm(request.POST)
        return render (request , "./login/login.html" , context = {"form": form , "error":error_var ,"sess":sess , "alredy":alredylog})
