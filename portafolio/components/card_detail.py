import reflex as rx
from portafolio.data import Service

from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size, glassmorphism


def card_detail(service: Service) -> rx.Component:
    return rx.vstack(
        rx.icon(
            service.icon,
            size=62
        ),
        rx.text.strong(
            service.title,
            align="center",
            as_="div"
        ),
        rx.text(
            service.description,
            size=Size.SMALL.value,
            color_scheme="gray",
            align="center", as_="div"
        ),
        align="center",
        width="100%",
        padding_y=EmSize.MEDIUM.value,
    )
