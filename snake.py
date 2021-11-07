import pygame, time, random, sys

class Snake:
    def __init__ (self, x, y, w):
        self.x = x
        self.y = y
        self.w = w
        self.direction = None
        self.tail_length = 1
        self.tail = []
        self.colors = {
            'green': (20, 255, 50),
            'red': (255, 20, 50)
        }
        self.food = {
            'x': random.randrange(0, 24) * 20,
            'y': random.randrange(0, 24) * 20
        }
        self.frame_rate = 0.1

    def render (self, window):
        # Render snake
        pygame.draw.rect(window, self.colors['green'], (self.x, self.y, self.w, self.w), 2)

        # Render snake tail
        for tail_section in self.tail:
            pygame.draw.rect(window, self.colors['green'], (tail_section['x'], tail_section['y'], self.w, self.w), 2)

        # Render food
        pygame.draw.rect(window, self.colors['red'], (self.food['x'], self.food['y'], self.w, self.w), 2)


    def keyboard_events (self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and self.direction != 'left':
                    self.direction = 'right'
                elif event.key == pygame.K_a and self.direction != 'right':
                    self.direction = 'left'
                elif event.key == pygame.K_w and self.direction != 'down':
                    self.direction = 'up'
                elif event.key == pygame.K_s and self.direction != 'up':
                    self.direction = 'down'

    def generate_food (self):
        # Adds a new tail section
        self.tail_length += 1

        # Speeds up the game
        if self.frame_rate > 0.06:
            self.frame_rate -= 0.001

        # Generates a new food at a random position
        self.food['x'] = random.randrange(0, 24) * 20
        self.food['y'] = random.randrange(0, 24) * 20

    def collisions (self):
        for tail_section_index, tail_section in enumerate(self.tail):
            if self.x == tail_section['x'] and self.y == tail_section['y'] and tail_section_index < len(self.tail) - 1:
                print('Game Over!')
                pygame.quit()
                sys.exit(0)

            if self.x < 0 or self.y < 0 or self.x > 500 or self.y > 500:
                print('Game Over!')
                pygame.quit()
                sys.exit(0)


    def update (self):
        # Movement based on direction
        if self.direction == 'right':
            self.x += self.w
        elif self.direction == 'left':
            self.x -= self.w
        elif self.direction == 'up':
            self.y -= self.w
        elif self.direction == 'down':
            self.y += self.w

        # Keep an history of the tail positions
        self.tail.append({ 'x': self.x, 'y': self.y })
        
        if len(self.tail) > self.tail_length:
            self.tail.pop(0)

        # Generate a new food when food is eated
        if self.x == self.food['x'] and self.y == self.food['y']:
            self.generate_food()
        
        # Framerate
        time.sleep(self.frame_rate)
