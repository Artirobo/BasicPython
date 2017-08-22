from django.shortcuts import render , render_to_response

def  startpage(request):

    return render_to_response("startpage.html",{'name':'python'})

