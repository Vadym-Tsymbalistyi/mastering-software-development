class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct_pizza(self):
        self.builder \
            .add_dough() \
            .add_filling() \
            .build()





