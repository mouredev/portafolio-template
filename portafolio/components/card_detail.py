from turtle import width
import reflex as rx

from portafolio.styles.styles import IMAGE_HEIGHT, Size


def card_detail() -> rx.Component:
    return rx.card(
        rx.inset(
            rx.image(
                src="/favicon.ico",
                height=IMAGE_HEIGHT,
                width="100%"
            ),
            pb=Size.DEFAULT.value
        ),
        rx.text(
            "Description",
            size=Size.SMALL.value,
            color_scheme="gray"
        ),
        width="100%"
    )
