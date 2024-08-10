# i have created this file for textutils
from django.http import HttpResponse
#template
from django.shortcuts import render

#bootstrap website index...
def index(request):
    return render(request,'index2.html')

def analyze(request):
# get the text
    
    dtext=request.POST.get('text','Default') # use for privacy
#chekbox values
    # removepunc=request.GET.get('removepunc','off')
    # fullcaps=request.GET.get("fullcaps",'off')
    # newlineremover=request.GET.get("newlineremover",'off')
    # extraspaceremover=request.GET.get("extraspaceremover",'off')
    # charactercounter=request.GET.get("charactercounter",'off')

# for security reason all get post converted into post request for use url=index2.html only 
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get("fullcaps",'off')
    newlineremover=request.POST.get("newlineremover",'off')
    extraspaceremover=request.POST.get("extraspaceremover",'off')
    charactercounter=request.POST.get("charactercounter",'off')
    numberremover = request.POST.get('numberremover','off')
    # print(removepunc)
    # print(dtext)

#check which chekbox on /////////////////////////////////////
    if removepunc=='on':
       punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
       analyzed=" "
       for char in dtext:
          if char not in punctuations:
              analyzed=analyzed+char
       
       params={'purpose':'Removing punctuations','analyzed_text':analyzed}
       dtext=analyzed # override
       #analyzed the text
      # return render(request,'analyze.html',params)
    # else:
    #     return HttpResponse ("error") for sinle check box run only
   
#check which chekbox on /////////////////////////////////////
    if(fullcaps=="on"):
        analyzed=""
        for char in dtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Change to UPPERCASE','analyzed_text':analyzed}
        dtext=analyzed

        # return render(request,'analyze.html',params)
    
#check which chekbox on /////////////////////////////////////    
    if(newlineremover=='on'):
       analyzed=""
       for char in dtext:
          if char != "\n" and char!="\r":
              analyzed=analyzed+char
          else:
              print("no")
    #    print("pre", analyzed)
       params={'purpose':'Removed New Line','analyzed_text':analyzed}
       
       #analyzed the text
    #    return render(request,'analyze.html',params)
    
#check which chekbox on /////////////////////////////////////    
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(dtext):
            # It is for if a extraspace is in the last of the string
            if char == dtext[-1]:
                    if not(dtext[index] == " "):
                        analyzed = analyzed + char

            elif not(dtext[index] == " " and dtext[index+1]==" "):                        
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        dtext = analyzed
       #analyzed the text
    #    return render(request,'analyze.html',params)

#check which chekbox on /////////////////////////////////////   
    if charactercounter=='on':
        analyzed=''
        count=0
        for char in dtext:
            if char.isalpha():
                count=count+1
                analyzed=count
        params={'purpose':'Character Count','analyzed_text':analyzed}
        #dtext=analyzed

#check which chekbox on /////////////////////////////////////      
    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in dtext:
            if char not in numbers:
                analyzed = analyzed + char
        
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        dtext = analyzed

## Return error if no options are selected
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and numberremover != "on"):
        return HttpResponse("please select any operation and try again")
    
    return render(request,'analyze.html',params)
   
def about(request):
    return render(request, 'about.html')
    
    