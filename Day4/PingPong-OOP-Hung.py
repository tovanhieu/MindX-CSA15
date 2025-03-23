import pygame, sys, random

class PongGame:
    def __init__(self):
        # General setup
        pygame.mixer.pre_init(44100,-16,1, 1024)
        pygame.init()
        self.clock = pygame.time.Clock()

        # Main Window
        self.screen_width = 1280
        self.screen_height = 960
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Pong')

        # Colors
        self.light_grey = (200, 200, 200)
        self.bg_color = pygame.Color('grey12')

        # Game Variables
        self.ball_speed_x = 7 * random.choice((1, -1))
        self.ball_speed_y = 7 * random.choice((1, -1))
        self.player_speed = 0
        self.opponent_speed = 7
        self.ball_moving = False
        self.score_time = True

        # Game Rectangles
        self.ball = pygame.Rect(self.screen_width / 2 - 15, self.screen_height / 2 - 15, 30, 30)
        self.player = pygame.Rect(self.screen_width - 20, self.screen_height / 2 - 70, 10, 140)
        self.opponent = pygame.Rect(10, self.screen_height / 2 - 70, 10, 140)

        # Score Text
        self.player_score = 0
        self.opponent_score = 0

    def ball_animation(self):
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        if self.ball.top <= 0 or self.ball.bottom >= self.screen_height:
            self.ball_speed_y *= -1

        # Player Score
        if self.ball.left <= 0:
            self.score_time = pygame.time.get_ticks()
            self.player_score += 1

        # Opponent Score
        if self.ball.right >= self.screen_width:
            self.score_time = pygame.time.get_ticks()
            self.opponent_score += 1

        if self.ball.colliderect(self.player) and self.ball_speed_x > 0:
            if abs(self.ball.right - self.player.left) < 10:
                self.ball_speed_x *= -1
            elif abs(self.ball.bottom - self.player.top) < 10 and self.ball_speed_y > 0:
                self.ball_speed_y *= -1
            elif abs(self.ball.top - self.player.bottom) < 10 and self.ball_speed_y < 0:
                self.ball_speed_y *= -1

        if self.ball.colliderect(self.opponent) and self.ball_speed_x < 0:
            if abs(self.ball.left - self.opponent.right) < 10:
                self.ball_speed_x *= -1
            elif abs(self.ball.bottom - self.opponent.top) < 10 and self.ball_speed_y > 0:
                self.ball_speed_y *= -1
            elif abs(self.ball.top - self.opponent.bottom) < 10 and self.ball_speed_y < 0:
                self.ball_speed_y *= -1

    def player_animation(self):
        self.player.y += self.player_speed

        if self.player.top <= 0:
            self.player.top = 0
        if self.player.bottom >= self.screen_height:
            self.player.bottom = self.screen_height

    def opponent_ai(self):
        if self.opponent.top < self.ball.y:
            self.opponent.y += self.opponent_speed
        if self.opponent.bottom > self.ball.y:
            self.opponent.y -= self.opponent_speed

        if self.opponent.top <= 0:
            self.opponent.top = 0
        if self.opponent.bottom >= self.screen_height:
            self.opponent.bottom = self.screen_height

    def ball_start(self):
        self.ball.center = (self.screen_width / 2, self.screen_height / 2)
        current_time = pygame.time.get_ticks()

        if current_time - self.score_time < 2100:
            self.ball_speed_y, self.ball_speed_x = 0, 0
        else:
            self.ball_speed_x = 7 * random.choice((1, -1))
            self.ball_speed_y = 7 * random.choice((1, -1))
            self.score_time = None

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player_speed -= 6
                    if event.key == pygame.K_DOWN:
                        self.player_speed += 6
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.player_speed += 6
                    if event.key == pygame.K_DOWN:
                        self.player_speed -= 6

            # Game Logic
            self.ball_animation()
            self.player_animation()
            self.opponent_ai()

            # Visuals
            self.screen.fill(self.bg_color)
            pygame.draw.rect(self.screen, self.light_grey, self.player)
            pygame.draw.rect(self.screen, self.light_grey, self.opponent)
            pygame.draw.ellipse(self.screen, self.light_grey, self.ball)
            pygame.draw.aaline(self.screen, self.light_grey, (self.screen_width / 2, 0),
                               (self.screen_width / 2, self.screen_height))

            if self.score_time:
                self.ball_start()

            pygame.display.flip()
            self.clock.tick(60)

game = PongGame()
game.run()