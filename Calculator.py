from nicegui import ui

ui.colors(primary='#1e222c')

ui.query('body').classes('bg-[#0f1117]')

def add_text(number):
    if display_number.text == "0":
        display_number.text = ""
    display_number.text = display_number.text + str(number)

def remove_text():
    if len(display_number.text) > 1:
        display_number.text = display_number.text[:-1]
    else:
        display_number.text = "0"


def all_clr():
    display_number.text = "0"

calc_memory = {
    "temp": 0,
    "operator": ""
}

def add_number():
    calc_memory["temp"] = float(display_number.text)
    calc_memory["operator"] = "+"
    display_number.text = "0"

def subtract_number():
    calc_memory["temp"] = float(display_number.text)
    calc_memory["operator"] = "-"
    display_number.text = "0"

def multiply_number():
    calc_memory["temp"] = float(display_number.text)
    calc_memory["operator"] = "*"
    display_number.text = "0"

def divide_number():
    calc_memory["temp"] = float(display_number.text)
    calc_memory["operator"] = "/"
    display_number.text = "0"

def equal_number():
    result = 0
    if calc_memory["operator"] == "+":
        result = calc_memory["temp"] + float(display_number.text)
    elif calc_memory["operator"] == "-":
        result = calc_memory["temp"] - float(display_number.text)
        calc_memory["temp"] = float(display_number.text)
    elif calc_memory["operator"] == "*":
        result = calc_memory["temp"] * float(display_number.text)
    elif calc_memory["operator"] == "/":
        result = calc_memory["temp"] / float(display_number.text)
    else:
        result = "0"
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    display_number.text = str(result)




with ui.column().classes("w-full items-center justify-center"):
    ui.row.default_classes("justify-center gap-4 translate-x-17")
    ui.button.default_classes("w-30 h-30 text-4xl font-bold ring-5 ring-blue-500/10")

    with ui.card().classes("bg-white/80 w-98 max-w-3xl mx-auto shadow-lg shadow-green-100/20 ring-4 ring-teal-500/20 whitespace-nowrap overflow-x-auto").style("scrollbar-width: none; -ms-overflow-style: none;"):
        display_number = ui.label("0").classes("w-full text-right text-4xl font-bold")
    with ui.row():
        ui.button("1", on_click=lambda: add_text(1))
        ui.button("2", on_click=lambda: add_text(2))
        ui.button("3", on_click=lambda: add_text(3))
        ui.button("+", on_click=lambda: add_number(), color="green").classes("ring-4 ring-green-500/20")
    with ui.row():
        ui.button("4", on_click=lambda: add_text(4))
        ui.button("5", on_click=lambda: add_text(5))
        ui.button("6", on_click=lambda: add_text(6))
        ui.button("-", on_click=lambda: subtract_number(), color="green").classes("ring-4 ring-green-500/20")
    with ui.row():
        ui.button("7", on_click=lambda: add_text(7))
        ui.button("8", on_click=lambda: add_text(8))
        ui.button("9", on_click=lambda: add_text(9))
        ui.button("×", on_click=lambda: multiply_number(), color="green").classes("ring-4 ring-green-500/20")
    with ui.row():
        ui.button("AC", on_click=lambda: all_clr(), color="red").classes("ring-4 ring-red-500/20")
        ui.button("0", on_click=lambda: add_text(0))
        ui.button(on_click=lambda: remove_text(), color="red", icon="backspace").classes("ring-4 ring-red-500/20")
        ui.button("÷", on_click=lambda: divide_number(), color="green").classes("ring-4 ring-green-500/20")
    ui.button("=", on_click=lambda: equal_number(), color="cyan-9").classes("w-98 ring-4 ring-blue-500/20")
ui.run(title="Calculator")