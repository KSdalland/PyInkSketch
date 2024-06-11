import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

class MouseTracker:
    def __init__(self):
        
        fig, ax = plt.subplots() 
        plt.xlim(0,1)
        plt.ylim(0,1) 
        fig.subplots_adjust(bottom=0.2)
        button_ax = plt.axes([0.8, 0.05, 0.1, 0.075]) 
        button = Button(button_ax, 'boooton')
        button.on_clicked(self.on_button_clicked)
        self.fig=fig
        self.ax = ax
        self.fig = ax.figure
        self.pressed = False
        self.reset_sketch()
        self.cidpress = self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.line=None
        self.button=button
        plt.show()
    
    def on_button_clicked(self, event):
        print("Button clicked!")
        for line in self.ax.lines:
            line.remove()
        for scatter in self.ax.collections:
            scatter.remove()
        self.reset_sketch()
        self.fig.canvas.draw()



  

    def reset_sketch(self):
        self.x = np.array([])
        self.y = np.array([])

   

    def on_press(self, event):
        if event.inaxes != self.ax:
            return
        if event.button == 1:  # Left mouse button
            self.pressed = True
            self.x=np.append(self.x,[event.xdata])
            self.y=np.append(self.y,[event.ydata])

        elif event.button == 3:
            self.ax.lines[-1].remove()
            self.fig.canvas.draw()

    def on_release(self, event):
        if event.inaxes != self.ax:
            return
        if event.button == 1:  # Left mouse button
            self.pressed = False
            self.do_stuff()
            self.reset_sketch()
 
    def do_stuff(self):
        self.line=self.ax.plot(self.x,self.y)
        self.fig.canvas.draw()

    def on_motion(self, event):
        if event.inaxes != self.ax:
            return
        if self.pressed:
            self.x=np.append(self.x,[event.xdata])
            self.y=np.append(self.y,[event.ydata])
            self.ax.scatter(self.x[-1],self.y[-1])
            self.fig.canvas.draw()
    
    


# fig, ax = plt.subplots()
# plt.xlim([0,1])
# plt.ylim([0,1])
# fig.subplots_adjust(bottom=0.2)
# # button_ax = plt.axes([0.8, 0.05, 0.1, 0.075]) 
# # button = Button(button_ax, 'boooton')
# tracker = MouseTracker(ax,fig,button)
# button.on_clicked(tracker.on_button_clicked)
# plt.show()

tracker = MouseTracker()
