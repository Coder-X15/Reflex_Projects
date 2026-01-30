"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

class ButtonState(rx.State):
    """ A counter statekeeper"""
    count : int = 0

    @rx.event
    def increment(self):
        """Increment the counter."""
        self.count += 1

    @rx.event
    def decrement(self):
        """Decrement the counter."""
        self.count -= 1



def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            rx.heading(ButtonState.count, size="5"),
            rx.hstack(
                rx.button("Increment", on_click=ButtonState.increment),
                rx.button("Decrement", on_click=ButtonState.decrement),
            ),
            spacing="5",
            justify="center",
            align = "center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
