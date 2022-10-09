from genericpath import exists
from django.shortcuts import render, redirect    #redirect i import ediyoruz
#  kayıt ve login için gerekli importlar
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# messages i import ediyoruz uyarı mesajı
from django.contrib import messages

# Create your views here.

#kayıt ol fonksıyonum
def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']

        if sifre1 == sifre2:
            # burda kullanıcı adımızı filtreliyoruz
            if User.objects.filter(username = kullanici).exists():
                messages.error(request, 'Kullanıcı adı zaten alınmış')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Email kullanımda')
                return redirect('register')
            # len sifrem küçükse 6 dan hata ver    
            elif len(sifre1) < 6:
                messages.error(request, 'Şifre en az 6 karakter olması gerekiyor')
                return redirect('register')
            elif kullanici in sifre1:
                messages.error(request, 'Şifre ile kullanıcı adı benzer olamaz')
                return redirect('register')
            else:
                # hata yoksa kullanıcıyı oluşturur
                user = User.objects.create_user(username = kullanici, email = email, password = sifre1)
                user.save()
                messages.success(request, 'Kullanıcı oluşturuldu')
                return redirect('index')
        else:
            messages.error(request, 'Şifreler uyuşmuyor')
            return redirect('register')
    return render(request, 'register.html')
# giriş yapıldı fonksıyonum

def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş yaptınız')
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı')
            return redirect('login')
    return render(request, 'login.html')

# çıkış yapıldı fonksıyonum
def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış yapıldı')
    return redirect('index')