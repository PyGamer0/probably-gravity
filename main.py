from freegames import vector
import pyglet as p

class entity:
    def __init__(self, m, x, y):
        self.pos = vector(x, y)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)
        self.mass = m

    def apply_force(self, f):
        self.acc += f / self.mass

    def apply_gravity(self, other):
        # Calculate distances
        dx = other.pos.x - self.pos.x
        dy = other.pos.y - self.pos.y

        # Normalize
        m = (dx ** 2 + dy ** 2) ** 0.5
        n = vector(dx / m, dy / m)

        # Force
        f = 1/10 * vector(other.mass / n.x, other.mass / n.y)

        self.apply_force(f)


    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self, c, r):
        shape = p.shapes.Circle(self.pos.x, self.pos.y, r)
        shape.color = c
        shape.draw()

win = p.window.Window(width=500, height=500)
e1 = entity(1, 200, 200)
e2 = entity(1, 300, 300)

def update(t):
    e1.update()
    e2.update()

    e1.apply_gravity(e2)
    # e1.apply_force(vector(0.01, 0.0000751))

    e2.apply_gravity(e1)
    # e2.apply_force(vector(-0.01, -0.0000751))

@win.event
def on_draw():
    win.clear()
    e1.draw((217, 32, 134), 25)
    e2.draw((31, 103, 231), 25)

p.clock.schedule_interval(update, 1/2048)
p.app.run()

