from dominate.tags import *

def show_menu(menu_items):
    with ul(cls='menu'):
        for (fname, lnk, linkid) in menu_items:
            with li(cls='menu-item'):
                a(img(src=fname, id=linkid), cls='button', href=lnk)