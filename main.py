import matplotlib.pyplot as plt
plt.ion()
class DynamicUpdate():
    #Suppose we know the x range
    min_y = 0
    max_y = 45

    def on_launch(self):
        #Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[], 'o')
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        self.ax.set_autoscalex_on(True)
        self.ax.set_ylim(self.min_y, self.max_y)
        #Other stuff
        self.ax.grid()
        l1 = self.ax.axhline(38.5, color='red', ls='--')
        l1.set_label('Febre')
        

    def on_running(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    #Example
    def __call__(self):
        import numpy as np
        import time
        self.on_launch()
        xdata = []
        ydata = []
        x = 0
        while True:
            y = 35
            x = x + 1
            xdata.append(x)
            ydata.append(y)
            self.on_running(xdata, ydata)
            time.sleep(0.1)
        return xdata, ydata

d = DynamicUpdate()
d()
