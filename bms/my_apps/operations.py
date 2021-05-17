from .models import bookmarkList

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

def get_bookmarks():
    bookmarks = bookmarkList.objects.all()
    bookmark_objects = []

    for bookmark in bookmarks:
        bookmark_objects.append(BookmarkModel(bookmark))
    
    return bookmark_objects
