import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk

# ✅ Datos actualizados según la imagen
labels_q1 = ['0 días', '1 día', '2 días', '3 días', '4 días', '5 días', 'Rara vez', 'Traigo mi almuerzo']
sizes_q1 = [3, 8, 12, 7, 2, 3, 2, 1]

ratings = [1, 2, 3, 4, 5]
counts_q2 = [4, 9, 11, 13, 1]
percentages_q2 = [f'{(count / 31) * 100:.1f}%' for count in counts_q2]

labels_q3 = ['Menos de 1 hora', 'Entre 1 y 2 horas', 'Más de 2 horas']
sizes_q3 = [6, 25, 3]

# 🔧 Gráfico de barras
def create_bar_chart():
    fig, ax = plt.subplots()
    bars = ax.bar(ratings, counts_q2, color='skyblue')
    ax.set_title("¿Qué tan bueno consideras el servicio? (1=mal, 5=excelente)")
    ax.set_xlabel("Calificación")
    ax.set_ylabel("Cantidad de estudiantes")
    for bar, count, pct in zip(bars, counts_q2, percentages_q2):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                f'{count} ({pct})', ha='center', va='bottom')
    return fig

# 🔧 Gráfico circular Q1
def create_pie_chart_q1():
    fig, ax = plt.subplots()
    explode = [0.05] * len(sizes_q1)
    ax.pie(sizes_q1, labels=labels_q1, autopct='%1.1f%%', startangle=90,
           explode=explode, labeldistance=1.1, pctdistance=0.8)
    ax.set_title("¿Cuántos días a la semana consumes en la cafetería?")
    return fig

# 🔧 Gráfico circular Q3
def create_pie_chart_q3():
    fig, ax = plt.subplots()
    explode = [0.05] * len(sizes_q3)
    ax.pie(sizes_q3, labels=labels_q3, autopct='%1.1f%%', startangle=90,
           explode=explode, labeldistance=1.1, pctdistance=0.8)
    ax.set_title("¿Cuánto tiempo te tardas en reclamar y consumir el almuerzo?")
    return fig

# 🖥️ Interfaz
class ChartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resultados Encuesta Cafetería")
        self.root.attributes("-fullscreen", True)  # Pantalla completa
        self.index = 0
        self.figures = [create_bar_chart, create_pie_chart_q1, create_pie_chart_q3]

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.show_chart()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.next_button = tk.Button(self.button_frame, text="Siguiente", command=self.next_chart)
        self.next_button.pack(side=tk.LEFT, padx=10)

        self.exit_button = tk.Button(self.button_frame, text="Salir", command=self.root.quit)
        self.exit_button.pack(side=tk.LEFT, padx=10)

    def show_chart(self):
        fig = self.figures[self.index]()
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame)
        self.canvas.draw()
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
        self.toolbar.update()
        self.toolbar.pack()

    def next_chart(self):
        self.canvas_widget.pack_forget()
        self.toolbar.pack_forget()
        self.index = (self.index + 1) % len(self.figures)
        self.show_chart()

# ▶️ Ejecutar la aplicación
root = tk.Tk()
app = ChartApp(root)
root.mainloop()
