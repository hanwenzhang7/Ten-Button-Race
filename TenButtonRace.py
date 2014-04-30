import wx
import time
import random


class BtnRaceFrame(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY,"The Fabulous Ten Button Race",size = (1000,800))
		self.panel = wx.Panel(self)
		self.heading = wx.StaticText(self.panel, label="Let's Click Some Buttons. Press \"start\"to start!", pos=(10,5))
		self.btnStart = wx.Button(self.panel, label="Start", pos = (20,20))
		self.btnStart.Bind(wx.EVT_BUTTON, self.onStart)
	
		
	def onStart(self,e):
		self.btnStart.Show(False)
		self.startTime = time.time()
		self.btnClickMe = wx.Button(self.panel, label="Click Me", pos = (50,50))
		self.btnClickMe.Bind(wx.EVT_BUTTON, self.onClickMe)
		self.buttons = [self.btnClickMe]
		label = ["Me Too", "and me fool!", "can you catch me:)","you can't catch me!","HaHa!!!"]
		for i in range (9):
			x = random.randint(1,500)
			y = random.randint(1,500)
			i = random.randint(0,4)
			self.btnMeToo = wx.Button(self.panel, label=label[i], pos = (x,y))
			self.buttons.append(self.btnMeToo)
			self.btnMeToo.Show(False)
			self.btnMeToo.Bind(wx.EVT_BUTTON, self.onMeToo)
		self.i = 0
	def onClickMe(self,e):
		self.btnClickMe.Show(False)
		self.buttons[1].Show(True)
			
	def onMeToo(self,e):
		self.i += 1
		self.buttons[self.i].Show(False)
		if self.i == 9:
			self.finishtime = time.time()
			self.time = self.finishtime - self.startTime
			self.heading = wx.StaticText(self.panel, label="Your finished the race in %d seconds" %(self.time), pos=(500,500)) 
		else:
			self.buttons[self.i + 1].Show(True)
		
		
				
#-------------------------------------Main Program--------------------------------------------------------------------------------------	
raceApp = wx.App(False)
frame = BtnRaceFrame(None)
frame.Show()
raceApp.MainLoop()

