import reflex as rx

from portfolio import data
from portfolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portfolio.views.header import header
from portfolio.views.about import about
from portfolio.views.extra import extra
from portfolio.views.info import info
from portfolio.views.footer import footer
from portfolio.views.tech_stack import tech_stack
from portfolio.components.heading import heading

DATA = data.data


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        rx.script("document.documentElement.lang='es'"),
        rx.theme_panel(default_open=False),
        rx.vstack(
            # rx.color_mode.button(position="top-right"),
            header(DATA),
            about(DATA.about),
            rx.divider(),
            tech_stack(DATA.technologies),
            info("Experiencia", DATA.experience),
            info("Proyectos", DATA.projects),
            heading("Más proyectos en desarrollo..."),
            rx.divider(),
            info("Formación", DATA.training),
            extra(DATA.extras),
            rx.divider(),
            footer(DATA.media),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%",
        ),
    )


app = rx.App(
    stylesheets=STYLESHEETS, 
    style=BASE_STYLE, 
    theme=rx.theme(
        accent_color="indigo"
    )
)

title = DATA.title
description = DATA.description
image = DATA.image

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image},
        {"char_set": "UTF-8"},
    ],
)
