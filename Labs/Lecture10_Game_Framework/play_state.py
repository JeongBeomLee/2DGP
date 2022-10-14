from pico2d import *
import game_framework
import logo_state
import title_state

boy = None
grass = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    #global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
    delay(0.1)

def enter(): # 초기화
    global boy, grass
    boy = Boy()
    grass = Grass()

def exit():  # 종료
    global boy, grass
    del boy, grass

def update(): # 월드에 존재하는 객체들을 업데이트한다
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()





