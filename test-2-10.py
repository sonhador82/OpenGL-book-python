from core.base import Base


class Test(Base):

    def initialize(self):
        print("init programm")

    def update(self):
        if len(self.input.keyDownList) > 0:
            print("Keys down:", self.input.keyDownList)

        if len(self.input.keyPressedList) > 0:
            print("keys pressed:", self.input.keyPressedList)

        if len(self.input.keyUpList) > 0:
            print("Keys up:", self.input.keyUpList)


Test().run()
