import pygame
import random
import os
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game constants
GRAVITY = 0.5
JUMP_STRENGTH = -8
OBSTACLE_SPEED = 3
OBSTACLE_SPAWN_RATE = 90  # Frames between obstacle spawns
SCROLL_SPEED = 2

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.width = 60
        self.height = 60
        
        # Smaller hitbox (70% of sprite, centered)
        self.hitbox_scale = 0.7
        self.hitbox_width = int(self.width * self.hitbox_scale)
        self.hitbox_height = int(self.height * self.hitbox_scale)
        self.hitbox_offset_x = (self.width - self.hitbox_width) // 2
        self.hitbox_offset_y = (self.height - self.hitbox_height) // 2
        
        # Load player image (flying horse)
        image_path = os.path.join("Images", "Flying_horse_with_wings", "rotations", "east.png")
        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        except:
            # Fallback to a colored rectangle if image not found
            self.image = None
            self.color = BLUE
    
    def jump(self):
        self.velocity = JUMP_STRENGTH
    
    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        
        # Keep player on screen
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        if self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.velocity = 0
    
    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def get_rect(self):
        # Return smaller hitbox for more forgiving gameplay
        return pygame.Rect(
            self.x + self.hitbox_offset_x,
            self.y + self.hitbox_offset_y,
            self.hitbox_width,
            self.hitbox_height
        )

class Obstacle:
    def __init__(self, x, y, image_path, movement_type="horizontal"):
        self.x = x
        self.y = y
        self.movement_type = movement_type
        self.base_speed = OBSTACLE_SPEED + random.uniform(-1, 1)
        
        # Load obstacle image
        try:
            self.image = pygame.image.load(image_path)
            # Scale image to reasonable size
            original_width, original_height = self.image.get_size()
            scale_factor = random.uniform(0.5, 1.2)
            self.width = int(original_width * scale_factor)
            self.height = int(original_height * scale_factor)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        except:
            self.image = None
            self.width = 50
            self.height = 50
            self.color = RED
        
        # Smaller hitbox (65% of image size, centered)
        self.hitbox_scale = 0.65
        self.hitbox_width = int(self.width * self.hitbox_scale)
        self.hitbox_height = int(self.height * self.hitbox_scale)
        self.hitbox_offset_x = (self.width - self.hitbox_width) // 2
        self.hitbox_offset_y = (self.height - self.hitbox_height) // 2
        
        # Movement parameters
        self.vertical_speed = random.uniform(-2, 2) if movement_type == "diagonal" else 0
        self.vertical_direction = 1
        self.oscillation_amplitude = random.randint(20, 60) if movement_type == "oscillating" else 0
        self.oscillation_speed = random.uniform(0.05, 0.15) if movement_type == "oscillating" else 0
        self.oscillation_offset = 0
        self.base_y = y  # Store original Y for oscillation
    
    def update(self):
        # Horizontal movement (always moves left)
        self.x -= self.base_speed
        
        # Vertical movement based on type
        if self.movement_type == "diagonal":
            self.y += self.vertical_speed
            # Bounce off top and bottom
            if self.y <= 0 or self.y >= SCREEN_HEIGHT - self.height:
                self.vertical_speed *= -1
        elif self.movement_type == "oscillating":
            self.oscillation_offset += self.oscillation_speed
            self.y = self.base_y + self.oscillation_amplitude * math.sin(self.oscillation_offset)
            # Keep within bounds
            if self.y < 0:
                self.y = 0
            elif self.y > SCREEN_HEIGHT - self.height:
                self.y = SCREEN_HEIGHT - self.height
    
    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def get_rect(self):
        # Return smaller hitbox instead of full image size
        return pygame.Rect(
            self.x + self.hitbox_offset_x,
            self.y + self.hitbox_offset_y,
            self.hitbox_width,
            self.hitbox_height
        )
    
    def is_off_screen(self):
        return self.x + self.width < 0

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Horse")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        
        # Load background
        bg_path = os.path.join("Images", "background.jfif")
        try:
            self.background = pygame.image.load(bg_path)
            self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except:
            self.background = None
        
        # Obstacle image paths
        self.obstacle_paths = [
            os.path.join("Images", "meteor.jfif"),
            os.path.join("Images", "missile.png"),
            os.path.join("Images", "ufo.png"),
            os.path.join("Images", "Man_drving_a_small_airplane", "rotations", "west.png"),
        ]
        
        self.reset()
    
    def reset(self):
        self.player = Player(100, SCREEN_HEIGHT // 2)
        self.obstacles = []
        self.score = 0
        self.game_over = False
        self.frame_count = 0
        self.bg_offset = 0
    
    def spawn_obstacle(self):
        # Choose random obstacle image
        image_path = random.choice(self.obstacle_paths)
        
        # Choose random movement type
        movement_types = ["horizontal", "diagonal", "oscillating"]
        movement_type = random.choice(movement_types)
        
        # Spawn at random Y position
        y = random.randint(50, SCREEN_HEIGHT - 150)
        
        obstacle = Obstacle(SCREEN_WIDTH, y, image_path, movement_type)
        self.obstacles.append(obstacle)
    
    def check_collisions(self):
        player_rect = self.player.get_rect()
        
        for obstacle in self.obstacles:
            if player_rect.colliderect(obstacle.get_rect()):
                return True
        
        return False
    
    def update(self):
        if self.game_over:
            return
        
        self.frame_count += 1
        self.bg_offset = (self.bg_offset - SCROLL_SPEED) % SCREEN_WIDTH
        
        # Update player
        self.player.update()
        
        # Spawn obstacles
        if self.frame_count % OBSTACLE_SPAWN_RATE == 0:
            self.spawn_obstacle()
        
        # Update obstacles
        for obstacle in self.obstacles[:]:
            obstacle.update()
            if obstacle.is_off_screen():
                self.obstacles.remove(obstacle)
                self.score += 1
        
        # Check collisions
        if self.check_collisions():
            self.game_over = True
    
    def draw(self):
        # Draw background
        if self.background:
            # Draw two copies for seamless scrolling
            self.screen.blit(self.background, (self.bg_offset, 0))
            self.screen.blit(self.background, (self.bg_offset + SCREEN_WIDTH, 0))
        else:
            self.screen.fill((135, 206, 235))  # Sky blue
        
        # Draw player
        self.player.draw(self.screen)
        
        # Draw obstacles
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw game over screen
        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            game_over_text = self.big_font.render("GAME OVER", True, RED)
            score_final_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
            restart_text = self.font.render("Press R to Restart or ESC to Quit", True, WHITE)
            
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
            score_rect = score_final_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
            
            self.screen.blit(game_over_text, text_rect)
            self.screen.blit(score_final_text, score_rect)
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def run(self):
        running = True
        
        while running:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.game_over:
                            self.reset()
                        else:
                            self.player.jump()
                    elif event.key == pygame.K_r and self.game_over:
                        self.reset()
                    elif event.key == pygame.K_ESCAPE:
                        running = False
            
            self.update()
            self.draw()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
