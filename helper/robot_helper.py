import tkinter as tk

# change here
def initialize_canvas(window):
    window.resizable(False,False)
    canvas = tk.Canvas(window,width=1000,height=1000)
    canvas.pack()
    return canvas

def bot_clicked(x, y, registryActives, Bot):
    '''
    Bot is a class
    :param x:
    :param y:
    :param registryActives:
    :param Bot:
    :return:
    rpb purposely use the pass statement here. to be use in tutorial 8. see the pre-requisite section about the full code
    '''
    pass
