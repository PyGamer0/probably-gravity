import numpy as np    # Numpy for vectors
import pyglet

# Class 

class body:
    def __init__(self, x, y, mass, vx=0, vy=0):
        self.position = np.array([x, y])
        self.velocity = np.array([vx, vy])
        self.acceleration = np.array([0, 0])
        self.mass = mass
        self.r = 25 * (self.mass / 2)

    def draw(self, color):
        shape = pyglet.shapes.Circle(self.position[0], self.position[1], self.r)
        shape.color = color
        shape.draw()

    def update(self):
        VELOCITY_CAP = 10
        if self.velocity[0] > VELOCITY_CAP:
            self.velocity[0] = VELOCITY_CAP
        if self.velocity[1] > VELOCITY_CAP:
            self.velocity[1] = VELOCITY_CAP

        if self.velocity[0] < -VELOCITY_CAP:
            self.velocity[0] = -VELOCITY_CAP
        if self.velocity[1] < -VELOCITY_CAP:
            self.velocity[1] = -VELOCITY_CAP

        self.velocity = self.velocity + self.acceleration
        self.position = self.position + self.velocity
        self.acceleration *= 0

    def apply_force(self, force):
        # self.acceleration += force / self.mass
        self.acceleration = self.acceleration + (force / self.mass)

    def gravity(self, other):
        distv = other.position - self.position
        dist = np.linalg.norm(distv)
        normal = distv / dist

        G = 1
        force = G * self.mass * other.mass * 1/dist * normal
        
        self.apply_force(force)


win = pyglet.window.Window(500, 500, "Gravity")

# Make bodies
# TODO: Make this expandible using a list
b1 = body(200, 200, 1, 0.1, 1)
b2 = body(300, 300, 1, -0.2, -1)
# b3 = body(200, 300, 1, 0.1, 0.1)

def update(dt):
    b1.gravity(b2)
    b2.gravity(b1)
    # b1.gravity(b3)
    # b2.gravity(b3)
    # b3.gravity(b1)
    # b3.gravity(b2)

    b1.update()
    b2.update()
    # b3.update()

@win.event
def on_draw():
    win.clear()
    b1.draw((245, 24, 134))
    b2.draw((145, 20, 233))
    # b3.draw((34, 234, 123))


pyglet.clock.schedule_interval(update, 1/999999)     # 60 frames per second (60 fps)
pyglet.app.run()

