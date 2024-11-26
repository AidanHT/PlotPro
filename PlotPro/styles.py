from tkinter import ttk

def setup_styles(base_font_size, colors):
    style = ttk.Style()
    style.theme_use('clam')
    
    style.configure('Modern.TLabel',
                   font=('Segoe UI', base_font_size),
                   foreground=colors['text'])
    
    style.configure('Modern.TEntry',
                   font=('Segoe UI', base_font_size),
                   fieldbackground='white',
                   borderwidth=0)
    
    style.configure('Modern.TButton',
                   font=('Segoe UI', base_font_size),
                   background=colors['accent'],
                   foreground='white',
                   padding=(20, 10))