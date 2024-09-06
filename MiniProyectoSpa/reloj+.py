class ClockStopwatchApp:  
        def __init__(self, root):  
            self.root = root  
            self.root.title("Reloj y Cronómetro")  
            self.running = False  
            self.start_time = None  
            self.elapsed_time = timedelta(0)  

            self.clock_label = tk.Label(root, text="", font=("Helvetica", 48))  
            self.clock_label.pack()  

            self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))  
            self.stopwatch_label.pack()  

            self.start_button = tk.Button(root, text="Iniciar Cronómetro", command=self.start)  
            self.start_button.pack()  

            self.stop_button = tk.Button(root, text="Detener Cronómetro", command=self.stop)  
            self.stop_button.pack()  

            self.reset_button = tk.Button(root, text="Reiniciar Cronómetro", command=self.reset)  
            self.reset_button.pack()  

            self.update_clock()  

        def start(self):  
            if not self.running:  
                self.start_time = datetime.now() + timedelta(minutes=5)  
    # Sumar 5 minutos de preparación  
                self.running = True  
                self.update_stopwatch()  
    
        def stop(self):  
            self.running = False  

        def reset(self):  
            self.running = False  
            self.elapsed_time = timedelta(0)  
            self.stopwatch_label.config(text="00:00:00")  

        def update_stopwatch(self):  
            if self.running:  
                current_time = datetime.now()  
                total_time = self.start_time + self.elapsed_time  
                self.stopwatch_label.config(text=total_time.strftime("%H:%M:%S"))  
                self.root.after(1000, self.update_stopwatch)  

        def update_clock(self):  
            now = datetime.now()  
            self.clock_label.config(text=now.strftime("%H:%M:%S"))  
            self.root.after(1000, self.update_clock)  

if __name__ == "__main__":  
        root = tk.Tk()  
        app = ClockStopwatchApp(root)  
        root.mainloop()  
#Codigo de Noemi
