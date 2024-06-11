import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

class MouseTracker:
    def __init__(self):

        # Figure stuff
        fig, ax = plt.subplots() 
        plt.xlim(0,1)
        plt.ylim(0,1) 
        self.fig = fig
        self.ax = ax
        
        # Button stuff
        fig.subplots_adjust(bottom=0.2)
        fig.subplots_adjust(left=0.2)
        booted_ax = plt.axes([0.8, 0.05, 0.1, 0.075]) 
        booted = Button(booted_ax, 'boooton')
        booted.on_clicked(self.booted)

        # Coordinate ledger
        self.reset_sketch()
        
        # Mouse tracking
        self.cidpress = self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.pressed = False
            
        plt.show()
        
    
    def booted(self,event):
        print("Booted")
        for line in self.ax.lines:
            line.remove()
        for scatter in self.ax.collections:
            scatter.remove()
        self.reset_sketch()
        self.fig.canvas.draw()

    def reset_sketch(self):
        self.x = []
        self.y = []
        self.dots=[]

    def on_press(self, event):
        if event.inaxes != self.ax:
            return
        if event.button == 1:  # Left mouse button
            if self.pressed==False:
                self.dots.append(1)
            self.pressed = True
            self.x.append([event.xdata])
            self.y.append([event.ydata])
            self.ax.scatter(self.x[-1],self.y[-1])
        elif event.button == 3:
            self.ax.lines[-1].remove()
            for _ in range(self.dots[-1]):
                self.ax.collections[-1].remove()
            del self.dots[-1],self.x[-1],self.y[-1]
            self.fig.canvas.draw()

    def on_release(self, event):
        if event.inaxes != self.ax:
            return
        if event.button == 1:  # Left mouse button
            self.pressed = False
            self.ax.plot(self.x,self.y)
            self.fig.canvas.draw()
    
    def on_motion(self, event):
        if event.inaxes != self.ax:
            return
        if self.pressed:
            self.x[-1].append(event.xdata)
            self.y[-1].append(event.ydata)
            self.ax.scatter(self.x[-1],self.y[-1])
            self.dots[-1]+=1
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
