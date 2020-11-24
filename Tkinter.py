# TODO SIMPLE GAME GIU USING TKINTER
# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import tkinter.font as font
#
# root = Tk()
#
#
# class Window(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master
#         self.pack(fill=BOTH, expand=1)
#
#         load = Image.open("Chou.jpg")
#         load1 = Image.open("Valir.jpg")
#         load.thumbnail((200, 250))
#         load1.thumbnail((200, 250))
#         render = ImageTk.PhotoImage(load)
#         render1 = ImageTk.PhotoImage(load1)
#         img = Label(self, image=render)
#         img1 = Label(self, image=render1)
#         img.image = render
#         img1.image = render1
#
#         img.place(x=0, y=50)
#         img1.place(x=500, y=50)
#
# class mylabels(object):
#
#
#     def command1(self):
#         if self.chou_hp.get() == 100:
#             messagebox.showinfo("CAN'T PERFORM HEAL", "FULL HEALTH")
#         else:
#             messagebox.showinfo("HEAL!", "YOU HEALED YOURSELF")
#             self.chou_hp.set(self.chou_hp.get() + 1)
#
#
#     def command2(self):
#         if self.valir_hp.get() >= 1:
#             messagebox.showwarning("ATTACK!", "YOU ATTACKED PLAYER 2")
#             self.valir_hp.set(self.valir_hp.get()-1)
#             frame = LabelFrame(root, text="EFFECT:", padx=20, pady=20, font=('hooge 05_55', 15, 'bold'))
#             frame.place(x=35, y=380)
#             msg = Label(frame, text=f"Chou dealt {self.damage.get()+1} health damage to Valir!", bd=10, relief=SOLID,
#                         font=('hooge 05_55', 15, 'bold'), width=42, height=5, anchor=NW, fg="black")
#
#             msg.pack()
#             self.damage.set(self.damage.get()+1)
#         elif self.valir_hp.get() == 0:
#             messagebox.showwarning("CAN'T PERFORM ATTACK", "ENEMY DEFEATED")
#
#
#     @staticmethod
#     def Chou():
#         player1 = Label(root, text=f"PLAYER 1", fg="Blue")
#         player1.config(width=0)
#         player1.config(font=("hooge 05_53", 20))
#         player1.place(x=30, y=5)
#
#     @staticmethod
#     def Valir():
#         player2 = Label(root, text=f"PLAYER 2", fg="Red")
#         player2.config(width=0)
#         player2.config(font=("hooge 05_53", 20))
#         player2.place(x=530, y=5)
#
#     @staticmethod
#     def HEADER1():
#         header = Label(root, text=f"TURN:", fg="#000000")
#         header.config(width=0)
#         header.config(font=("hooge 05_53", 15))
#         header.place(x=310, y=10)
#
#     @staticmethod
#     def HEADER2():
#         header1 = Label(root, text=f"PLAYER 1", fg="#fff200")
#         header1.config(width=0)
#         header1.config(font=("hooge 05_53", 15))
#         header1.place(x=293, y=50)
#
#     @staticmethod
#     def HEADER3():
#         header3 = Label(root, text=f"HP", fg="#000000")
#         header3.config(width=0)
#         header3.config(font=("hooge 05_53", 25))
#         header3.place(x=319, y=100)
#
#     def buttton1(self):
#         ATTACK = Button(root, text="ATTACK", padx=50, pady=10, command=self.command2, fg="white",
#                         bg="#c21807", cursor="pirate")
#         myFont = font.Font(family="hooge 05_55")
#         ATTACK['font'] = myFont
#         ATTACK.place(x=200, y=280)
#
#     def buttton2(self):
#         HEAL = Button(root, text="HEAL", padx=50, pady=10, command=self.command1, fg="white", bg="#03ac13",
#         cursor="heart")
#         myFont = font.Font(family="hooge 05_55")
#         HEAL['font'] = myFont
#         HEAL.place(x=355, y=280)
#
#     def LP1(self):
#         LP1 = Label(root, textvariable=self.chou_hp, fg="#03ac13")
#         LP1.config(width=0)
#         LP1.config(font=("hooge 05_53", 25))
#         LP1.place(x=210, y=100)
#
#     def LP2(self):
#         LP2 = Label(root, textvariable=self.valir_hp, fg="#03ac13")
#         LP2.config(width=0)
#         LP2.config(font=("hooge 05_53", 25))
#         LP2.place(x=440, y=100)
#
#     @staticmethod
#     def versus():
#         versus = Label(root, text=f"VS", fg="#000000")
#         versus.config(width=0)
#         versus.config(font=("Digital-7 Mono", 50))
#         versus.place(x=319, y=200)
#
#     @staticmethod
#     def versus():
#         versus = Label(root, text=f"VS", fg="#000000")
#         versus.config(width=0)
#         versus.config(font=("Digital-7 Mono", 50))
#         versus.place(x=319, y=200)
#
#     @staticmethod
#     def NAME1():
#         NAME1 = Label(root, text=f"Chou", fg="#000000")
#         NAME1.config(width=0)
#         NAME1.config(font=("hooge 05_55", 30))
#         NAME1.place(x=49, y=253)
#
#     @staticmethod
#     def NAME2():
#         NAME2 = Label(root, text=f"Valir", fg="#000000")
#         NAME2.config(width=0)
#         NAME2.config(font=("hooge 05_55", 30))
#         NAME2.place(x=538, y=253)
#
#     def message_box(self):
#         frame = LabelFrame(root, text="EFFECT:", padx=20, pady=20, font=('hooge 05_55', 15, 'bold'))
#         frame.place(x=35, y=380)
#         msg = Label(frame, text=f"Chou dealt {self.damage.get()+1} health damage to Valir!", bd=0.5, relief=SOLID,
#                     font=('hooge 05_55', 15, 'bold'), width=42, height=5, anchor=NW, fg="black")
#         msg.pack()
#
#     valir_hp = IntVar()
#     chou_hp = IntVar()
#     damage = IntVar()
#     damage.set(96)
#     chou_hp.set(97)
#     valir_hp.set(4)
#
#
# if __name__ == "__main__":
#     app = Window(root)
#     GAME = mylabels()
#     GAME.Chou()
#     GAME.Valir()
#     GAME.HEADER1()
#     GAME.HEADER2()
#     GAME.HEADER3()
#     GAME.LP1()
#     GAME.LP2()
#     GAME.versus()
#     GAME.NAME1()
#     GAME.NAME2()
#     GAME.buttton1()
#     GAME.buttton2()
#     GAME.message_box()
#     root.wm_title("Mobile Legends")
#     logo = PhotoImage(file="LOGO.png")
#     root.iconphoto(False, logo)
#     root.geometry("704x620")
#     root.config(bg="blue")
#     mainloop()

