import tkinter as tk
import random


def main():

    root = tk.Tk()
    root.title('Number Guesser')
    root.geometry('330x240')
    root.configure(bg='#76849D')
    answer = random.randint(0, 100)
    text_value = ''

    def main_menu():
        lbl_1.pack(pady=25)
        btn_start.pack()
        btn_how.pack()
        btn_quit.pack()

    def end_screen():
        btn_guess.destroy()
        text_field.destroy()
        #lbl_2.config(text=f'Congratulations! \n You made it. The number was {answer}.')
        lbl_2.config(text='Never gonna give you up\n Never gonna let you down\n Never gonna run around and desert you\n Never gonna make you cry\n Never gonna say goodbye\n Never gonna tell a lie and hurt you')
        lbl_2.pack(expand=True)

    def how_play():
        lbl_1.forget()
        btn_quit.forget()
        btn_how.forget()
        lbl_how.pack(pady=20)
        btn_start.pack(side='bottom', expand=True)

    def start():
        lbl_1.forget()
        btn_start.forget()
        btn_quit.forget()
        btn_how.forget()
        lbl_how.forget()
        text_field.place(x=20, y=20)
        lbl_2.place(x=20, y=115)
        btn_guess.place(x=185, y=20)

    def game():
        global text_value
        try:
            text_value = int(text_field.get(1.0, 'end'))
        except ValueError:
            lbl_2.config(text='Invalid input')
            text_value = 1
        else:
            if text_value > answer:
                lbl_2.config(text='The number \n is lower')
            else:
                lbl_2.config(text='The number \n is higher')
            if text_value == answer:
                end_screen()
        text_field.delete(1.0, 'end')

    lbl_1 = tk.Label(root, height=2, text='Welcome to my game.', font=('Times New Roman', 15), bg='#76849D')
    lbl_2 = tk.Label(root, text='', font=('Times New Roman', 15), bg='#76849D')
    lbl_how = tk.Label(root, text='You have to guess a number between \n0 and 100. Each time it will tell \nyou if the'
                                  ' number is higher or lower.', font=('Times New Roman', 15), bg='#76849D')
    btn_start = tk.Button(root, text='Start', command=start, width=10, font=('Times New Roman', 15))
    btn_quit = tk.Button(root, text='Quit', command=root.quit, width=10, font=('Times New Roman', 15))
    btn_how = tk.Button(root, text='How to play', command=how_play, width=10, font=('Times New Roman', 15))
    btn_guess = tk.Button(root, text='Guess', command=game, width=10, height=8, font=('Times New Roman', 15))
    text_field = tk.Text(root, height=4, width=16, font=('Times New Roman', 13))

    main_menu()
    root.mainloop()


if __name__ == '__main__':
    main()
