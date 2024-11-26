import numpy as np
import matplotlib.pyplot as plt
import re

class GraphPlotter:
    def __init__(self, figure, ax, canvas, colors):
        self.figure = figure
        self.ax = ax
        self.canvas = canvas
        self.colors = colors

    def plot(self, func_str, x_min, x_max):
        try:
            self.ax.clear()
            x = np.linspace(x_min, x_max, 1000)
            
            # Convert carets to ** for Python evaluation
            func_str = func_str.replace('^', '**')
            
            # Add 'np.' prefix to numpy functions
            for func in ['sin', 'cos', 'tan', 'exp', 'abs', 'floor']:
                func_str = re.sub(f'(?<!np\\.){func}(?!\\()', f'np.{func}(x)', func_str)
                func_str = re.sub(f'(?<!np\\.){func}\\(', f'np.{func}(', func_str)
            
            # Safe math functions namespace
            safe_dict = {
                "x": x,
                "np": np,
                "sin": np.sin,
                "cos": np.cos,
                "tan": np.tan,
                "exp": np.exp,
                "abs": abs,
                "floor": np.floor,
                "pi": np.pi,
                "e": np.e
            }
            
            y = eval(func_str, {"__builtins__": {}}, safe_dict)
            
            self._style_and_draw_plot(x, y)
            return True
            
        except Exception as e:
            self._draw_error()
            return False

    def _style_and_draw_plot(self, x, y):
        self.ax.plot(x, y, color=self.colors['accent'], linewidth=2)
        self.ax.grid(True, linestyle='--', alpha=0.7)
        self.ax.axhline(y=0, color=self.colors['text'], linestyle='-', linewidth=0.5, alpha=0.5)
        self.ax.axvline(x=0, color=self.colors['text'], linestyle='-', linewidth=0.5, alpha=0.5)
        self.canvas.draw()

    def _draw_error(self):
        self.ax.clear()
        self.ax.text(0.5, 0.5, 'Error', 
                    horizontalalignment='center',
                    verticalalignment='center',
                    transform=self.ax.transAxes,
                    color='red',
                    fontsize=200)
        self.canvas.draw()