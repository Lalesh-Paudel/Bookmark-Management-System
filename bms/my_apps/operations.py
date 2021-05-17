from .models import bookmarkList
import numpy as np

class BookmarkModel():

    def __init__(self, bookmark):
        self.bookmark = bookmark

    def get_id(self):
        return self.bookmark.id

    def get_sitename(self):
        return self.bookmark.site_name

    def get_siteurl(self):
        return self.bookmark.url

    def get_category(self):
        return self.bookmark.category

def get_bookmarks(category):
    bookmarks = bookmarkList.objects.all()
    bookmark_objects = []

    if category == 'all':
        for bookmark in bookmarks:
            bookmark_objects.append(BookmarkModel(bookmark))
    else:
        for bookmark in bookmarks:
            if bookmark.category == category:
                bookmark_objects.append(BookmarkModel(bookmark))

    return bookmark_objects

def get_categories():
    bookmarks = bookmarkList.objects.all()
    categories = []

    for bookmark in bookmarks:
        categories.append(bookmark.category)
    
    return np.unique(categories)
