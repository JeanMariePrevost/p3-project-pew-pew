import global_events


class RenderableFlashWrapper:
    def __init__(self, renderable, color_rgb, alpha, duration_ticks):
        self.renderable = renderable
        self.color_rgb = color_rgb
        self.alpha = alpha
        self.duration_ticks = duration_ticks
        self.ticks_remaining = duration_ticks
        global_events.tick_signal.add(self.tick)

    def tick(self):
        self.ticks_remaining -= 1
        # Calculate the current alpha value
        if self.ticks_remaining > 0:
            current_alpha = self.alpha * (self.ticks_remaining / self.duration_ticks)
            self.renderable.set_tint(self.color_rgb, current_alpha)
        else:
            global_events.tick_signal.remove(self.tick)
            self.renderable.set_tint((255, 255, 255), 0)

    def destroy(self):
        global_events.tick_signal.remove(self.tick)
        self.renderable = None  # Needed?
