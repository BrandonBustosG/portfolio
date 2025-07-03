import reflex as rx
from portfolio.components.media import media
from portfolio.data import Media
from portfolio.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(rx.text("Brandon"), media(data), spacing=Size.SMALL.value)
