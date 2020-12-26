class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('The beginning of the drawing: Stationery')


class Pen(Stationery):
    def draw(self):
        print('The beginning of the drawing: Pen')


class Pencil(Stationery):
    def draw(self):
        print('The beginning of the drawing: Pencil')


class Handle(Stationery):
    def draw(self):
        print('The beginning of the drawing: Handle')


stationery = Stationery('Python')
stationery.draw()

pen = Pen('Python')
pen.draw()

pencil = Pencil('Python')
pencil.draw()

handle = Handle('Python')
handle.draw()
