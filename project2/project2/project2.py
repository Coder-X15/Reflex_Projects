"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

# my calculator application

class CalculatorState(rx.State):
    """The state of the calculator string."""
    expression : str = ""

    @rx.event
    def add_to_expression(self, value: str):
        """Add a value to the expression."""
        self.expression += value
    
    @rx.event
    def clear_expression(self):
        """Clear the expression."""
        self.expression = ""

    @rx.event
    def evaluate_expression(self):
        """Evaluate the expression and update the state."""
        try:
            self.expression = str(eval(self.expression))
        except:
            self.expression = "Error"

    @rx.event
    def delete_last(self):
        """Delete the last character from the expression."""
        self.expression = self.expression[:-1]

# Define the calculator buttons
keypad = rx.vstack(
    rx.hstack(
        rx.button("7", on_click= lambda : CalculatorState.add_to_expression("7"), width = "60px", height="60px", text_align="center"),
        rx.button("8", on_click= lambda : CalculatorState.add_to_expression("8"), width = "60px", height="60px", text_align="center"),
        rx.button("9", on_click= lambda : CalculatorState.add_to_expression("9"), width = "60px", height="60px", text_align="center"),
        rx.button("/", on_click= lambda : CalculatorState.add_to_expression("/"), width = "60px", height="60px", text_align="center"),
    ),
    rx.hstack(
        rx.button("4", on_click= lambda : CalculatorState.add_to_expression("4"), width = "60px", height="60px", text_align="center"),
        rx.button("5", on_click= lambda : CalculatorState.add_to_expression("5"), width = "60px", height="60px", text_align="center"),
        rx.button("6", on_click= lambda : CalculatorState.add_to_expression("6"), width = "60px", height="60px", text_align="center"),
        rx.button("*", on_click= lambda : CalculatorState.add_to_expression("*"), width = "60px", height="60px", text_align="center"),
    ), 
    rx.hstack(
        rx.button("1", on_click= lambda : CalculatorState.add_to_expression("1"), width = "60px", height="60px", text_align="center"),
        rx.button("2", on_click= lambda : CalculatorState.add_to_expression("2"), width = "60px", height="60px", text_align="center"),
        rx.button("3", on_click= lambda : CalculatorState.add_to_expression("3"), width = "60px", height="60px", text_align="center"),
        rx.button("-", on_click= lambda : CalculatorState.add_to_expression("-"), width = "60px", height="60px", text_align="center"),
    ),
    rx.hstack(
        rx.button("0", on_click= lambda : CalculatorState.add_to_expression("0"), width = "60px", height="60px", text_align="center"),
        rx.button(".", on_click= lambda : CalculatorState.add_to_expression("."), width = "60px", height="60px", text_align="center"),
        rx.button("=", on_click= CalculatorState.evaluate_expression, width = "60px", height="60px", text_align="center"),
        rx.button("+", on_click= lambda : CalculatorState.add_to_expression("+"), width = "60px", height="60px", text_align="center"),
    ),
    rx.hstack(
        rx.button("C", on_click= CalculatorState.clear_expression, width = "60px", height="60px", text_align="center"),
        rx.button("DEL", on_click= CalculatorState.delete_last, width = "60px", height="60px", text_align="center"),
    )
)

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Calculator", font_size="36px"),
            rx.text("Welcome to the calculator app!", font_size="24px"),
            rx.heading(CalculatorState.expression, font_size="32px", margin_bottom="20px"),
            keypad
        ),
    )


app = rx.App()
app.add_page(index)
