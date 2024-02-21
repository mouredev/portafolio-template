import reflex as rx
from portafolio.components.media import media
from portafolio.styles.styles import Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.text("Nombre"),
        media(),
        spacing=Size.SMALL.value
    )
