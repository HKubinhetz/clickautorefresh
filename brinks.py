import pywinauto

app = pywinauto.Application(backend="win32")
try:
    app.connect(title_re=".*Geogás Distri*.", visible_only=False)
except:
    print("Not visible...")
    exit()
top_window = app.window(title_re=".*Geogás Distri*.", visible_only=False)
top_window.restore().set_focus()
