import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="#2E2E2E")  # Dark background

        self.current_player = "X"  # Starting player
        self.buttons = [[None for _ in range(3)] for _ in range(3)]  # Grid of buttons

        self.create_widgets()

    def create_widgets(self):
        button_style = {
            "font": ('Arial', 24, 'bold'),
            "width": 5,
            "height": 2,
            "bg": "#FFFFFF",  # White background
            "fg": "#000000",  # Black text
            "activebackground": "#CCCCCC",  # Light gray when clicked
            "bd": 2,
            "relief": "raised"
        }

        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", command=lambda r=row, c=col: self.on_button_click(r, c),
                                   **button_style)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                self.buttons[row][col] = button

        reset_button_style = {
            "font": ('Arial', 14, 'bold'),
            "bg": "#007BFF",  # Blue background
            "fg": "#FFFFFF",  # White text
            "activebackground": "#0056b3",  # Darker blue when clicked
            "bd": 2,
            "relief": "raised"
        }

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game, **reset_button_style)
        self.reset_button.grid(row=3, column=0, columnspan=3, pady=10, sticky="nsew")

        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

    def on_button_click(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == "":
            button["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True

        # Check diagonals
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True

        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
