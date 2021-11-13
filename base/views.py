from django.shortcuts import render

# Create your views here.


rooms = [
    {"id": 1, "name": 'Let\'s learn python !'},
    {"id": 2, "name": 'Front-end Developers'},
    {"id": 3, "name": 'design with me !'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for rm in rooms:
        if rm['id'] == int(pk):
            room = rm
    context = room
    print(context)
    return render(request, 'base/room.html', context)
