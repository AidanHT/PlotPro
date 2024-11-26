import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from config import Config
from styles import setup_styles
from graph_plotter import GraphPlotter

class GraphingCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("PlotPro")
        self.root.state('zoomed')
        
        self.colors = Config.COLORS
        self._setup_root()
        self._create_main_frame()
        self._setup_styles()
        self._create_ui_elements()
        self._setup_matplotlib()

    def _setup_root(self):
        self.root.configure(bg=self.colors['bg'])
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def _create_main_frame(self):
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(3, weight=1)

    def _setup_styles(self):
        screen_width = self.root.winfo_screenwidth()
        self.base_font_size = int(screen_width / 100)
        setup_styles(self.base_font_size, self.colors)

    def _create_ui_elements(self):
        self._create_header_frame()
        self._create_function_buttons()
        self._create_range_frame()
        self._create_plot_button()

    def _create_header_frame(self):
        header_frame = ttk.Frame(self.main_frame)
        header_frame.grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="ew")
        
        ttk.Label(header_frame, text="f(x) = ", style='Modern.TLabel').pack(side='left', padx=(0, 10))
        
        self.function_entry = ttk.Entry(header_frame, width=40, font=('Segoe UI', self.base_font_size))
        self.function_entry.pack(side='left', fill='x', expand=True)
        self.function_entry.insert(0, " ")
        
        self.clear_button = ttk.Button(header_frame, text="Clear", 
                                     style='Modern.TButton', command=self.clear_function)
        self.clear_button.pack(side='left', padx=(10, 0))

    def _create_function_buttons(self):
        func_frame = ttk.Frame(self.main_frame)
        func_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky="ew")
        
        for i, (btn_text, func) in enumerate(Config.FUNCTION_BUTTONS):
            btn = ttk.Button(func_frame, text=btn_text, style='Modern.TButton',
                           command=lambda f=func: self.insert_function(f))
            row = i // 5
            col = i % 5
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            
        for i in range(5):
            func_frame.grid_columnconfigure(i, weight=1)

    def _create_range_frame(self):
        range_frame = ttk.Frame(self.main_frame)
        range_frame.grid(row=2, column=0, columnspan=3, pady=20, sticky="ew")
        
        ttk.Label(range_frame, text="X Range:", style='Modern.TLabel').pack(side='left', padx=(0, 10))
        
        self.x_min = ttk.Entry(range_frame, width=10, font=('Segoe UI', self.base_font_size))
        self.x_min.pack(side='left', padx=5)
        self.x_min.insert(0, "-10")
        
        ttk.Label(range_frame, text="to", style='Modern.TLabel').pack(side='left', padx=10)
        
        self.x_max = ttk.Entry(range_frame, width=10, font=('Segoe UI', self.base_font_size))
        self.x_max.pack(side='left', padx=5)
        self.x_max.insert(0, "10")

    def _create_plot_button(self):
        self.plot_button = ttk.Button(self.main_frame, text="Plot Function", 
                                    command=self.plot_function, style='Modern.TButton')
        self.plot_button.grid(row=3, column=0, columnspan=3, pady=20)

    def _setup_matplotlib(self):
        plt.style.use('bmh')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        fig_width = screen_width / 100
        fig_height = screen_height / 100
        
        self.figure, self.ax = plt.subplots(figsize=(fig_width, fig_height))
        self.figure.patch.set_facecolor(self.colors['graph_bg'])
        self.ax.set_facecolor(self.colors['graph_bg'])
        self.ax.tick_params(axis='both', which='major', 
                           labelsize=self.base_font_size, colors=self.colors['text'])
        
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.main_frame)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_rowconfigure(4, weight=1)
        
        self.plotter = GraphPlotter(self.figure, self.ax, self.canvas, self.colors)

    def insert_function(self, func_str):
        current_pos = self.function_entry.index(tk.INSERT)
        self.function_entry.insert(current_pos, func_str)

    def plot_function(self):
        try:
            x_min = float(self.x_min.get())
            x_max = float(self.x_max.get())
            func_str = self.function_entry.get()
            self.plotter.plot(func_str, x_min, x_max)
        except ValueError:
            self.plotter._draw_error()

    def clear_function(self):
        self.function_entry.delete(0, tk.END)
        self.function_entry.insert(0, " ")