import flet 
from flet import *
from flet import icons, colors

def apps(page:Page):
    page.window_width = 300
    page.window_height = 300
    page.add(
        TextField(label="Ismingiz nima:")
    )
