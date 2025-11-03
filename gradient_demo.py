import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(width=600, height=600)
dpg.setup_dearpygui()

with dpg.theme() as no_paddding_theme:
    with dpg.theme_component(dpg.mvWindowAppItem):
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, 0)

with dpg.window(label="tutorial", width=500, height=500) as wnd:
    dpg.bind_item_theme(dpg.last_item(), no_paddding_theme)

    dpg.draw_rectangle(
        (0, 0), (500, 500),
        label = "background-gradient",
        color_bottom_right=(24, 8, 75),#verified
        color_bottom_left=(56, 24, 75),
        color_upper_right=(68, 30, 80),
        color_upper_left=(69, 42, 64),#verified
        multicolor=True,
        fill=True
    )
    with dpg.child_window(pos=(8, 28), width=100, height=100):
        dpg.add_button(label="Button to click", callback=lambda: print("dolor sit"))

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
