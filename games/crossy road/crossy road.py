import pygame
import random
from pygame.locals import *

# initializing pygame
pygame.init()

#creating the screen
wn = pygame.display.set_mode((1900, 1000))
pygame.display.set_caption("crossy road")


BG = (144,201,120)
wn.fill(BG)

spawn_time = pygame.time.get_ticks()
cars = []

w = ['yes','no','no']
black = (0,0,0)

#loading my images
street_img = pygame.image.load(r"c:\Users\joe\OneDrive\Pictures\street.png")
car_img = pygame.image.load(r"c:\Users\joe\OneDrive\Pictures\car.png")
car_blue_img = pygame.image.load(r"c:\Users\joe\OneDrive\Pictures\car_blue.png")
cool_car_img = pygame.image.load(r"c:\Users\joe\OneDrive\Pictures\cool car.png")
bus_img = pygame.image.load(r"c:\Users\joe\OneDrive\Pictures\bus.png")
rail_img = pygame.image.load(r"c:\Users\joe\OneDrive\Pictures\rail.png")
train_img = pygame.image.load(r"c:\Users\joe\OneDrive\Pictures\train.png")
player_img = pygame.image.load(r"c:\Users\joe\OneDrive\Pictures\chicken.png")
bg_img = pygame.image.load(r"c:\Users\joe\OneDrive\Pictures\grass_bg.png")

#creating lists that I use to determine the street type and what side the cars/trains come from
side = ['left','right']
street_type = ['rail', 'street']
used_lane_ys = set()
LANE_HEIGHT = 108







#creating my player class
class Player(object):
    def __init__(self):
        self.img = player_img
        self.rect = player_img.get_rect()
        #where it will be placed
        self.rect.x = 500
        self.rect.y = 900 // LANE_HEIGHT * LANE_HEIGHT

        self.alive = True
        self.width = player_img.get_width()
        self.height = player_img.get_height()
    def draw(self,surface):
        #drawing the img and rectangle on to the screen
        surface.blit(self.img, self.rect)

#creating my street class
class street(object):
    def __init__(self):
        global used_lane_ys
        self.last_spawn_time = pygame.time.get_ticks()
        # decide type (rail or street)
        self.z = random.choice(street_type)
        if self.z == 'rail':
            self.img = rail_img
        else:
            self.img = street_img

        self.rect = self.img.get_rect()
        self.rect.x = 0

        # pick a free y row (multiples of 30, since player moves 30px)
        possible_positions = list(range(0, 1000, LANE_HEIGHT))
        free_positions = [y for y in possible_positions if y not in used_lane_ys]
        if free_positions:
            self.rect.y = random.choice(free_positions)
        else:
            self.rect.y = random.choice(possible_positions)


        # choose direction
        self.type = random.choice(side)

        # create vehicle depending on type/direction
        if self.type == 'right':
            if self.z == 'rail':
                self.car = Car('train', self.rect.y, -500)
            else:
                self.car = Car('car', self.rect.y, -500)
        else:
            if self.z == 'rail':
                self.car = Car('train', self.rect.y, 3000)
            else:
                self.car = Car('car', self.rect.y, 3000)

    def update(self):
        if self.type == 'right':
            self.car.move(False, True)
        else:
            self.car.move(True, False)

    def draw(self, surface):
        surface.blit(self.img, self.rect)
        self.car.draw(surface)


#my car class
class Car(object):
    def __init__(self,type,y,x):
        self.type = type
        if self.type == 'train':
            self.img = train_img
        else:
            j = random.choice(["z","l","h","m"])
            if j == "z":
                self.img = car_img
            elif j == "h":
                self.img = car_blue_img
            elif j == "l":
                self.img = cool_car_img
            else:
                self.img = bus_img
        self.rect = self.img.get_rect()
        #where it will be placed on the screen
        self.rect.y = y
        self.rect.x = x
    def move(self, moving_left, moving_right):
        dx = 0
        if self.type == 'train':
            speed = 7
        else:
            speed = 3   #cars slower than trains
        #if the moving left variable it true, then go left, other wise, go right
        if moving_left:
            dx = -speed
        if moving_right:
            dx = speed
        #add dx to self.rect.x so that the car/train actualy moves
        self.rect.x += dx

    def draw(self,surface):
        #drawing the car's image and rectangle onto the screen
        surface.blit(self.img,self.rect)


#creating my streets
p = street()
d = street()
a = street()
l = street()
m = street()
n = street()
o = street()
v = street()
c = street()
x = street()
z = street()
g = street()
u = street()
b = street()

#creating my player
player = Player()

run = True
lane_group = [p,a,d,l,m,n,o,v,c,x,z,g,u,b]
s = ['yes','no']
e = ['yes','no','no','no','no','no','no','no','no','no']

while run:
    #fill the background
    wn.fill(BG)
    wn.blit(bg_img, (0,0))

    #draw streets
    for lane in lane_group:
        lane.draw(wn)

    #spawn new cars every 500 miliseconds
    for lane in lane_group:
            if lane.z == 'street':
                h = random.choice(s)
            if lane.z == 'rail':
                h = random.choice(e)
            if h == 'yes':
                current_time = pygame.time.get_ticks()
                if lane.z == 'rail':
                    if current_time - lane.last_spawn_time > 5000:  # per-lane cooldown
                        lane.last_spawn_time = current_time
                        

                        

                        if lane.z == 'street':
                            vehicle_type = 'car'
                        else:
                            vehicle_type = 'train'
                        
                        #creating the cars and saying that if its left then the new vehicle's direction is left otherwise, its direction is right
                        if lane.type == 'left':
                            new_vehicle = Car(vehicle_type, lane.rect.y, 3000)
                            new_vehicle.direction = "left"
                        else:
                            new_vehicle = Car(vehicle_type, lane.rect.y, -500)
                            new_vehicle.direction = "right"
                        #add the vehicle to the list of cars/trains
                        cars.append(new_vehicle)
                else:
                    if current_time - lane.last_spawn_time > 1000:  # per-lane cooldown
                        lane.last_spawn_time = current_time
                        

                        

                        if lane.z == 'street':
                            vehicle_type = 'car'
                        else:
                            vehicle_type = 'train'
                        
                        #creating the cars and saying that if its left then the new vehicle's direction is left otherwise, its direction is right
                        if lane.type == 'left':
                            new_vehicle = Car(vehicle_type, lane.rect.y, 3000)
                            new_vehicle.direction = "left"
                        else:
                            new_vehicle = Car(vehicle_type, lane.rect.y, -500)
                            new_vehicle.direction = "right"
                        #add the vehicle to the list of cars/trains
                        cars.append(new_vehicle)

                #update and draw cars
                for v in cars[:]:
                    if v.direction == "left":
                        v.move(True, False)
                    else:
                        v.move(False, True)

                    v.draw(wn)

                    #remove off-screen
                    if v.rect.x < -200 or v.rect.x > 3000:
                        cars.remove(v)
    for lane in lane_group[:]:
        if lane.rect.y > 1000:  # off-screen bottom
            lane_group.remove(lane)

            # find the highest current lane
            top_y = min(l.rect.y for l in lane_group)

            # place the new lane one step above it
            new_lane = street()
            i = random.choice(w)
            if i == 'no':
                new_lane.rect.y = top_y - LANE_HEIGHT
            elif i == 'yes':
                new_lane.rect.y = top_y - top_y
            lane_group.append(new_lane)

    #update player
    player.draw(wn)
    # --- check for collisions with cars/trains ---
    for v in cars:
        if player.rect.colliderect(v.rect):
            player.alive = False
            print("YOU GOT HIT!")  # optional debug line
    if not player.alive:
        wn.fill((255, 0, 0))  # red flash
        font = pygame.font.SysFont(None, 100)
        text = font.render("YOU DIED!", True, (255, 255, 255))
        wn.blit(text, (750, 400))
        pygame.display.update()
        pygame.time.delay(1500)

        # reset position
        player.rect.x = 500
        player.rect.y = 900 // LANE_HEIGHT * LANE_HEIGHT
        player.alive = True
        cars.clear()  # remove all cars so you don't insta-die again

    
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                for lane in lane_group:
                    # move the lane
                    lane.rect.y += 54

                    # also move this lane's first car
                    lane.car.rect.y += 54  

                for v in cars:
                    v.rect.y += 54  # move all the extra spawned cars too
            if event.key == K_LEFT:
                player.rect.x -= 30
            if event.key == K_RIGHT:
                player.rect.x += 30
        
            
        




    pygame.display.update()

pygame.quit()
