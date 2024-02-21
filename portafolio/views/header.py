import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.styles.styles import Size


def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(size=Size.BIG.value),
        rx.vstack(
            heading("Nombre", True),
            heading("Habilidad principal"),
            rx.text(
                rx.icon("map-pin"),
                "Localización",
                display="inherit"
            ),
            media(),
            spacing=Size.SMALL.value,
        ),
        spacing=Size.DEFAULT.value,
    )
