from core.base import Base


class Test(Base):
    def initialize(self):
        print("initializing programm...")

    def update(self):
        pass


Test().run()


