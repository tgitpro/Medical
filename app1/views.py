from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import RegModel,Address,BlogModel
from .serializers import BlogModelSerializer

# Create your views here.

def indexr(request):
    return render(request, 'index.html')

def regr(request):
    return render(request, 'register.html')

def doctor_reg(request):
    return render(request, 'doctor-reg.html')

def patient_reg(request):
    return render(request, 'patient-reg.html')

def reg(request):
    if request.method == 'POST':
        fn=request.POST.get('fname')
        ln=request.POST.get('lname')
        pic=request.FILES['propic']
        un=request.POST.get('uname')
        em=request.POST.get('mail')
        pas=request.POST.get('cpsw')
        line=request.POST.get('line1')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        type=request.POST.get('utype')

        user_instance=RegModel(fname=fn,lname=ln,propic=pic,uname=un,email=em,psw=pas,utype=type)
        user_instance.save()
        Address(user=user_instance,line=line,city=city,state=state,pincode=pincode).save()
    return redirect(indexr)


def loginr(request):
    return render(request,'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        try:
            user = RegModel.objects.get(uname=username, psw=password)
            request.session['user_id'] = user.id
            request.session['typeu']=user.utype
            address = Address.objects.get(user=user)
            if user.utype == 'doctor':
                return render(request, 'doctor-dashboard.html', {'data': user,'address': address})
            else:
                return render(request, 'patient-dashboard.html', {'data': user,'address': address})

        except RegModel.DoesNotExist:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def logout(request):
    del request.session['user_id']
    return redirect(indexr)


def blogr(request):
    return render(request, 'blogr.html')

def bupload(request):
    uid=request.session.get('user_id')
    if request.method == 'POST':
        title=request.POST.get('btitle')
        image=request.FILES['bimg']
        category=request.POST.get('bcategory')
        summary=request.POST.get('bsummary')
        content=request.POST.get('bcontent')
        status=request.POST.get('bstatus')
        if status==None:
            status=True

        user=RegModel.objects.get(id=uid)

        blog_instance=BlogModel(btitle=title,bimage=image,bcategory=category,bsummary=summary,bcontent=content,bstatus=status,buser=user)
        blog_instance.save()

        if blog_instance.bstatus==False:
            draftdata=BlogModel.objects.filter(bstatus=False).filter(buser_id=uid)

        else:
            draftdata=BlogModel.objects.filter(bstatus=True).filter(buser_id=uid)

    return redirect(blogr)

def draft_data(request):
    uid=request.session.get('user_id')
    dobj=BlogModel.objects.filter(bstatus=False,buser_id=uid)
    return render(request,'blog-display.html',{'dobj':dobj})

def post_data(request):
    uid=request.session.get('user_id')
    dobj=BlogModel.objects.filter(bstatus=True,buser_id=uid)
    return render(request,'blog-display.html',{'dobj':dobj})

def blogform(request):
    return render(request,'blog-form.html')

def allblog(request):
    alldata=BlogModel.objects.filter(bstatus=True)
    serializer = BlogModelSerializer(alldata, many=True)
    serialized_data = serializer.data

    return JsonResponse(serialized_data, safe=False)

def category_blog(request,category):
    try:
        categorydata=BlogModel.objects.filter(bstatus=True,bcategory=category)
        serializer = BlogModelSerializer(categorydata, many=True)
        serialized_data = serializer.data
        return JsonResponse(serialized_data, safe=False)
    except BlogModel.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def update_blog(request,id):
    data=BlogModel.objects.get(id=id)
    return render(request,'update_blog.html',{'data':data})

def delete_blog(request,id):
    BlogModel.objects.get(id=id).delete()
    return render(request,'blog-display.html')

def publish_blog(request,id):
    data=BlogModel.objects.get(id=id)
    data.bstatus=True
    data.save()
    return render(request,'blog-display.html')

def view_blog(request,id):
    data=BlogModel.objects.get(id=id)
    return render(request,'view_blog.html',{'data':data})







