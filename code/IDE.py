from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import subprocess
compiler = Tk()
compiler.title('Khush\'s Python')
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def run_without():
    code = editor.get('1.0' , END)
    exec(code)
    save_prompt = Toplevel()
    text = Label(save_prompt , text = 'Please Check The Python Console')
    text.pack()





def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt , text = 'Please Save Your Code')
        text.pack()
        return

    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output , error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0' , error)

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files' , '*.py')])
    else:
        path = file_path
    with open(path , 'w') as file:
        code = editor.get('1.0' , END)
        file.write(code)
        set_file_path(path)

def open_file():
    path = askopenfilename(filetypes=[('Python Files' , '*.py')])
    with open(path , 'r') as file:
        code = file.read()
        editor.delete('1.0' , END)
        editor.insert('1.0' , code)
        set_file_path(path)




menu_bar = Menu(compiler)

file_bar = Menu(menu_bar,tearoff=0)
file_bar.add_command(label='Open' , command=open_file)
file_bar.add_command(label='Save' , command=save_as)
file_bar.add_command(label='Save As' , command=save_as)
menu_bar.add_cascade(label='File', menu=file_bar)

run_bar = Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run' , command=run)
run_bar.add_command(label='Run Without Saving' , command=run_without)
menu_bar.add_cascade(label='Run', menu=run_bar)

exit_bar = Menu(menu_bar , tearoff = 0)
exit_bar.add_command(label='Exit' , command = exit)
menu_bar.add_cascade(label='Exit' , menu=exit_bar)




compiler.config(menu=menu_bar)


editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()
