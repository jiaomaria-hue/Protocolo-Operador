import pygame
import sys
import random
import math
from pygame import gfxdraw

# --- CONFIGURAÇÕES VISUAIS ---
WIDTH, HEIGHT = 1000, 750
FPS = 60

# Palette Neon Intensa e Fundos Complexos
COLOR_BG = (6, 8, 16)
COLOR_GRID_PRIMARY = (20, 28, 48)
COLOR_TEXT_MAIN = (230, 245, 255)
COLOR_TEXT_GLOW = (0, 255, 230) # Ciano

# Cores dos Botões (Neon)
COLOR_BTN_DEFAULT = (40, 50, 70)
COLOR_BTN_HOVER = (70, 90, 120)
COLOR_BTN_SELECT = (255, 10, 110) # Magenta laser
COLOR_CORRECT = (50, 255, 100)    # Verde neon
COLOR_WRONG = (255, 60, 60)       # Vermelho neon

# --- BASE DE DADOS DO QUIZ (Cyberpunk/Python) ---
QUESTIONS = [
    {
        "q": "Qual elemento do Pygame é fundamental para suavizar bordas de geometria e texto, criando um visual 'anti-aliased'?",
        "opts": ["A) pygame.draw.circle", "B) pygame.transform", "C) pygame.font.SysFont", "D) pygame.gfxdraw"],
        "ans": 3 # Índice da resposta correta
    },
    {
        "q": "No estilo Neon Vector Arcade, como é gerado o efeito de 'Glow' procedimentalmente?",
        "opts": ["A) Usando uma imagem pré-renderizada.", "B) Sobrepondo múltiplas superfícies translúcidas.", "C) Ativando HWSURFACE no mixer.", "D) Aumentando a resolução da tela."],
        "ans": 1
    },
    {
        "q": "Para animar as partículas de uma explosão com suavidade, qual cálculo deve ser aplicado à velocidade (self.vel) a cada frame?",
        "opts": ["A) self.vel += aceleracao", "B) self.vel = random.uniform()", "C) self.vel *= desaceleracao", "D) self.vel = math.atan2()"],
        "ans": 2
    }
]

# --- FUNÇÕES AUXILIARES DE RENDERIZAÇÃO ---
def draw_neon_glow_rect(surface, color, rect, radius, layers=5):
    """Desenha múltiplas camadas de retângulos translúcidos para criar efeito de brilho."""
    r, g, b = color
    base_alpha = 70
    
    for i in range(layers):
        current_radius = radius + (i * 2.5)
        # alpha diminui com a distância
        alpha = max(5, base_alpha - (i * (base_alpha // layers)))
        
        # Cria uma superfície translúcida temporária
        glow_surf = pygame.Surface((rect.width + current_radius*2, rect.height + current_radius*2), pygame.SRCALPHA)
        # Desenha o retângulo suavizado na superfície temporária
        gfxdraw.box(glow_surf, (0, 0, glow_surf.get_width(), glow_surf.get_height()), (r, g, b, alpha))
        
        # Blit na superfície principal centralizado
        surface.blit(glow_surf, (rect.x - current_radius, rect.y - current_radius))

def draw_text_tech(surface, font, text, color, glow_color, pos, center=False):
    """Renderiza texto com brilho (glow) procedimental."""
    # Renderiza o brilho (levemente maior e translúcido)
    txt_glow = font.render(text, True, glow_color)
    txt_glow.set_alpha(120)
    
    # Renderiza o texto principal (nítido)
    txt_main = font.render(text, True, color)
    
    if center:
        rect_g = txt_glow.get_rect(center=pos)
        rect_m = txt_main.get_rect(center=pos)
        surface.blit(txt_glow, (rect_g.x + 2, rect_g.y + 2)) # Offset leve
        surface.blit(txt_main, rect_m)
    else:
        surface.blit(txt_glow, (pos[0] + 2, pos[1] + 2))
        surface.blit(txt_main, pos)

# --- CLASSE DE PARTÍCULA (Suavizada) ---
class Particle:
    def __init__(self, x, y, color):
        self.pos = pygame.math.Vector2(x, y)
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 6)
        self.vel = pygame.math.Vector2(math.cos(angle) * speed, math.sin(angle) * speed)
        self.lifetime = random.randint(20, 40)
        self.color = color
        self.base_radius = random.uniform(1.5, 4.5)

    def update(self):
        self.pos += self.vel
        self.vel *= 0.95 # Desaceleração suave
        self.lifetime -= 1

    def draw(self, surface):
        if self.lifetime > 0:
            ratio = self.lifetime / 40
            r, g, b = self.color
            alpha = int(255 * ratio)
            gfxdraw.filled_circle(surface, int(self.pos.x), int(self.pos.y), int(self.base_radius * ratio), (r, g, b, alpha))

# --- CLASSE DE BOTÃO DE RESPOSTA (Stylized) ---
class OptionButton:
    def __init__(self, x, y, w, h, text, index):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.index = index
        self.state = "normal" # normal, hover, correct, wrong
        self.particles = []

    def handle_event(self, event, mouse_pos):
        if self.state in ["correct", "wrong"]: return False # Desativa após seleção
        
        if self.rect.collidepoint(mouse_pos):
            if self.state == "normal": self.state = "hover"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return True # Foi clicado
        else:
            if self.state == "hover": self.state = "normal"
        return False

    def draw(self, surface, font):
        # Seleciona a cor do brilho com base no estado
        if self.state == "normal": color, glow = COLOR_BTN_DEFAULT, COLOR_BTN_DEFAULT
        elif self.state == "hover": color, glow = COLOR_BTN_HOVER, COLOR_TEXT_GLOW
        elif self.state == "correct": color, glow = COLOR_CORRECT, COLOR_CORRECT
        elif self.state == "wrong": color, glow = COLOR_WRONG, COLOR_WRONG

        # Desenha Glow Procedimental
        draw_neon_glow_rect(surface, glow, self.rect, radius=5, layers=6)
        
        # Borda AA e Preenchimento
        gfxdraw.box(surface, self.rect, color)
        gfxdraw.rect(surface, self.rect.x, self.rect.y, self.rect.w, self.rect.h, (100, 130, 150))
        
        # Texto da Opção com Glow
        txt_pos = (self.rect.x + 25, self.rect.centery - font.get_height()//2)
        draw_text_tech(surface, font, self.text, COLOR_TEXT_MAIN, COLOR_TEXT_GLOW, txt_pos)

# --- GERENCIADOR DO QUIZ ---
class QuizGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("CYBERQUIZ OVERCLOCK - Neon Edition")
        self.clock = pygame.time.Clock()
        
        # Fontes Tech
        try:
            self.font_q = pygame.font.SysFont("Consolas", 24, bold=True)
            self.font_opt = pygame.font.SysFont("Consolas", 18)
            self.font_hud = pygame.font.SysFont("Consolas", 20)
        except:
            self.font_q = pygame.font.SysFont(None, 32)
            self.font_opt = pygame.font.SysFont(None, 24)
            self.font_hud = pygame.font.SysFont(None, 26)

        self.current_q = 0
        self.score = 0
        self.state = "QUIZ" # QUIZ, FEEDBACK, GAME_OVER
        self.feedback_timer = 0
        self.buttons = []
        self.particles = []
        self.load_question()

    def load_question(self):
        if self.current_q >= len(QUESTIONS):
            self.state = "GAME_OVER"
            return

        q_data = QUESTIONS[self.current_q]
        self.buttons = []
        
        # Cria 4 botões centralizados
        start_y = 280
        btn_w, btn_h = 750, 65
        for i, opt in enumerate(q_data["opts"]):
            btn = OptionButton((WIDTH - btn_w)//2, start_y + (i * 85), btn_w, btn_h, opt, i)
            self.buttons.append(btn)

    def trigger_feedback(self, selected_index, correct_index):
        # Partículas de acerto ou erro
        color = COLOR_CORRECT if selected_index == correct_index else COLOR_WRONG
        btn = self.buttons[selected_index]
        for _ in range(30):
            self.particles.append(Particle(btn.rect.centerx, btn.rect.centery, color))
            
        # Atualiza o estado dos botões para visual
        if selected_index == correct_index:
            self.score += 1000
            btn.state = "correct"
        else:
            btn.state = "wrong"
            self.buttons[correct_index].state = "correct" # Mostra a correta

        self.state = "FEEDBACK"
        self.feedback_timer = pygame.time.get_ticks()

    def update(self):
        # Atualiza partículas
        for p in self.particles[:]:
            p.update()
            if p.lifetime <= 0: self.particles.remove(p)

        # Avança após feedback
        if self.state == "FEEDBACK":
            if pygame.time.get_ticks() - self.feedback_timer > 1500:
                self.current_q += 1
                self.state = "QUIZ"
                self.load_question()

    def draw(self):
        # Fundo Complexo (Superfície de Glow Base)
        self.screen.fill(COLOR_BG)
        bg_glow = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        for x in range(0, WIDTH, 50):
            gfxdraw.vline(bg_glow, x, 0, HEIGHT, (COLOR_GRID_PRIMARY[0], COLOR_GRID_PRIMARY[1], COLOR_GRID_PRIMARY[2], 100))
        for y in range(0, HEIGHT, 50):
            gfxdraw.hline(bg_glow, 0, WIDTH, y, (COLOR_GRID_PRIMARY[0], COLOR_GRID_PRIMARY[1], COLOR_GRID_PRIMARY[2], 100))
        self.screen.blit(bg_glow, (0, 0))

        # Renderiza Partículas
        for p in self.particles:
            p.draw(self.screen)

        if self.state in ["QUIZ", "FEEDBACK"]:
            # Card da Pergunta (Stylized with Glow)
            q_rect = pygame.Rect(80, 60, 840, 160)
            draw_neon_glow_rect(self.screen, COLOR_TEXT_GLOW, q_rect, radius=8, layers=7)
            
            gfxdraw.box(self.screen, q_rect, (COLOR_BG[0]+10, COLOR_BG[1]+10, COLOR_BG[2]+20))
            gfxdraw.rect(self.screen, q_rect.x, q_rect.y, q_rect.w, q_rect.h, COLOR_TEXT_GLOW)
            
            # Texto da Pergunta (com quebra de linha manual para simplificar)
            q_text = QUESTIONS[self.current_q]["q"]
            txt_surf = self.font_q.render(f"Q{self.current_q+1}: {q_text}", True, COLOR_TEXT_MAIN)
            self.screen.blit(txt_surf, (q_rect.x + 30, q_rect.centery - txt_surf.get_height()//2))

            # Desenha Botões
            for btn in self.buttons:
                btn.draw(self.screen, self.font_opt)

            # HUD
            draw_text_tech(self.screen, self.font_hud, f"// ACCESS_SCORE: {self.score:06d}", COLOR_TEXT_MAIN, COLOR_TEXT_GLOW, (WIDTH - 280, 30))

        elif self.state == "GAME_OVER":
            draw_text_tech(self.screen, self.font_q, "SYS_ACCESS_COMPLETED", COLOR_CORRECT, COLOR_CORRECT, (WIDTH // 2, HEIGHT // 2 - 40), center=True)
            draw_text_tech(self.screen, self.font_opt, f"Final Score: {self.score}", COLOR_TEXT_MAIN, COLOR_TEXT_GLOW, (WIDTH // 2, HEIGHT // 2 + 10), center=True)

        pygame.display.flip()

    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.state == "QUIZ":
                    for idx, btn in enumerate(self.buttons):
                        if btn.handle_event(event, mouse_pos):
                            self.trigger_feedback(idx, QUESTIONS[self.current_q]["ans"])

            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = QuizGame()
    game.run()