import pyray
import display
import numpy as np

# WIDTH = 800
# HEIGHT = 800
#
# pyray.init_window(WIDTH, HEIGHT, "Software Renderer")
# pyray.set_target_fps(60)
#
# # Pixel buffer (RGBA)
# color_buffer = np.zeros((HEIGHT, WIDTH, 4), dtype=np.uint8)
#
# # Initial image + texture
# image = pyray.gen_image_color(WIDTH, HEIGHT, pyray.BLANK)
# image.data = pyray.ffi.cast("unsigned char *", color_buffer.ctypes.data)
# texture = pyray.load_texture_from_image(image)
#
#
# def color(r: int, g: int, b: int, a=255) -> np.ndarray:
#     return np.array([r, g, b, a], dtype=np.uint16)
#
#
# def set_color_vectorized(r: int, g: int, b: int, a: int):
#     color_buffer[..., 0] = r
#     color_buffer[..., 1] = g
#     color_buffer[..., 2] = b
#     color_buffer[..., 3] = a
#
#
# def draw_grid(grid_spacing: int):
#     grid_color = np.array([100, 100, 100, 255], dtype=np.uint8)
#
#     for y in range(0, HEIGHT, grid_spacing):
#         color_buffer[y, :, :] = grid_color  # horizontal line
#
#     for x in range(0, WIDTH, grid_spacing):
#         color_buffer[:, x, :] = grid_color  # vertical line
#
#
# def draw_rectangle(x: int, y: int, height: int, width: int, color: np.ndarray):
#     # Clip rectangle if it goes outside the screen
#     x_end = min(x + width, color_buffer.shape[1])
#     y_end = min(y + height, color_buffer.shape[0])
#     x = max(x, 0)
#     y = max(y, 0)
#
#     # Fill the rectangle area
#     color_buffer[y:y_end, x:x_end] = color
#
#
# while not pyray.window_should_close():
#     # set_color_vectorized(255, 0, 0, 255)
#     red = color(255, 0, 0)
#     draw_grid(10)
#     draw_rectangle(300, 300, 100, 100, red)
#
#     # Send to GPU
#     pyray.update_texture(texture, pyray.ffi.cast("void *", color_buffer.ctypes.data))
#
#     # Draw
#     pyray.begin_drawing()
#     pyray.clear_background(pyray.BLACK)
#     pyray.draw_texture(texture, 0, 0, pyray.WHITE)
#     pyray.end_drawing()
#
#
# pyray.unload_texture(texture)
# pyray.close_window()
#
if __name__ == "__main__":
    display = display.Display(800, 800, "Software Renderer")
    display.main()
