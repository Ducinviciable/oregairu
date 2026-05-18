init python:

    class DrawImage(renpy.Displayable):

        def __init__(self, child, opaque_distance, transparent_distance, **kwargs):
            super(DrawImage, self).__init__(**kwargs)

            self.child = renpy.displayable(child)
            
            self.width = 0
            self.height = 0

        def render(self, width, height, st, at):
            t = Transform(child=self.child)

            child_render = renpy.render(t, width, height, st, at)

            self.width, self.height = child_render.get_size()

            render = renpy.Render(self.width, self.height)
            render.blit(child_render, (0, 0))

            return render