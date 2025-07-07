import reflex as rx
from portfolio.components.media import media
from portfolio.data import Media
from portfolio.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("Brandon Bustos Gaviria"),
        media(data),
        rx.text(
            "BUILDING SOFTWARE WITH ❤️ FROM COLOMBIA TO THE WORLD. CREATED WITH REFLEX.",
            size="1",
        ),
        spacing=Size.SMALL.value,
    )