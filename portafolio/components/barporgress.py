import reflex as rx

def bar_progress(label: str, value: int) -> rx.Component:
    return rx.box(
        rx.text(label),
        rx.progress(value=value,),
        width="100%",
    )