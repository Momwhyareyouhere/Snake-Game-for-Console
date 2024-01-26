import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="black")
        self.canvas.pack()
        self.master.bind("<KeyPress>", self.key_pressed)

        self.snake = [[100, 100], [90, 100], [80, 100]]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        self.high_score = self.load_high_score()

        self.score_label = tk.Label(self.master, text=f"Score: {self.score}")
        self.score_label.pack()

        self.high_score_label = tk.Label(self.master, text=f"High Score: {self.high_score}")
        self.high_score_label.pack()

        self.move_snake()

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                content = file.read()
                if content.strip():
                    return int(content)
                else:
                    return 0
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def create_food(self):
        # Delete existing food items
        self.canvas.delete("food")

        x = random.randint(1, 19) * 20
        y = random.randint(1, 19) * 20
        self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="red", tags="food")
        return [x, y]

    def move_snake(self):
        head = self.snake[0][:]
        if self.direction == "Up":
            head[1] -= 20
        elif self.direction == "Down":
            head[1] += 20
        elif self.direction == "Left":
            head[0] -= 20
        elif self.direction == "Right":
            head[0] += 20

        self.snake.insert(0, head)
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="green", tags="snake")

        if head == self.food:
            self.food = self.create_food()
            self.score += 10
            self.update_score()
        else:
            self.snake.pop()

        if self.check_collision():
            self.game_over()
        else:
            self.master.after(100, self.move_snake)

    def key_pressed(self, event):
        key = event.keysym
        if (
            (key in {"Up", "W"} and not self.direction == "Down") or
            (key in {"Down", "S"} and not self.direction == "Up") or
            (key in {"Left", "A"} and not self.direction == "Right") or
            (key in {"Right", "D"} and not self.direction == "Left")
        ):
            self.direction = key

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_label.config(text=f"High Score: {self.high_score}")
            self.save_high_score()

    def check_collision(self):
        head = self.snake[0]
        return (
            head[0] < 0 or head[0] >= 400 or
            head[1] < 0 or head[1] >= 400 or
            head in self.snake[1:]
        )

    def game_over(self):
        self.canvas.create_text(
            200, 200, text="Game Over!", font=("Helvetica", 16), fill="white"
        )

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

