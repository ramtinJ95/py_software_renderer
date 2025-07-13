import pyray
import numpy as np


class Display:
    def __init__(self, width: int, height: int, window_name: str):
        self.HEIGHT = height
        self.WIDTH = width
        self.window_name = window_name
        self.color_buffer = np.zeros((self.WIDTH, self.HEIGHT, 4), dtype=np.uint8)
        self.texture = None

    def render(self):
        if self.texture is None:
            self.texture = self.setup_texture()
        self.set_color_vectorized(255, 0, 0, 255)
        pyray.update_texture(
            self.texture, pyray.ffi.cast("void *", self.color_buffer.ctypes.data)
        )
        pyray.begin_drawing()
        pyray.clear_background([255, 255, 255, 255])
        pyray.draw_texture(self.texture, 0, 0, [0, 0, 0, 255])
        pyray.end_drawing()

    def setup_texture(self) -> pyray.Texture:
        image = pyray.gen_image_color(self.WIDTH, self.HEIGHT, pyray.BLANK)
        image.data = pyray.ffi.cast("unsigned char *", self.color_buffer.ctypes.data)
        texture = pyray.load_texture_from_image(image)
        return texture

    def set_color_vectorized(self, r: int, g: int, b: int, a: int):
        self.color_buffer[..., 0] = r
        self.color_buffer[..., 1] = g
        self.color_buffer[..., 2] = b
        self.color_buffer[..., 3] = a

    def draw_grid(self):
        pass

    def draw_rectangle(self):
        pass

    def update(self):
        pass

    def process_input(self):
        pass

    def main(self):
        pyray.init_window(self.WIDTH, self.HEIGHT, self.window_name)
        while not pyray.window_should_close():
            self.process_input()
            self.update()
            self.render()
        pyray.unload_texture(self.texture)
        pyray.close_window()
