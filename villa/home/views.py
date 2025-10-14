from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def two_p(request):
    return render(request, 'rooms/2p.html')

def tree_p(request):
    return render(request, 'rooms/3p.html')

def four_p(request):
    return render(request, 'rooms/4p.html')

def tree_p_coc(request):
    return render(request, 'rooms/3p_coc.html')

def two_comf(request):
    return render(request, 'rooms/2p_c.html')

def tree_comf(request):
    return render(request, 'rooms/3p_c.html')

def two_f(request):
    return render(request, 'rooms/2_room.html')

def tree_ap(request):
    return render(request, 'rooms/3_room.html')

def house(request):
    return render(request, 'rooms/house.html')

def dop_inf(request):
    return render(request, 'inform.html')