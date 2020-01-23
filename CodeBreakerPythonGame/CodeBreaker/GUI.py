import tkinter as tk
import main
import random

HEIGHT = 750
WIDTH = 750
DIGITS_TO_WIN = 5
ALLOWED_ATTEMPTS = 20


# creates a random code
def init_code():
    for i in range(len(main.code)):
        main.code[i] = str(random.randint(0, 9))
    print(main.code)


# ends the game in a victory
def end_game_win():
    main.attempts_label['text'] = "YOU WIN!"
    # main.restart_button.place(relx=.50, rely=.45,
    #                           relheight=.1, relwidth=.30, anchor='n')
    print("you win.")


# ends game in a loss
def end_game_lose():
    main.attempts_label['text'] = "YOU LOSE!"
    # main.restart_button.place(relx=.50, rely=.45,
    #                           relheight=.1, relwidth=.30, anchor='n')
    print("you lose")


# sets the digit to correct
def set_green(button):
    main.number_of_green += 1
    button['bg'] = '#00ff99'
    button['state'] = 'disabled'
    main.current_button = 0


# checks the current guessed code against the real code
# this code uses the button's wraplength to index since it is the only indexable attribute that is not being used
def check_code(button):
    if main.attempts_ > ALLOWED_ATTEMPTS - 1:
        end_game_lose()

    if button['text'] == main.code[button['wraplength']]:
        set_green(button)

    if main.number_of_green == DIGITS_TO_WIN:
        end_game_win()


# adds to the amount of attempts
def add_attempt(number_of_attempts_label):
    main.attempts_ += 1
    number_of_attempts_label['text'] = str(main.attempts_)


def keypad_click(keypad_button):
    if main.current_button != 0 and main.current_button['text'] != keypad_button['text']:
        main.current_button['state'] = 'normal'
        add_attempt(main.number_of_attempts_label)
        main.current_button['text'] = keypad_button['text']
        check_code(main.current_button)


# defines what will happen when a code button is clicked
def code_click(button):
    main.current_button = button
    button['state'] = 'disabled'


def create_frame():
    init_code()
    root = tk.Tk()
    root.title("Code Breaker")
    root.iconbitmap('appIcon.ico')
    root.geometry("{}x{}".format(WIDTH, HEIGHT))

    # main canvas
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#00d2d2")
    canvas.place(relwidth=1, relheight=1)

    # Upper Frame simply holds the title
    upper_frame = tk.Frame(root, bd=5, bg="#44204a")
    upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    # Title label adds the title
    txt_title = "Code Breaker"
    label = tk.Label(upper_frame, text=txt_title, bg="#a6e3b3", fg="#811006", font="courier 20")
    label.place(relwidth=1, relheight=1)

    # The lower frame where all of the input is taken in
    lower_frame = tk.Frame(root, bg='#44204a', bd=10)
    lower_frame.place(relx=.5, rely=.25, relwidth=.75, relheight=.6, anchor='n')

    inner_lower_frame = tk.Frame(lower_frame, bg="#1a617c")
    inner_lower_frame.place(relwidth=1, relheight=1)

    # restart Button

    restart_button = tk.Button(inner_lower_frame,
                               wraplength=0,
                               activebackground="#6e5272", activeforeground="#040005",
                               bg="#d2391e", fg="#ffcc00", text="Restart",
                               font="courier 25", relief='ridge',
                               command=lambda: print("totally restarted")
                               )

    # Buttons to show current code -------------------------------------------- code buttons start Here ----------------
    first_digit_button = tk.Button(inner_lower_frame,
                                   wraplength=0,
                                   activebackground="#6e5272", activeforeground="#040005",
                                   bg="#44204a", fg="#c0b4c2", text="0",
                                   font="courier 25", relief='ridge',
                                   command=lambda: code_click(first_digit_button)
                                   )
    first_digit_button.place(relx=.18, rely=.1,
                             relheight=.1, relwidth=.15, anchor='n')

    second_digit_button = tk.Button(inner_lower_frame,
                                    wraplength=1,
                                    activebackground="#6e5272", activeforeground="#040005",
                                    bg="#44204a", fg="#c0b4c2", text="0",
                                    font="courier 25", relief='ridge',
                                    command=lambda: code_click(second_digit_button)
                                    )
    second_digit_button.place(relx=.34, rely=.1,
                              relheight=.1, relwidth=.15, anchor='n')

    third_digit_button = tk.Button(inner_lower_frame,
                                   wraplength=2,
                                   activebackground="#6e5272", activeforeground="#040005",
                                   bg="#44204a", fg="#c0b4c2", text="0",
                                   font="courier 25", relief='ridge',
                                   command=lambda: code_click(third_digit_button)
                                   )
    third_digit_button.place(relx=.50, rely=.1,
                             relheight=.1, relwidth=.15, anchor='n')

    fourth_digit_button = tk.Button(inner_lower_frame,
                                    wraplength=3,
                                    activebackground="#6e5272", activeforeground="#040005",
                                    bg="#44204a", fg="#c0b4c2", text="0",
                                    font="courier 25", relief='ridge',
                                    command=lambda: code_click(fourth_digit_button)
                                    )
    fourth_digit_button.place(relx=.66, rely=.1,
                              relheight=.1, relwidth=.15, anchor='n')

    fith_digit_button = tk.Button(inner_lower_frame,
                                  wraplength=4,
                                  activebackground="#6e5272", activeforeground="#040005",
                                  bg="#44204a", fg="#c0b4c2", text="0",
                                  font="courier 25", relief='ridge',
                                  command=lambda: code_click(fith_digit_button)
                                  )
    fith_digit_button.place(relx=.82, rely=.1,
                            relheight=.1, relwidth=.15, anchor='n')
    # Buttons to show current code -------------------------------------------- code buttons end Here ------------------

    # Label to print attempts
    label_string = "Attempts"
    attempts_label = tk.Label(inner_lower_frame, text=label_string, bg="#1a617c", fg="#809fff",
                              font="courier 20")
    main.attempts_label = attempts_label
    attempts_label.place(relx=.5, rely=.25, relwidth=0.25, relheight=.075, anchor='n')

    number_of_attempts_label = tk.Label(inner_lower_frame, text='0', bg="#1a617c", fg="#809fff",
                                        font="courier 20")
    main.number_of_attempts_label = number_of_attempts_label
    number_of_attempts_label.place(relx=.5, rely=.35, relwidth=0.25, relheight=.075, anchor='n')

    # Buttons for keypad ------------------------------------------------------ keypad buttons start here---------------

    keypad_button_zero = tk.Button(inner_lower_frame,
                                   activebackground="#b3d9ff", activeforeground="#040005",
                                   bg="#4da6ff", fg="#0059b3", text="0",
                                   font="courier 20", relief='ridge',
                                   command=lambda: keypad_click(keypad_button_zero),
                                   )
    keypad_button_zero.place(relx=.50, rely=.87,
                             relheight=.075, relwidth=.1, anchor='n')

    keypad_button_one = tk.Button(inner_lower_frame,
                                  activebackground="#b3d9ff", activeforeground="#040005",
                                  bg="#4da6ff", fg="#0059b3", text="1",
                                  font="courier 20", relief='ridge',
                                  command=lambda: keypad_click(keypad_button_one)
                                  )
    keypad_button_one.place(relx=.395, rely=.785,
                            relheight=.075, relwidth=.1, anchor='n')

    keypad_button_two = tk.Button(inner_lower_frame,
                                  activebackground="#b3d9ff", activeforeground="#040005",
                                  bg="#4da6ff", fg="#0059b3", text="2",
                                  font="courier 20", relief='ridge',
                                  command=lambda: keypad_click(keypad_button_two)
                                  )
    keypad_button_two.place(relx=.50, rely=.785,
                            relheight=.075, relwidth=.1, anchor='n')

    keypad_button_three = tk.Button(inner_lower_frame,
                                    activebackground="#b3d9ff", activeforeground="#040005",
                                    bg="#4da6ff", fg="#0059b3", text="3",
                                    font="courier 20", relief='ridge',
                                    command=lambda: keypad_click(keypad_button_three)
                                    )
    keypad_button_three.place(relx=.605, rely=.785,
                              relheight=.075, relwidth=.1, anchor='n')

    keypad_button_four = tk.Button(inner_lower_frame,
                                   activebackground="#b3d9ff", activeforeground="#040005",
                                   bg="#4da6ff", fg="#0059b3", text="4",
                                   font="courier 20", relief='ridge',
                                   command=lambda: keypad_click(keypad_button_four)
                                   )
    keypad_button_four.place(relx=.395, rely=.7,
                             relheight=.075, relwidth=.1, anchor='n')

    keypad_button_five = tk.Button(inner_lower_frame,
                                   activebackground="#b3d9ff", activeforeground="#040005",
                                   bg="#4da6ff", fg="#0059b3", text="5",
                                   font="courier 20", relief='ridge',
                                   command=lambda: keypad_click(keypad_button_five)
                                   )
    keypad_button_five.place(relx=.50, rely=.7,
                             relheight=.075, relwidth=.1, anchor='n')

    keypad_button_six = tk.Button(inner_lower_frame,
                                  activebackground="#b3d9ff", activeforeground="#040005",
                                  bg="#4da6ff", fg="#0059b3", text="6",
                                  font="courier 20", relief='ridge',
                                  command=lambda: keypad_click(keypad_button_six)
                                  )
    keypad_button_six.place(relx=.605, rely=.7,
                            relheight=.075, relwidth=.1, anchor='n')

    keypad_button_seven = tk.Button(inner_lower_frame,
                                    activebackground="#b3d9ff", activeforeground="#040005",
                                    bg="#4da6ff", fg="#0059b3", text="7",
                                    font="courier 20", relief='ridge',
                                    command=lambda: keypad_click(keypad_button_seven)
                                    )
    keypad_button_seven.place(relx=.395, rely=.615,
                              relheight=.075, relwidth=.1, anchor='n')

    keypad_button_eight = tk.Button(inner_lower_frame,
                                    activebackground="#b3d9ff", activeforeground="#040005",
                                    bg="#4da6ff", fg="#0059b3", text="8",
                                    font="courier 20", relief='ridge',
                                    command=lambda: keypad_click(keypad_button_eight)
                                    )
    keypad_button_eight.place(relx=.50, rely=.615,
                              relheight=.075, relwidth=.1, anchor='n')

    keypad_button_nine = tk.Button(inner_lower_frame,
                                   activebackground="#b3d9ff", activeforeground="#040005",
                                   bg="#4da6ff", fg="#0059b3", text="9",
                                   font="courier 20", relief='ridge',
                                   command=lambda: keypad_click(keypad_button_nine)
                                   )
    keypad_button_nine.place(relx=.605, rely=.615,
                             relheight=.075, relwidth=.1, anchor='n')

    # Buttons for keypad ------------------------------------------------------ keypad buttons end here-----------------

    root.mainloop()


create_frame()
