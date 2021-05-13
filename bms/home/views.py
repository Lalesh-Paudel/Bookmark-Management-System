from django.apps.config import AppConfig
from django.db.models.manager import BaseManager
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    # context = {
    #     # 'bookmarks': bookmarkList.objects.all(),
    #     'bookmarks': inputs.modles.bookmarkList.get_bookmarks()
    #     # models.get_bookmarks
    # }
    print('hello workd this is working')
    # print(inputs.modles.bookmarkList.get_bookmarks())

    return render(request, 'Home.html', context={})


# def load_bookmarks(category_name="all"):
#     html = ""
#     bookmarks = bookmarkList.objects.all()
#     for bookmark in bookmarks:
#         html += "{}".format(
#             "<div class='bookmark_wrapper'>"
#                 +"<div class='top'>"
#                     +"<span>facebook </span>"
#                     +"<svg width='24' height='24' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'>"
#                         +"<path d='M12 8C13.1 8 14 7.1 14 6C14 4.9 13.1 4 12 4C10.9 4 10 4.9 10 6C10 7.1 10.9 8 12 8ZM12 10C10.9 10 10 10.9 10 12C10 13.1 10.9 14 12 14C13.1 14 14 13.1 14 12C14 10.9 13.1 10 12 10ZM12 16C10.9 16 10 16.9 10 18C10 19.1 10.9 20 12 20C13.1 20 14 19.1 14 18C14 16.9 13.1 16 12 16Z' fill='#323232'/>"
#                     +"</svg>"
#                     +"<div class='more_options' title='click'>"
#                         +"<ul>"
#                             +"<li>remove</li>"
#                             +"<li>update</li>"
#                         +"</ul>"
#                     +"</div>"
#                 +"</div>"

#                 +"<div class='bottom'>"
#                     +"<div class='highlight'> open </div>"
#                 +"</div>"
#             +"</div>"
#         )

#         return html

# def load_categorys():
#     pass