from django.shortcuts import render, redirect

# Create your views here.


def open_session(request):
    if 'counter' in request.session:
        request.session['counter'] = request.session['counter'] + 1
        print('existe', request.session['counter'])
    else:
        request.session['counter'] = 0
        print('no existo')
    return render(request, 'index.html')


def destroy_session(request):
    del request.session['counter']
    return redirect('/')
