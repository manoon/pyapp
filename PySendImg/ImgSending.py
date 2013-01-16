from PyQt4.QtGui import QIcon,QLabel,QPushButton,QMessageBox,QTextEdit,QApplication,QGridLayout,QWidget,QStatusBar
from PyQt4.QtCore import QTime,QTimer,SIGNAL,QDate
import os,sys,ftplib,time
class ImgSending(QWidget):
	def __init__(self,parent=None):
		super(ImgSending,self).__init__(parent)
		self.SetupUi()
		self.running=False
		self.connect(self.toggleButton,SIGNAL("clicked()"),self.StartWorking)
		self.connect(self.clearButton,SIGNAL("clicked()"),self.RemoveImg)
		self.setWindowTitle("ImgSending")
		self.setWindowIcon(QIcon('icons/web.png'))
	
	def SetupUi(self):
		toggleButton=QPushButton("Start!",self)
		clearButton=QPushButton("Clear!",self)
		statusBar=QStatusBar()
		self.statusBar=statusBar
		self.toggleButton=toggleButton
		self.clearButton=clearButton

		textEdit=QTextEdit()
		self.textEdit=textEdit

		self.date=QDate.currentDate()
		self.time=QTime.currentTime()
		statusText=self.time.toString("hh:mm:ss")
		statusText="Start up @ " +self.date.toString("yyyy-MM-dd")+" "+statusText
		self.statusBar.showMessage(statusText)
		
		grid=QGridLayout()
		grid.addWidget(textEdit,1,0)
		grid.addWidget(toggleButton,2,1)
		grid.addWidget(clearButton,2,2)
		grid.addWidget(statusBar,2,0)
		self.setLayout(grid)
		self.resize(500,500)
	def StartWorking(self):
		if not self.running:
			self.running=True
			secTimer=QTimer(self)
			secTimer.start(1000)
			self.secTimer=secTimer
			self.time=QTime.currentTime()
			self.textEdit.setText(self.time.toString("hh:mm:ss"))
			secTimer=QTimer(self)
			secTimer.start(3000)
			self.secTimer=secTimer
			self.connect(secTimer,SIGNAL("timeout()"),self.UpdateText)

			secTimerCls=QTimer(self)
			secTimerCls.start(180000)
			self.secTimerCls=secTimerCls
			self.connect(secTimerCls,SIGNAL("timeout()"),self.ClearText)


		else:
			self.running=False
			self.secTimer.stop()

	def ClearText(self):
		self.textEdit.setText("A new Page")

	def UpdateText(self):
		self.time=self.time.addSecs(+3)
		time=self.time
		ImgList=self.GetImgList("d:\\tmp\\pytest","jpg")
		if len(ImgList)==0:
			self.textEdit.append(self.time.toString("hh:mm:ss")+"-----No Images Need 2 Be Send")
		else:
			self.Send2Ftp(ImgList)
			self.textEdit.append(self.time.toString("hh:mm:ss")+"-----Images Sent Okay")
			self.RemoveLocal(ImgList)


	def GetImgList(self,dir,ext=None):
		ImgList=[]
		needExtFilter=(ext!=None)
		for root,dirs,files in os.walk(dir):
			for filespath in files:
				filepath=os.path.join(root,filespath)
				extension=os.path.splitext(filepath)[1][1:]
				if needExtFilter and extension in ext:
					ImgList.append(filepath)
				elif not needExtFilter:
					ImgList.append(filepath)
		return ImgList

	def Send2Ftp(self,imglist):
		    
		def list_contain( ls, item ):
			ret = True
			try:
				index = ls.index( item )
			except:
				ret = False
			return ret
		session=ftplib.FTP('127.0.0.1','user','pwd')
		curtime=time.localtime(time.time())
		curdate=time.strftime('%Y%m%d',curtime)
		remotedir="/img/"+curdate+"/"
		session.cwd("/img/")
		nlst = session.nlst()
		print session.nlst()
		
		if not list_contain(nlst, curdate):
			session.mkd(remotedir)
		session.cwd(remotedir)
		for img in imglist:
			file_handler=open(img,'rb')
			file_name=img.split('\\')[3]
			print file_name
			cmd="STOR %s"%(file_name)
			session.storbinary(cmd,file_handler)
			#print "we sending img..."
	def RemoveImg(self):
		ImgList=self.GetImgList("d:\\tmp\\pytest","jpg")
		self.RemoveLocal(ImgList)
		reply=QMessageBox.question(self,'Message',
				"All images had been removed!& Screen Is Cleared",QMessageBox.Yes)
	def RemoveLocal(self,imglist):
		for img in imglist:
			os.remove(img)
			#print "removed okay"
	
if __name__=="__main__":
	import sys
	app=QApplication(sys.argv)
	form=ImgSending()
	form.show()
	sys.exit(app.exec_())
