from dominate.tags import *

def show_menu(menu_items):
    with ul(cls='menu'):
        for (img, lnk) in menu_items:
            with li(cls='menu-item'):
                a(img, cls='button', href=lnk)