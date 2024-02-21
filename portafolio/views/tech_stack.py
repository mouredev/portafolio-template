import reflex as rx
from portafolio.components.heading import heading
from portafolio.styles.styles import Size


def tech_stack() -> rx.Component:
    return rx.vstack(
        heading("Tecnologías"),
        rx.flex(
            *[
                rx.badge(
                    rx.icon("code"),
                    rx.text(f"Stack{index}"),
                    size="2"
                )
                for index in range(0, 10)
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )
