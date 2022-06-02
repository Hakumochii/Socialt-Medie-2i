from fileinput import filename
from urllib.parse import quote
import dominate
from dominate.tags import *

from sanic import Sanic
from config import APP_NAME

import pages.userprofile as userprofile
from pages.menu import show_menu
import database.post as post

def show_posts(posts=[], user=None):
    app = Sanic.get_app(APP_NAME)
    doc = dominate.document(title=f'{APP_NAME} | Posts')

    with doc.head:
        link(rel='stylesheet', href=app.url_for('static',
                                                name='static',
                                                filename='Frontpage.css'))

    with doc:
        with div(cls="header"):
            with div(cls="logo"):
                img(src=app.url_for('static', name='static', filename='images/Logo.png'))
            with div(cls="top_menu"):
                menu_items = [
                (app.url_for('static', name='static', filename='images/Home.png'), '/', 'home_icon'),
                (app.url_for('static', name='static', filename='images/Notifikation.png'), '/logout','heart_icon'),
                (app.url_for('static', name='static', filename='images/OpretPost.png'), '/write','post_icon'),
                (app.url_for('static', name='static', filename='images/Beskeder.png'), '/upload','besked_icon'),
                (app.url_for('static', name='static', filename='images/Profil.png'), '/profile','profile_icon')
            ]
            
                show_menu(menu_items)
                if user is not None:
                    userprofile.user_profile(user)
        
        hr(cls="line")

        with div(cls="Content2"):
            with div(cls="searchbar"):
                img(src=app.url_for('static', name='static', filename='images/search.png'))
            with div(cls="menu2"):
                img(src=app.url_for('static', name='static', filename='images/fællesskaber.png'))
            with div(cls="fox_mascot"):
                img(src=app.url_for('static', name='static', filename='images/Fox.png'))

        for display_post in posts:
            with div(cls='post'):
                
                with div(cls='post-header'):
                
                    with div(cls='profie-post'):
                        a(img(src=app.url_for('static', name='static', filename='images/profilbillede-post.png')), href=f'/u/{quote(display_post.author.username)}')
                
                    with div(cls='author_name'):   
                        a(f'{display_post.author.username}', href=f'/u/{quote(display_post.author.username)}')
            
                    with div(cls='report-post'):
                        img(src=app.url_for('static', name='static', filename='images/report.png'), id='report')
                
                with div(cls='post_contents'):
                    h1(display_post.post.title)
                    
                    img(src=app.url_for('static', name='static', filename='images/line.png'), id='line_post')
                    
                    if isinstance(display_post.post, post.TextPost): # text post
                        with div():
                            lines = filter(bool, display_post.post.contents.splitlines())
                            for par in lines:
                                p(par)
                    else: # image post
                        with div(cls='image_in_post'):
                            img(src=app.url_for('static', name='static',filename=f'images/posts/{display_post.post.image_path}'))
                    
                    with div(cls='post_bottom'):
                        img(src=app.url_for('static', name='static', filename='images/post-bottom.png'))
        
        
        
    return doc.render()

def create_image_page():
    app = Sanic.get_app(APP_NAME)
    doc = dominate.document(title=f'{APP_NAME} | Upload billede')

    with doc.head:
        link(rel='stylesheet', href=app.url_for('static',
                                                name='static',
                                                filename='style.css'))

    with doc:
        with div(cls="header"):
            with div(cls="logo"):
                img(src=app.url_for('static', name='static', filename='images/Logo.png'))
            menu_items = [
            (app.url_for('static', name='static', filename='images/Home.png'), '/', ''),
            (app.url_for('static', name='static', filename='images/OpretPost.png'), '/logout',''),
            (app.url_for('static', name='static', filename='images/OpretPost.png'), '/write',''),
            (app.url_for('static', name='static', filename='images/OpretPost.png'), '/upload',''),
            (app.url_for('static', name='static', filename='images/Profil.png'), '/profile','Profil')
        ]
        show_menu(menu_items)
        with form(cls='post-form', enctype='multipart/form-data', method='POST', action='/post/image'):
            with div(cls='post'):
                input_(type='text', cls='title_inp',
                        name='title',
                        placeholder='Indtast titel...')
                input_(type='file', name='image', accept='image/*')
            input_(type='submit', value='Post', cls='button')

    return doc.render()

def create_page():
    app = Sanic.get_app(APP_NAME)
    doc = dominate.document(title=f'{APP_NAME} | Skriv')

    with doc.head:
        link(rel='stylesheet', href=app.url_for('static',
                                                name='static',
                                                filename='style.css'))

    with doc:
        with div(cls="header"):
            with div(cls="logo"):
                img(src=app.url_for('static', name='static', filename='images/Logo.png'))
            menu_items = [
            (app.url_for('static', name='static', filename='images/Home.png'), '/', ''),
            (app.url_for('static', name='static', filename='images/OpretPost.png'), '/logout',''),
            (app.url_for('static', name='static', filename='images/OpretPost.png'), '/write',''),
            (app.url_for('static', name='static', filename='images/OpretPost.png'), '/upload',''),
            (app.url_for('static', name='static', filename='images/Profil.png'), '/profile','Profil')
        ]
        show_menu(menu_items)
        with form(cls='post-form', method='POST', action='/post/text'):
            with div(cls='post'):
                input_(type='text', cls='title_inp',
                        name='title',
                        placeholder='Indtast titel...')
                textarea(cls='contents_inp',
                            name='contents',
                            placeholder='Indtast tekst...')
            input_(type='submit', value='Post', cls='button')

    return doc.render()