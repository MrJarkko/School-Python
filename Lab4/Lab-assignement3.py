import tkinter
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog

'''This is lab4 school assignment for testing Python GUI. The program is a small version of Notepad application called Notepad--'''

############### Functions #############

# Call back function to show file content
def openfile():
    filename = filedialog.askopenfilename(title = 'Select File', filetypes = (('Text Files','*.txt'),('All files','*.*')) ) # Open file selection window
    fileHandle = open(filename)                                         # Open the file selected previously
    filecontent = fileHandle.read()                                     # Read the file content into memory
    fileHandle.close()                                                  # Close the file, we already have the content
    textboxfield.delete(1.0, tkinter.END)                               # Clear the scrolledText textbox
    textboxfield.insert(tkinter.INSERT, filecontent)                    # Insert the file content from memory into scrolledText textbox

# Call back function to save textbox content to new file
def savefile():
    filename = filedialog.asksaveasfilename(title = 'Enter Filename', filetypes = (('Text Files','*.txt'),('All files','*.*')) )    # Open file selection window
    filehandle = open(filename, 'w')                                    # Open the file selected (it can be existing file)
    filehandle.write(textboxfield.get(1.0, tkinter.END))                # Write the content of scrolledText textbox into file opened
    messagebox.showinfo('Info', 'File Saved')                           # Notify File save operation
    filehandle.close()                                                  # Close the file

#Call back function for Exit menu
def _quit():
    mainwindow.quit()                                                   # Quit the root window process
    mainwindow.destroy()                                                # Cleanup the root window
    exit()                                                              # Exit out the from the application

#Call back function for Help menu
def _help():
    messagebox.showinfo("About Notepad--", "Author : Jarkko Ainsoo\nProduct name: Notepad--\nProduct Version:\n1.0.0") # Show messagebox with info

################ GUI building ###############
mainwindow = tkinter.Tk()                                           # Main window
mainwindow.title('Notepad--')                                       # Main window title
mainframe = tkinter.LabelFrame(mainwindow)                          # Main frame in main window
mainframe.grid(column=0, row=0, padx = 10, pady = 10)               # Set the size of main frame in main window

# Adding scrolled textbox widget
scrolW = 80                                                         # Set scrolledtext textbox Width
scrolH = 30                                                         # Set scrolledtext textbox Height
textboxfield = tkinter.StringVar()                                  # Define a String variable
textboxfield = scrolledtext.ScrolledText(mainframe, width = scrolW, height = scrolH, wrap = tkinter.WORD)   # Set the scrolledText textbox options
textboxfield.pack()                                                 # Add the scrolledText into frame

# Creating Menu Bar
menuBar = tkinter.Menu(mainwindow)
mainwindow.config(menu = menuBar)
fileMenu = tkinter.Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'Open', command = openfile)
fileMenu.add_command(label = 'Save', command = savefile)
menuBar.add_cascade(label = 'File', menu = fileMenu)
fileMenu.add_separator()
fileMenu.add_command(label = 'Close', command = _quit)

helpMenu = tkinter.Menu(menuBar, tearoff = 0)
helpMenu.add_command(label ='About', command = _help)
menuBar.add_cascade(label = 'Help', menu = helpMenu)

# Starting main window (root window)
mainwindow.mainloop()
