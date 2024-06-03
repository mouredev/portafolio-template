import reflex as rx
from portafolio.components.card_detail import card_detail
from portafolio.components.heading import heading
from portafolio.data import Service
from portafolio.styles.styles import Size


def service(services: list[Service]) -> rx.Component:
    return rx.vstack(
        heading("Service"),
        heading("What can i do?"),
        rx.mobile_only(
            rx.vstack(
                *[
                    card_detail(service)
                    for service in services
                ],
                spacing=Size.DEFAULT.value
            ),
            width="100%"
        ),
        rx.tablet_and_desktop(
            rx.grid(
                *[
                    card_detail(service)
                    for service in services
                ],
                spacing=Size.DEFAULT.value,
                columns="4"
            ),
            width="100%"
        ),
        align="center",
        spacing=Size.MEDIUM.value,
        width="100%"
    )
