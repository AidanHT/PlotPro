class Config:
    COLORS = {
        'bg': '#f0f2f5',           # Light gray background
        'accent': '#2962ff',       # Blue accent
        'text': '#1a237e',         # Dark blue text
        'graph_bg': '#ffffff'      # White graph background
    }

    FUNCTION_BUTTONS = [
        ('x²', 'x^2'), ('x³', 'x^3'), 
        ('sin(x)', 'sin(x)'), ('cos(x)', 'cos(x)'), ('tan(x)', 'tan(x)'),
        ('eˣ', 'exp(x)'),
        ('|x|', 'abs(x)'), ('1/x', '1/x'), ('⌊x⌋', 'floor(x)')
    ]

    SUPPORTED_FUNCTIONS = ['sin', 'cos', 'tan', 'exp', 'abs', 'floor']