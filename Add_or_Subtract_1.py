from nicegui import ui

display_number = ui.label("0")

def increment_number():
    current = int(display_number.text)
    new_value = current + 1
    display_number.text = str(new_value)

def decrement_number():
    current = int(display_number.text)
    new_value = current - 1
    display_number.text = str(new_value)

with ui.row():
    ui.button("Remove 1", on_click=decrement_number, color="red")
    ui.button("Add 1", on_click=increment_number)


ui.run()