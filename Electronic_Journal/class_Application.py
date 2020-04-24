import tkinter
import tkinter.ttk
 


VERSION = "0.0.1"

class Application(tkinter.ttk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.master.title(f"Электронный журнал ver. {VERSION}")
        #Узнаем размер экрана, создаем окно по фактическому 
        # разрешению монитора
        W = str(self.winfo_screenwidth()//2)
        H = str(self.winfo_screenheight()//2)
        self.master.geometry(f"={W}x{H}")
        
        
    def create_widgets(self):
        self.create_menu()
    
        #Buttons

        btn_add_comment = tkinter.ttk.Button(self, text = "Добавить\nзамечание", command = self.add_comment)
        btn_add_comment.grid(row = 0, column = 0)
        btn_del_comment = tkinter.ttk.Button(self, text = "Delete", command = self.del_comment)
        btn_del_comment.grid(row = 0, column = 1)
    
    def create_menu(self):
        window = self.master
        mainmenu= tkinter.Menu(window)
        window["menu"] = mainmenu
        self.menu = tkinter.Menu(mainmenu, tearoff = False)
        self.menu.add_command(label = "Open")
        self.menu.add_command(label = "Close", command = self.master.destroy)
        self.menu.add_command(label = "Print") 
        self.menu.add_command(label = "Send") #Отправить имеется ввиду на почту
        mainmenu.add_cascade(label = "File", menu = self.menu)

        self.comment_management = tkinter.Menu(mainmenu, tearoff = False)
        self.comment_management.add_command(label = "Comment management") #Добавить замечание
        self.comment_management.add_command(label = "Sign") #подписать
        self.comment_management.add_command(label = "Edit") #редактировать
        self.comment_management.add_command(label = "Revoke") #Анулировать
        mainmenu.add_cascade(label = "Comment management", menu = self.comment_management)

        self.bind()



    def add_comment(self):
        pass
    def del_comment(self):
        self.master.destroy()




root = tkinter.Tk()
app = Application(master = root)

root.mainloop()