import pyray
import numpy as np


class Display:
    def __init__(self, width: int, height: int, window_name: str):
        self.HEIGHT = height
        self.WIDTH = width
        self.window_name = window_name
        self.color_buffer = np.zeros((self.WIDTH, self.HEIGHT, 4), dtype=np.uint8)
        self.texture = None

    def color(self, r: int, g: int, b: int, a=255) -> np.ndarray:
        return np.array([r, g, b, a], dtype=np.uint16)

    def render(self):
        if self.texture is None:
            self.texture = self.setup_texture()
        # self.set_color_vectorized(255, 0, 0, 255)
        # self.draw_grid(10)
        color = self.color(0, 255, 0)
        self.draw_rectangle(150, 150, 100, 100, color)
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

    def draw_rectangle(
        self, x: int, y: int, height: int, width: int, color: np.ndarray
    ):
        # Clip rectangle if it goes outside the screen
        x_end = min(x + width, self.color_buffer.shape[1])
        y_end = min(y + height, self.color_buffer.shape[0])
        x = max(x, 0)
        y = max(y, 0)

        # Fill the rectangle area
        self.color_buffer[y:y_end, x:x_end] = color

    def draw_grid(self, grid_size: int):
        grid_color = self.color(100, 100, 100)
        for y in range(0, self.HEIGHT, grid_size):
            self.color_buffer[:, y, :] = grid_color

        for x in range(0, self.WIDTH, grid_size):
            self.color_buffer[x, :, :] = grid_color

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
