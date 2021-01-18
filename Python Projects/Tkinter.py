# TODO SIMPLE GAME GIU USING TKINTER
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as font
import pygame
import os

root = Tk()

pygame.mixer.init()
pygame.init()


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        Spectre = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Spectre.jpg")
        Medusa = Image.open(r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Medusa.jpg")

        Spectre_Skill1 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Spectre Skills\Spectral Dagger.png")
        Spectre_Skill2 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Spectre Skills\Desolate.png")
        Spectre_Skill3 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Spectre Skills\Dispersion.png")
        Spectre_Ulti = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Spectre Skills\Spectral Hunt.png")

        Medusa_Skill1 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Medusa Skills\Split Shot.png")
        Medusa_Skill2 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Medusa Skills\Mystic Snake.png")
        Medusa_Skill3 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Medusa Skills\Mana Shield.png")
        Medusa_Ulti = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Medusa Skills\Stone Gaze.png")

        attack1 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Attribute\Attack Icon.png")
        defense1 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Attribute\Defense Icon.png")
        strength1 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Attribute\Strength Icon.png")
        agility1 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Attribute\Agility Icon.png")
        intelligence1 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Attribute\Intelligence Icon.png")

        attack2 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Attribute\Attack Icon.png")
        defense2 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Attribute\Defense Icon.png")
        strength2 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Attribute\Strength Icon.png")
        agility2 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Attribute\Agility Icon.png")
        intelligence2 = Image.open(
            r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\Attribute\Intelligence Icon.png")

        Spectre.thumbnail((200, 250))
        Medusa.thumbnail((200, 250))

        Medusa_Skill1.thumbnail((200, 250))
        Medusa_Skill2.thumbnail((200, 250))
        Medusa_Skill3.thumbnail((200, 250))
        Medusa_Ulti.thumbnail((200, 250))

        Spectre_Skill1.thumbnail((200, 250))
        Spectre_Skill2.thumbnail((200, 250))
        Spectre_Skill3.thumbnail((200, 250))
        Spectre_Ulti.thumbnail((200, 250))

        attack1.thumbnail((200, 250))
        defense1.thumbnail((200, 250))
        agility1.thumbnail((200, 250))
        strength1.thumbnail((200, 250))
        intelligence1.thumbnail((200, 250))

        attack2.thumbnail((200, 250))
        defense2.thumbnail((200, 250))
        agility2.thumbnail((200, 250))
        strength2.thumbnail((200, 250))
        intelligence2.thumbnail((200, 250))

        render = ImageTk.PhotoImage(Spectre)
        render1 = ImageTk.PhotoImage(Medusa)
        render2 = ImageTk.PhotoImage(Medusa_Skill1)
        render3 = ImageTk.PhotoImage(Medusa_Skill2)
        render4 = ImageTk.PhotoImage(Medusa_Skill3)
        render5 = ImageTk.PhotoImage(Medusa_Ulti)

        render6 = ImageTk.PhotoImage(Spectre_Skill1)
        render7 = ImageTk.PhotoImage(Spectre_Skill2)
        render8 = ImageTk.PhotoImage(Spectre_Skill3)
        render9 = ImageTk.PhotoImage(Spectre_Ulti)

        render10 = ImageTk.PhotoImage(attack1)
        render11 = ImageTk.PhotoImage(defense1)
        render12 = ImageTk.PhotoImage(agility1)
        render13 = ImageTk.PhotoImage(strength1)
        render14 = ImageTk.PhotoImage(intelligence1)

        render15 = ImageTk.PhotoImage(attack2)
        render16 = ImageTk.PhotoImage(defense2)
        render17 = ImageTk.PhotoImage(agility2)
        render18 = ImageTk.PhotoImage(strength2)
        render19 = ImageTk.PhotoImage(intelligence2)


        img = Label(self, image=render)
        img1 = Label(self, image=render1)

        img2 = Label(self, image=render2)
        img3 = Label(self, image=render3)
        img4 = Label(self, image=render4)
        img5 = Label(self, image=render5)

        img6 = Label(self, image=render6)
        img7 = Label(self, image=render7)
        img8 = Label(self, image=render8)
        img9 = Label(self, image=render9)

        img10 = Label(self, image=render10)
        img11 = Label(self, image=render11)
        img12 = Label(self, image=render12)
        img13 = Label(self, image=render13)
        img14 = Label(self, image=render14)

        img15 = Label(self, image=render15)
        img16 = Label(self, image=render16)
        img17 = Label(self, image=render17)
        img18 = Label(self, image=render18)
        img19 = Label(self, image=render19)

        img.image = render
        img1.image = render1

        img2.image = render2  # Skill 1 (Medusa)
        img3.image = render3  # Skill 2 (Medusa)
        img4.image = render4  # Skill 3 (Medusa)
        img5.image = render5  # Ulti (Medusa)

        img6.image = render6  # Skill 1 (Spectre)
        img7.image = render7  # Skill 2 (Spectre)
        img8.image = render8  # Skill 3 (Spectre)
        img9.image = render9  # Ulti (Spectre)

        # Attributes (Spectre)
        img10.image = render10
        img11.image = render11
        img12.image = render12
        img13.image = render13
        img14.image = render14

        # Attributes (Medusa)
        img15.image = render15  # Attack
        img16.image = render16  # Defense
        img17.image = render17  # Agility
        img18.image = render18  # Strength
        img19.image = render19  # Intelligence

        img.place(x=0, y=50)
        img1.place(x=796, y=50)

        # Spectre Skills
        img6.place(x=1, y=341)
        img7.place(x=96, y=341)
        img8.place(x=191, y=341)
        img9.place(x=286, y=341)

        # Spectre Attributes
        img10.place(x=5, y=441)
        img11.place(x=3, y=485)
        img12.place(x=5, y=540)
        img13.place(x=5, y=589)
        img14.place(x=5, y=637)

        # Medusa Skills
        img2.place(x=904, y=341)
        img3.place(x=810, y=341)
        img4.place(x=716, y=341)
        img5.place(x=621, y=341)

        # Medusa Attributes
        img15.place(x=945, y=441)
        img16.place(x=945, y=485)
        img17.place(x=950, y=540)
        img18.place(x=950, y=589)
        img19.place(x=950, y=637)



class mylabels(object):

    def command1(self):
        if self.spectre_hp.get() == 5000:
            messagebox.showinfo("CAN'T PERFORM HEAL", "MAX HEALTH")
        elif self.spectre_mana.get() >= 65:
            self.spectre_hp.set(self.spectre_hp.get() + 25)
            self.spectre_mana.set(self.spectre_mana.get() - 65)

            pygame.mixer.Channel(3).play(pygame.mixer.Sound(
                r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\HEAL.mp3"),
                                         maxtime=2000,)
            pygame.mixer.music.set_volume(1)

        elif self.spectre_mana.get() <= 64:
            messagebox.showinfo("CAN'T PERFORM HEAL", "NOT ENOUGH MANA")

    def command2(self):
        if self.medusa_hp.get() >= 1:
            self.medusa_hp.set(self.medusa_hp.get() - 110)
            frame = LabelFrame(root, text="EFFECT:", padx=20, pady=20, font=('hooge 05_55', 15, 'bold'), fg="black",
                               relief=SOLID)
            frame.place(x=185, y=450)
            msg = Label(frame, text=f"Spectre dealt {self.damage.get()} health damage to Medusa!", bd=0.5,
                        relief=SOLID,
                        font=('hooge 05_55', 15, 'bold'), width=42, height=6, anchor=NW, fg="black")

            msg.pack()
            self.damage.set(self.damage.get() + 110)
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(
                r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\SPECTRE ATTACK SOUND.mpeg"),
                                         maxtime=2000,)
            pygame.mixer.music.set_volume(0.5)

        elif self.medusa_hp.get() == 0:
            messagebox.showwarning("CAN'T PERFORM ATTACK", "ENEMY DEFEATED")
            self.damage.set(self.damage.get() + 110)

            pygame.mixer.music.load(r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\VICTORY SOUND.mpeg")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(loops=-1)

    @staticmethod
    def Spectre():
        player1 = Label(root, text=f"PLAYER 1", fg="Blue")
        player1.config(width=0)
        player1.config(font=("hooge 05_53", 20))
        player1.place(x=30, y=5)

    @staticmethod
    def Medusa():
        player2 = Label(root, text=f"PLAYER 2", fg="Red")
        player2.config(width=0)
        player2.config(font=("hooge 05_53", 20))
        player2.place(x=821, y=5)

    @staticmethod
    def HEADER1():
        header = Label(root, text=f"TURN:", fg="#000000")
        header.config(width=0)
        header.config(font=("hooge 05_53", 20))
        header.place(x=450, y=5)

    @staticmethod
    def HEADER2():
        header1 = Label(root, text=f"PLAYER 1", fg="#000000")
        header1.config(width=0)
        header1.config(font=("hooge 05_53", 20))
        header1.place(x=429, y=45)

    @staticmethod
    def HEADER3():
        header3 = Label(root, text=f"HP", fg="#03ac13")
        header3.config(width=0)
        header3.config(font=("hooge 05_53", 25))
        header3.place(x=468, y=100)

    @staticmethod
    def HEADER4():
        header4 = Label(root, text=f"MANA", fg="#01579b")
        header4.config(width=0)
        header4.config(font=("hooge 05_53", 25))
        header4.place(x=441, y=150)

    @staticmethod
    def HEADER5():
        header5 = Label(root, text=f"SKILLS", fg="#ffd700")
        header5.config(width=0)
        header5.config(font=("hooge 05_53", 25))
        header5.place(x=435, y=365)

    def buttton1(self):
        ATTACK = Button(root, text="ATTACK", padx=50, pady=10, command=self.command2, fg="white",
                        bg="#c21807", cursor="pirate")
        myFont = font.Font(family="hooge 05_55")
        ATTACK['font'] = myFont
        ATTACK.place(x=340, y=280)

    def buttton2(self):
        HEAL = Button(root, text="HEAL", padx=50, pady=10, command=self.command1, fg="white", bg="#03ac13",
                      cursor="heart")
        myFont = font.Font(family="hooge 05_55")
        HEAL['font'] = myFont
        HEAL.place(x=500, y=280)

    def LP1(self):
        LP1 = Label(root, textvariable=self.spectre_hp, fg="#03ac13")
        LP1.config(width=0)
        LP1.config(font=("hooge 05_53", 25))
        LP1.place(x=210, y=100)

    def LP2(self):
        LP2 = Label(root, textvariable=self.medusa_hp, fg="#03ac13")
        LP2.config(width=0)
        LP2.config(font=("hooge 05_53", 25))
        LP2.place(x=686, y=100)

    def MP1(self):
        MP1 = Label(root, textvariable=self.spectre_mana, fg="#01579b")
        MP1.config(width=0)
        MP1.config(font=("hooge 05_53", 25))
        MP1.place(x=210, y=150)

    def MP2(self):
        MP2 = Label(root, textvariable=self.medusa_mana, fg="#01579b")
        MP2.config(width=0)
        MP2.config(font=("hooge 05_53", 25))
        MP2.place(x=686, y=150)

    @staticmethod
    def versus():
        versus = Label(root, text=f"VS", fg="#000000")
        versus.config(width=0)
        versus.config(font=("Digital-7 Mono", 50))
        versus.place(x=466, y=200)

    @staticmethod
    def NAME1():
        NAME1 = Label(root, text=f"Spectre", fg="#000000")
        NAME1.config(width=0)
        NAME1.config(font=("hooge 05_55", 30))
        NAME1.place(x=12, y=283)

    @staticmethod
    def NAME2():
        NAME2 = Label(root, text=f"MEDUSA", fg="#000000")
        NAME2.config(width=0)
        NAME2.config(font=("hooge 05_55", 30))
        NAME2.place(x=821, y=283)

    def message_box(self):
        frame = LabelFrame(root, text="EFFECT:", padx=20, pady=20, font=('hooge 05_55', 15, 'bold'), fg="black",
                           relief=SOLID)
        frame.place(x=185, y=450)
        msg = Label(frame, text=f"Spectre dealt {0} health damage to Medusa!", bd=0.5, relief=SOLID,
                    font=('hooge 05_55', 15, 'bold'), width=42, height=6, anchor=NW, fg="black")
        msg.pack()

    @staticmethod
    def Spec_Attributes():
        attack1 = Label(root, text="110", fg="#000000")
        attack1.config(width=0)
        attack1.config(font=("hooge 05_55", 15))
        attack1.place(x=65, y=441)

        defense1 = Label(root, text="3.22", fg="#000000")
        defense1.config(width=0)
        defense1.config(font=("hooge 05_55", 15))
        defense1.place(x=65, y=485)

        agility1 = Label(root, text="23 + 3.10", fg="#000000")
        agility1.config(width=0)
        agility1.config(font=("hooge 05_55", 15))
        agility1.place(x=65, y=540)

        strength1 = Label(root, text="23 + 2.50", fg="#000000")
        strength1.config(width=0)
        strength1.config(font=("hooge 05_55", 15))
        strength1.place(x=65, y=598)

        intelligence1 = Label(root, text="16 + 1.90", fg="#000000")
        intelligence1.config(width=0)
        intelligence1.config(font=("hooge 05_55", 15))
        intelligence1.place(x=65, y=637)

    @staticmethod
    def Medusa_Attributes():
        attack2 = Label(root, text="107", fg="#000000")
        attack2.config(width=0)
        attack2.config(font=("hooge 05_55", 15))
        attack2.place(x=898, y=449)

        defense2 = Label(root, text="3.01", fg="#000000")
        defense2.config(width=0)
        defense2.config(font=("hooge 05_55", 15))
        defense2.place(x=890, y=485)

        agility2 = Label(root, text="24 + 3.05", fg="#000000")
        agility2.config(width=0)
        agility2.config(font=("hooge 05_55", 15))
        agility2.place(x=839, y=540)

        strength2 = Label(root, text="23 + 2.50", fg="#000000")
        strength2.config(width=0)
        strength2.config(font=("hooge 05_55", 15))
        strength2.place(x=839, y=598)

        intelligence2 = Label(root, text="11 + 1.90", fg="#000000")
        intelligence2.config(width=0)
        intelligence2.config(font=("hooge 05_55", 15))
        intelligence2.place(x=854, y=637)

    def sound_effects(self):
        if self.medusa_hp.get() >= 1:
            pygame.mixer.music.load(os.path.join(os.getcwd(), 'sound',
                                             r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\BACKGROUND MUSIC.mp3"))
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(loops=False)


    spectre_hp = IntVar()
    medusa_hp = IntVar()
    damage = IntVar()
    spectre_mana = IntVar()
    medusa_mana = IntVar()

    damage.set(110)

    spectre_hp.set(4190)
    medusa_hp.set(1100)

    spectre_mana.set(1000)
    medusa_mana.set(1000)


if __name__ == "__main__":
    app = Window(root)
    GAME = mylabels()
    GAME.Spectre()
    GAME.Medusa()
    GAME.HEADER1()
    GAME.HEADER2()
    GAME.HEADER3()
    GAME.HEADER4()
    GAME.HEADER5()
    GAME.LP1()
    GAME.LP2()
    GAME.MP1()
    GAME.MP2()
    GAME.versus()
    GAME.NAME1()
    GAME.NAME2()
    GAME.buttton1()
    GAME.buttton2()
    GAME.message_box()
    GAME.Spec_Attributes()
    GAME.Medusa_Attributes()
    GAME.sound_effects()
    root.wm_title("Defense of the Ancients 2")
    logo = PhotoImage(file=r"C:\Users\User\PycharmProjects\My_Repository\Python Projects\Tkinter GUI Tools\DOTA2 LOGO.png")
    root.iconphoto(False, logo)
    root.geometry("1000x682")
    mainloop()