import random

class WordSearch:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.words = []  # Store words and their positions
        self.found_words = []  # Track found words
        self.score = 0  # Track score
    
    def place_word(self, word):
        word_length = len(word)
        placed = False
        
        while not placed:
            direction = random.randint(0, 2)
            if direction == 0:  # Horizontal
                row = random.randint(0, self.height - 1)
                col = random.randint(0, self.width - word_length)
                if all(self.grid[row][col + i] in (' ', word[i]) for i in range(word_length)):
                    for i in range(word_length):
                        self.grid[row][col + i] = word[i]
                    self.words.append((word, "horizontal", row, col))
                    placed = True
            
            elif direction == 1:  # Vertical
                row = random.randint(0, self.height - word_length)
                col = random.randint(0, self.width - 1)
                if all(self.grid[row + i][col] in (' ', word[i]) for i in range(word_length)):
                    for i in range(word_length):
                        self.grid[row + i][col] = word[i]
                    self.words.append((word, "vertical", row, col))
                    placed = True
            
            elif direction == 2:  # Diagonal
                row = random.randint(0, self.height - word_length)
                col = random.randint(0, self.width - word_length)
                if all(self.grid[row + i][col + i] in (' ', word[i]) for i in range(word_length)):
                    for i in range(word_length):
                        self.grid[row + i][col + i] = word[i]
                    self.words.append((word, "diagonal", row, col))
                    placed = True

    def fill_grid(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == ' ':
                    self.grid[row][col] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    def print_grid(self):
        for row in self.grid:
            print(' '.join(row))
    
    def find_word(self, word):
        if word in self.found_words:
            print(f"Word '{word}' already found!")
            return
        
        for w, direction, row, col in self.words:
            if w == word:
                self.mark_word_found(word, direction, row, col)
                self.found_words.append(word)
                self.score += 10  # Increase score for each found word
                print(f"Congratulations! You found the word '{word}'. Your updated score: {self.score}")
                return
        
        print(f"Sorry, the word '{word}' is not in the grid.")
    
    def mark_word_found(self, word, direction, row, col):
        word_length = len(word)
        if direction == "horizontal":
            for i in range(word_length):
                self.grid[row][col + i] = '-'  # Strike-through word with '-'
        elif direction == "vertical":
            for i in range(word_length):
                self.grid[row + i][col] = '-'
        elif direction == "diagonal":
            for i in range(word_length):
                self.grid[row + i][col + i] = '-'

        print(f"Word '{word}' has been struck through in the grid.")

if __name__ == "__main__":
    ws = WordSearch(10, 10)
    words = ["PYTHON", "JAVA", "CODE", "GRID", "SEARCH"]
    
    # Place the words in the grid
    for word in words:
        ws.place_word(word)
    
    # Fill the remaining spaces
    ws.fill_grid()
    
    # Show the initial grid
    print("Initial Grid:")
    ws.print_grid()
    
    # Start user interaction to find words
    while len(ws.found_words) < len(words):
        user_input = input("\nEnter a word you found: ").upper()
        ws.find_word(user_input)
        ws.print_grid()

    print(f"Game over! Final score: {ws.score}")
