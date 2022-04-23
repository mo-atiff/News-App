from PyQt5 import QtCore, QtGui, QtWidgets
import math as m
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet('background-color : black')
        MainWindow.resize(400, 428)   #332,428
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 71))
        self.label.setStyleSheet('QLabel {background-color: black; color: white;}')
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.cutbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('AC'))
        self.cutbut.setStyleSheet('QPushButton {background-color: black; color: orange;}')
        self.cutbut.setGeometry(QtCore.QRect(1, 80, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.cutbut.setFont(font)
        self.cutbut.setAutoFillBackground(True)
        self.cutbut.setObjectName("cutbut")
        self.singbut = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press('C'))
        self.singbut.setGeometry(QtCore.QRect(60, 80, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.singbut.setFont(font)
        self.singbut.setStyleSheet('QPushButton {background-color: black; color: orange;}')
        self.singbut.setAutoFillBackground(True)
        self.singbut.setObjectName("singbut")
        self.modbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('%'))
        self.modbut.setGeometry(QtCore.QRect(120, 80, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.modbut.setFont(font)
        self.modbut.setAutoFillBackground(True)
        self.modbut.setStyleSheet('QPushButton {background-color: black; color: orange;}')
        self.modbut.setObjectName("modbut")
        self.divbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('/'))
        self.divbut.setGeometry(QtCore.QRect(180, 80, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.divbut.setFont(font)
        self.divbut.setAutoFillBackground(True)
        self.divbut.setFlat(False)
        self.divbut.setObjectName("divbut")
        self.divbut.setStyleSheet('QPushButton {background-color: black; color: orange;}')
        
        
        self.sinbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('sin('))
        self.sinbut.setGeometry(QtCore.QRect(240, 80, 54, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.sinbut.setFont(font)
        self.sinbut.setAutoFillBackground(True)
        self.sinbut.setFlat(False)
        self.sinbut.setObjectName("sinbut")
        self.sinbut.setStyleSheet('QPushButton {background-color: black; color: grey;}')

        self.openbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('('))
        self.openbut.setGeometry(QtCore.QRect(300, 80, 54, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.openbut.setFont(font)
        self.openbut.setAutoFillBackground(True)
        self.openbut.setFlat(False)
        self.openbut.setObjectName("openbut")
        self.openbut.setStyleSheet('QPushButton {background-color: black; color: grey;}')



        self.num7but = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('7'))
        self.num7but.setGeometry(QtCore.QRect(0, 140, 51, 41))
        self.num7but.setAutoFillBackground(True)
        self.num7but.setFlat(False)
        self.num7but.setObjectName("num7but")
        self.num7but.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.num8but = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('8'))
        self.num8but.setGeometry(QtCore.QRect(60, 140, 51, 41))
        self.num8but.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.num8but.setWhatsThis("")
        self.num8but.setAutoFillBackground(True)
        self.num8but.setObjectName("num8but")
        self.num8but.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.num9but = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('9'))
        self.num9but.setGeometry(QtCore.QRect(120, 140, 51, 41))
        self.num9but.setAutoFillBackground(True)
        self.num9but.setAutoDefault(False)
        self.num9but.setDefault(False)
        self.num9but.setFlat(False)
        self.num9but.setObjectName("num9but")
        self.num9but.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.mulbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('*'))
        self.mulbut.setGeometry(QtCore.QRect(180, 140, 51, 41))
        self.mulbut.setAutoFillBackground(True)
        self.mulbut.setObjectName("mulbut")
        self.mulbut.setStyleSheet('QPushButton {background-color: black; color: orange;}')

        self.cosbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('cos('))
        self.cosbut.setGeometry(QtCore.QRect(240, 140, 56, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.cosbut.setFont(font)
        self.cosbut.setAutoFillBackground(True)
        self.cosbut.setFlat(False)
        self.cosbut.setObjectName("cosbut")
        self.cosbut.setStyleSheet('QPushButton {background-color: black; color: grey;}')

        self.closebut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press(')'))
        self.closebut.setGeometry(QtCore.QRect(300, 140, 56, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.closebut.setFont(font)
        self.closebut.setAutoFillBackground(True)
        self.closebut.setFlat(False)
        self.closebut.setObjectName("closebut")
        self.closebut.setStyleSheet('QPushButton {background-color: black; color: grey;}')


        self.num4but = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('4'))
        self.num4but.setGeometry(QtCore.QRect(0, 200, 51, 41))
        self.num4but.setAutoFillBackground(True)
        self.num4but.setObjectName("num4but")
        self.num4but.setStyleSheet('QPushButton {background-color: black; color: white;}')

        self.num5but = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('5'))
        self.num5but.setGeometry(QtCore.QRect(60, 200, 51, 41))
        self.num5but.setAutoFillBackground(True)
        self.num5but.setObjectName("num5but")
        self.num5but.setStyleSheet('QPushButton {background-color: black; color: white;}')

        self.num6but = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('6'))
        self.num6but.setGeometry(QtCore.QRect(120, 200, 51, 41))
        self.num6but.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.num6but.setAutoFillBackground(True)
        self.num6but.setObjectName("num6but")
        self.num6but.setStyleSheet('QPushButton {background-color: black; color: white;}')

        self.minbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('-'))
        self.minbut.setGeometry(QtCore.QRect(180, 200, 51, 41))
        self.minbut.setAutoFillBackground(True)
        self.minbut.setObjectName("minbut")
        self.minbut.setStyleSheet('QPushButton {background-color: black; color: orange;}')

        self.tanbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('tan('))
        self.tanbut.setGeometry(QtCore.QRect(240, 200, 66, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tanbut.setFont(font)
        self.tanbut.setAutoFillBackground(True)
        self.tanbut.setFlat(False)
        self.tanbut.setObjectName("tanbut")
        self.tanbut.setStyleSheet('QPushButton {background-color: black; color: grey;}')

        self.pibut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('π'))
        self.pibut.setGeometry(QtCore.QRect(300, 200, 66, 41))
        self.pibut.setAutoFillBackground(True)
        self.pibut.setObjectName("pibut")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pibut.setFont(font)
        self.pibut.setFlat(False)
        self.pibut.setStyleSheet('QPushButton {background-color: black; color: grey;}')

        self.num1but = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('1'))
        self.num1but.setGeometry(QtCore.QRect(0, 260, 51, 41))
        self.num1but.setAutoFillBackground(True)
        self.num1but.setObjectName("num1but")
        self.num1but.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.num2but = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('2'))
        self.num2but.setGeometry(QtCore.QRect(60, 260, 51, 41))
        self.num2but.setAutoFillBackground(True)
        self.num2but.setObjectName("num2but")
        self.num2but.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.num3but = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('3'))
        self.num3but.setGeometry(QtCore.QRect(120, 260, 51, 41))
        self.num3but.setAutoFillBackground(True)
        self.num3but.setObjectName("num3but")
        self.num3but.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.addbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('+'))
        self.addbut.setGeometry(QtCore.QRect(180, 260, 51, 41))
        self.addbut.setAutoFillBackground(True)
        self.addbut.setObjectName("addbut")
        self.addbut.setStyleSheet('QPushButton {background-color: black; color: orange;}')

        self.logbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('log('))
        self.logbut.setGeometry(QtCore.QRect(240, 260, 64, 41))
        self.logbut.setAutoFillBackground(True)
        self.logbut.setObjectName("logbut")
        font.setBold(True)
        font.setWeight(75)
        self.logbut.setFont(font)
        self.logbut.setFlat(False)
        self.logbut.setStyleSheet('QPushButton {background-color: black; color: grey;}')

        self.ebut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('e'))
        self.ebut.setGeometry(QtCore.QRect(300, 260, 64, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ebut.setFont(font)
        self.ebut.setAutoFillBackground(True)
        self.ebut.setFlat(False)
        self.ebut.setObjectName("ebut")
        self.ebut.setStyleSheet('QPushButton {background-color: black; color: grey;}')

        self.byebut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('BYE'))
        self.byebut.setGeometry(QtCore.QRect(0, 320, 61, 41))
        self.byebut.setAutoFillBackground(True)
        self.byebut.setObjectName("byebut")
        self.byebut.setStyleSheet('QPushButton {background-color: black; color: red;}')
        self.num0but = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('0'))
        self.num0but.setGeometry(QtCore.QRect(60, 320, 51, 41))
        self.num0but.setAutoFillBackground(True)
        self.num0but.setObjectName("num0but")
        self.num0but.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.dotbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('.'))
        self.dotbut.setGeometry(QtCore.QRect(120, 320, 51, 41))
        self.dotbut.setAutoFillBackground(True)
        self.dotbut.setObjectName("dotbut")
        self.dotbut.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.eqbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('='))   
        self.eqbut.setGeometry(QtCore.QRect(180, 320, 51, 41))    
        self.eqbut.setAutoFillBackground(True)
        self.eqbut.setObjectName("eqbut")
        self.eqbut.setStyleSheet('QPushButton {background-color: orange; color: white;}')
        self.rootbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press('√'))
        self.rootbut.setGeometry(QtCore.QRect(240, 320, 51, 41))
        self.rootbut.setAutoFillBackground(True)
        self.rootbut.setObjectName("rootbut")
        self.rootbut.setStyleSheet('QPushButton {background-color: black; color: grey;}')

        MainWindow.setCentralWidget(self.centralwidget)
        self.hhhkkj = QtWidgets.QMenuBar(MainWindow)
        self.hhhkkj.setGeometry(QtCore.QRect(0, 0, 232, 33))
        self.hhhkkj.setAutoFillBackground(True)
        self.hhhkkj.setNativeMenuBar(True)
        self.hhhkkj.setObjectName("hhhkkj")
        MainWindow.setMenuBar(self.hhhkkj)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def press(self,sign):
        if sign == 'AC':
            self.label.setText('')
            

        elif sign == 'C':
            if len(self.label.text()) == 0:
                pass
            else:
                current = self.label.text()
                currentrev = current[::-1]
                lst = list(currentrev)
                lst.pop(0)
                lst = lst[::-1]
                final = ''
                final = final.join(lst)
                self.label.setText(final)


        elif sign == 'BYE':
            exit()        

        else:                                                          
            
            if self.label.text() == '0':
                self.label.setText('')
            
            if sign!= '=':
                self.label.setText(self.label.text()+sign)
                                                                                                                                                                                
            if sign == '=':
                try : 
                    ToEval = self.label.text()
                    if (ToEval[-2:] == '/0') or (ToEval == '1/sin(0') or (ToEval == '1/cos(90') or (ToEval == '1/tan(0'):
                        self.label.setText('Zero Division Error')


                    else : 
                        evaluated = eval(ToEval)
                        evaluated = str(evaluated)
                        self.label.setText(evaluated)
                        print(evaluated)
                        


                except Exception:
                    try:
                        Sine = self.label.text() 
                        if sign == '=' and 'sin' in Sine and not '+'in Sine and not '-' in Sine and not '/' in Sine and not '*' in Sine:
                            print(Sine)
                            ektry = Sine.index('i')   
                            RadVal = Sine[ektry+3:] 

                            Rad = list(RadVal)
                            if ')' in Rad:
                                Rad.remove(')')
                                s = ''
                                RadNum = s.join(Rad)
                                RadNum = int(RadNum)

                                SineVal = m.sin(m.radians(RadNum))        #RadVal       
                                formatter = "{0:.10f}"
                                FSineVal = formatter.format(SineVal)
                        
                                                        
                                if FSineVal == '1.0000000000':
                                    self.label.setText('1')
                                elif FSineVal == '0.0000000000':
                                    self.label.setText('0')
                                elif FSineVal == '0.5000000000':
                                    self.label.setText('0.5')
                                elif FSineVal == '-1.0000000000':
                                    self.label.setText('-1')

                                else:
                                    self.label.setText(FSineVal)


                            else:

                                RadVal = int(RadVal) 
                                SineVal = m.sin(m.radians(RadVal))        #RadVal       
                                formatter = "{0:.10f}"
                                FSineVal = formatter.format(SineVal)
                        
                                                        
                                if FSineVal == '1.0000000000':
                                    self.label.setText('1')
                                elif FSineVal == '0.0000000000':
                                    self.label.setText('0')
                                elif FSineVal == '0.5000000000':
                                    self.label.setText('0.5')
                                elif FSineVal == '-1.0000000000':
                                    self.label.setText('-1')

                                else:
                                    self.label.setText(FSineVal)

                        elif sign == '=' and 'sin' in Sine and '+' or '-' or '/' or '*' in Sine :
                            print(self.label.text())                                                                            
                            print('Yay!!!...iam in sine')
                            nindex = self.label.text().index('i')  # .index('s')       
                            print(nindex)  #This is printing
                            nindexp = nindex+2 #+3                          
                            print(self.label.text()[nindexp])

                            try:
                                self.label.text()[nindexp] == '('
                                print('yes...it is fine...iam in sine')
                                compsinindex = nindexp + 1
                                print('ssss', compsinindex)
                                compsinval = self.label.text()[compsinindex:]
                                print('Saarreee', compsinval)

                                radcompsinval = list(compsinval)
                                if ')' in radcompsinval:
                                    radcompsinval.remove(')')
                                    s1 = ''
                                    rads = s1.join(radcompsinval)
                                    rads = int(rads)


                                    print(compsinval)
                                    #compsincal = int(compsinval)  
                                    #print('here,,,',compsincal)
                                    compsincalval = m.sin(m.radians(rads))
                                    #print('dekh',compsincalval)
                                    compsincalval = str(compsincalval)
                                    #print('seedha dekh',compsincalval)
                                    print('Index : ',self.label.text()[nindex-2:])
                                    replacesinval = self.label.text().replace(self.label.text()[nindexp-3:],compsincalval)
                                    print('Replace', replacesinval)    # -sin(........
                                    peacesin = eval(replacesinval)
                                    print(peacesin,'kaiku')
                                    peacesin = str(peacesin)
                                    self.label.setText(peacesin)
                                    #print('mai aagaya')     tan came upto here it isnt going into exception block

                                else:
                                    print('yes...it is fine...iam in sine without closing')
                                    compsinindex = nindexp + 1
                                    compsinval = self.label.text()[compsinindex:]
                                                                                                

                                    print('ye wala truck', compsinval)
                                    compsincal = int(compsinval)
                                    print(compsincal)           # uncomment this
                                    #print('here,,,',compsincal)
                                    compsincalval = m.sin(m.radians(compsincal))      # compsincal
                                    #print('dekh',compsincalval)
                                    compsincalval = str(compsincalval)
                                    #print('seedha dekh',compsincalval)
                                    print('Index : ',self.label.text()[nindex-2:])
                                    replacesinval = self.label.text().replace(self.label.text()[nindexp-3:],compsincalval)
                                    print(replacesinval)    # -sin(........
                                    peacesin = eval(replacesinval)
                                    print(peacesin,'kaiku')
                                    peacesin = str(peacesin)
                                    self.label.setText(peacesin)
                            except Exception:
                                # exception_type, exception_object, exception_traceback = sys.exc_info()
                                pass

                    
                    except Exception:
                        try :
                            if sign == '=' and 'cos' in self.label.text() and not '+'in self.label.text() and not '-' in self.label.text() and not '/' in self.label.text() and not '*' in self.label.text():
                                ektry = self.label.text().index('o')
                                print('iam in cos')
                                print(ektry)   
                                RadVal = self.label.text()[ektry+3:] 
                                print(RadVal) 

                                #RadVal = int(RadVal) # Uncomment this
                                rad = list(RadVal)

                                if ')' in rad:
                                    rad.remove(')')
                                    s = ''
                                    RadNum = s.join(rad)
                                    RadNum = int(RadNum)

                                    CosVal = m.cos(m.radians(RadNum))        #RadVal       
                                    formatter = "{0:.10f}"
                                    FCosVal = formatter.format(CosVal)
                            
                                                            
                                    if FCosVal == '1.0000000000':
                                        self.label.setText('1')
                                    elif FCosVal == '0.0000000000':
                                        self.label.setText('0')
                                    elif FCosVal == '0.5000000000':
                                        self.label.setText('0.5')
                                    elif FCosVal == '-1.0000000000':
                                        self.label.setText('-1')

                                    else:
                                        self.label.setText(FCosVal)


                                else:

                                    RadVal = int(RadVal) 
                                    CosVal = m.cos(m.radians(RadVal))        #RadVal       
                                    formatter = "{0:.10f}"
                                    FCosVal = formatter.format(CosVal)
                            
                                                            
                                    if FCosVal == '1.0000000000':
                                        self.label.setText('1')
                                    elif FCosVal == '0.0000000000':
                                        self.label.setText('0')
                                    elif FCosVal == '0.5000000000':
                                        self.label.setText('0.5')
                                    elif FCosVal == '-1.0000000000':
                                        self.label.setText('-1')

                                    else:
                                        self.label.setText(FCosVal)


                            elif sign == '=' and 'cos' in self.label.text() and '+' or '-' or '/' or '*' in self.label.text() :

                                print(self.label.text())                                                                            
                                print('Yay!!!...iam in cos')
                                nindex = self.label.text().index('s')        
                                print(nindex)  #This is printing
                                nindexp = nindex+1 #+3                          
                                print(self.label.text()[nindexp])

                                try:
                                    self.label.text()[nindexp] == '('
                                    print('yes...it is fine...iam in cos')
                                    compcosindex = nindexp + 1
                                    compcosval = self.label.text()[compcosindex:]

                                    radcompcosval = list(compcosval)
                                    if ')' in radcompcosval:
                                        radcompcosval.remove(')')
                                        s1 = ''
                                        rads = s1.join(radcompcosval)
                                        rads = int(rads)


                                        print(compcosval)
                                        #compsincal = int(compsinval)          
                                        #print('here,,,',compsincal)
                                        compcoscalval = m.cos(m.radians(rads))      # compsincal
                                        #print('dekh',compsincalval)
                                        compcoscalval = str(compcoscalval)
                                        #print('seedha dekh',compsincalval)
                                        print('Index : ',self.label.text()[nindex-2:])
                                        replacecosval = self.label.text().replace(self.label.text()[nindexp-3:],compcoscalval)
                                        print(replacecosval)    # -sin(........
                                        peacecos = eval(replacecosval)
                                        print(peacecos,'kaiku')
                                        peacecos = str(peacecos)
                                        self.label.setText(peacecos)
                                        #print('mai aagaya')     tan came upto here it isnt going into exception block

                                    else:
                                        print('yes...it is fine...iam in sine without closing')
                                        compcosindex = nindexp + 1
                                        compcosval = self.label.text()[compcosindex:]
                                                                                                    

                                        print('ye wala truck', compcosval)
                                        compcoscal = int(compcosval)
                                        print(compcoscal)           # uncomment this
                                        #print('here,,,',compsincal)
                                        compcoscalval = m.cos(m.radians(compcoscal))      # compsincal
                                        #print('dekh',compsincalval)
                                        compcoscalval = str(compcoscalval)
                                        #print('seedha dekh',compsincalval)
                                        print('Index : ',self.label.text()[nindex-2:])
                                        replacecosval = self.label.text().replace(self.label.text()[nindexp-3:],compcoscalval)
                                        print(replacecosval)    # -sin(........
                                        peacecos = eval(replacecosval)
                                        print(peacecos,'kaiku')
                                        peacecos = str(peacecos)
                                        self.label.setText(peacecos)
                                except Exception:
                                    # exception_type, exception_object, exception_traceback = sys.exc_info()
                                    pass

                                
                
                        except Exception:
                            try:
                                print('hiii')
                                #Tann = self.label.text()
                                print('hiiooiioo')
                                if sign == '=' and 'tan' in self.label.text() and not '+'in self.label.text() and not '-' in self.label.text() and not '/' in self.label.text() and not '*' in self.label.text():
                                    ektry = self.label.text().index('a')
                                    print('iam in tan')
                                    print(ektry)   
                                    RadVal = self.label.text()[ektry+3:] 
                                    print(RadVal) 

                                    #RadVal = int(RadVal) # Uncomment this
                                    rad = list(RadVal)

                                    if ')' in rad:
                                        rad.remove(')')
                                        s = ''
                                        RadNum = s.join(rad)
                                        RadNum = int(RadNum)

                                        TanVal = m.tan(m.radians(RadNum))        #RadVal       
                                        formatter = "{0:.10f}"
                                        FTanVal = formatter.format(TanVal)
                                
                                                                
                                        if FTanVal == '1.0000000000':
                                            self.label.setText('1')
                                        elif FTanVal == '0.0000000000':
                                            self.label.setText('0')
                                        elif FTanVal == '0.5000000000':
                                            self.label.setText('0.5')
                                        elif FTanVal == '-1.0000000000':
                                            self.label.setText('-1')

                                        else:
                                            self.label.setText(FTanVal)


                                    else:

                                        RadVal = int(RadVal) 
                                        TanVal = m.tan(m.radians(RadVal))        #RadVal       
                                        formatter = "{0:.10f}"
                                        FTanVal = formatter.format(TanVal)
                                
                                                                
                                        if FTanVal == '1.0000000000':
                                            self.label.setText('1')
                                        elif FTanVal == '0.0000000000':
                                            self.label.setText('0')
                                        elif FTanVal == '0.5000000000':
                                            self.label.setText('0.5')
                                        elif FTanVal == '-1.0000000000':
                                            self.label.setText('-1')

                                        else:
                                            self.label.setText(FTanVal)
                                            
                                        
                                elif sign == '=' and 'tan' in self.label.text() and '+' or '-' or '/' or '*' in self.label.text() :

                                    print(self.label.text())                                                                            
                                    print('Yay!!!...iam in tan')
                                    try:
                                        nindex = self.label.text().index('n')  # .index('s')       
                                        print(nindex)  #This is printing
                                        nindexp = nindex+1 #+3                          
                                        print(self.label.text()[nindexp])

                                    except Exception:
                                        pass

                                    try:
                                        self.label.text()[nindexp] == '('
                                        print('yes...it is fine...iam in tan')
                                        comptanindex = nindexp + 1
                                        comptanval = self.label.text()[comptanindex:]

                                        radcomptanval = list(comptanval)
                                        if ')' in radcomptanval:
                                            radcomptanval.remove(')')
                                            s1 = ''
                                            rads = s1.join(radcomptanval)
                                            rads = int(rads)


                                            print(comptanval)
                                            #compsincal = int(compsinval)           # uncomment this
                                            #print('here,,,',compsincal)
                                            comptancalval = m.tan(m.radians(rads))      # compsincal
                                            #print('dekh',compsincalval)
                                            comptancalval = str(comptancalval)
                                            #print('seedha dekh',compsincalval)
                                            print('Index : ',self.label.text()[nindex-2:])
                                            replacetanval = self.label.text().replace(self.label.text()[nindexp-3:],comptancalval)
                                            print(replacetanval)    # -sin(........
                                            peacetan = eval(replacetanval)
                                            print(peacetan,'kaiku')
                                            peacetan = str(peacetan)
                                            self.label.setText(peacetan)

                                            #print('mai aagaya')     tan came upto here it isnt going into exception block

                                        else:
                                            print('yes...it is fine...iam in sine without closing')
                                            comptanindex = nindexp + 1
                                            comptanval = self.label.text()[comptanindex:]
                                                                                                        

                                            print('ye wala truck', comptanval)
                                            comptancal = int(comptanval)
                                            print(comptancal)           # uncomment this
                                            #print('here,,,',compsincal)
                                            comptancalval = m.tan(m.radians(comptancal))      # compsincal
                                            #print('dekh',compsincalval)
                                            comptancalval = str(comptancalval)
                                            #print('seedha dekh',compsincalval)
                                            print('Index : ',self.label.text()[nindex-2:])
                                            replacetanval = self.label.text().replace(self.label.text()[nindexp-3:],comptancalval)
                                            print(replacetanval)    # -sin(........
                                            peacetan = eval(replacetanval)
                                            print(peacetan,'kaiku')
                                            peacetan = str(peacetan)
                                            self.label.setText(peacetan)                
                                    
                                    except Exception:
                                        print('hao')
                                        if sign == '=' and 'log' in self.label.text():
                                            print('iam in log')
                                            ektry = self.label.text().index('(')
                                            LogVal = self.label.text()[ektry+1:]
                                            LogVal = int(LogVal)
                                            try :
                                                if not '+'in self.label.text() and not '-' in self.label.text() and not '/' in self.label.text() and not '*' in self.label.text():
                                                    LogCal = m.log10(LogVal)
                                                    formatter = "{0:.10f}"
                                                    FLogVal = formatter.format(LogCal)
                                                    FLogVal = str(FLogVal)
                                                    print(FLogVal)
                                                    
                                                
                                                    print(self.label.text()[4:])
                                                    if FLogVal == '0.0000000000':
                                                        self.label.setText('0')

                                                    elif '.0000000000' in FLogVal:
                                                        gud = FLogVal.split('.')
                                                        if gud[1] == '0000000000':
                                                            self.label.setText(gud[0])

                                                        
                                                    elif self.label.text()[4] == '0':
                                                        self.label.setText('Error')

                                                    else:
                                                        self.label.setText(FLogVal)

                                                elif 'log' in self.label.text() and '+' or '-' or '/' or '*' in self.label.text():
                                                    print('Yay!!!...iam in log')
                                                    nnindex = self.label.text().index('g')
                                                    print(nnindex)
                                                    nindexp = nnindex+1
                                                    print(self.label.text()[nindexp])

                                                    if self.label.text()[nindexp] == '(':
                                                        print('yes...it is fine...')
                                                        complogindex = nindexp + 1
                                                        complogval = self.label.text()[complogindex:]
                                                        print(complogval)
                                                        complogcal = int(complogval)
                                                        complogcalval = m.log10(complogcal)
                                                        complogcalval = str(complogcalval)
                                                        replacelogval = self.label.text().replace(self.label.text()[nnindex-2:],complogcalval)
                                                        print(replacelogval)
                                                        peacelog = eval(replacelogval)
                                                        print(peacelog)
                                                        peacelog = str(peacelog)
                                                        self.label.setText(peacelog)


                                            except Exception:
                                                self.label.setText('Error')



                                        if sign == '=' and '√' in self.label.text():
                                            try:
                                                if '√' in self.label.text() and '+' or '-' or '/' or '*' in self.label.text():
                                                    print('Bosss')  #came 
                                                    print(self.label.text())
                                                    rootindexu = self.label.text().index('√')
                                                    print('Index of Root')
                                                    rootval = self.label.text()[rootindexu+1:]
                                                    print('After Root',rootval)
                                                    rootval = int(rootval)
                                                    rootcalval = m.sqrt(rootval)
                                                    print('Root : ',rootcalval)
                                                    rootcalval = str(rootcalval)
                                                    replacerootval = self.label.text().replace(self.label.text()[rootindexu:],rootcalval)
                                                    print('ituuu')  #came
                                                    print(replacerootval)
                                                    evalroot = eval(replacerootval)
                                                    print('Eval : ',evalroot)
                                                    evalroot = str(evalroot)
                                                    self.label.setText(evalroot)

                                                

                                            except Exception:
                                                self.label.setText('Errorr')

                                        if sign == '=' and 'π' in self.label.text() and not 'e' in self.label.text():
                                            try:
                                                if 'π' in self.label.text() and '+' or '-' or '/' or '*' in self.label.text():
                                                    print('Bosssssssssssssssssssss') 
                                                    print(self.label.text())
                                                    #indexofpi = self.label.text().index('π')
                                                    mathpi = m.pi
                                                    mathpi = str(mathpi)
                                                    l = self.label.text().replace('π', mathpi)
                                                    print(l)
                                                    evalpi = eval(l)
                                                    evalpi = str(evalpi)
                                                    if len(self.label.text()) > 15:
                                                        F = "{0:.15f}"
                                                        FPiVal = F.format(evalpi)
                                                        self.label.setText(FPiVal)
                                                    else:
                                                        self.label.setText(evalpi)

                                                

                                            except Exception:
                                                self.label.setText('Error')


                                        if sign == '=' and 'e' in self.label.text() and not 'π' in self.label.text():
                                            try:
                                                if 'e' in self.label.text() and '+' or '-' or '/' or '*' in self.label.text():
                                                    print('Bovvvvvvvvvvvvvvvvvvvvvvvvvvv')
                                                    mathe = m.e
                                                    mathe = str(mathe)
                                                    le = self.label.text().replace('e', mathe)
                                                    print(le)
                                                    evale = eval(le)
                                                    evale = str(evale)
                                                    if len(self.label.text()) > 15:
                                                        Fe = "{0:.15f}"
                                                        FEVal = Fe.format(evale)
                                                        self.label.setText(FEVal)
                                                    else:
                                                        self.label.setText(evale)

                                                

                                            except Exception:
                                                self.label.setText('Error')


                                        if sign == '=' and 'e' in self.label.text() and 'π' in self.label.text():
                                            try:
                                                if 'e' in self.label.text() and 'π' in self.label.text() and '+' or '-' or '/' or '*' in self.label.text():
                                                    print('Beepppiii')
                                                    mathep = m.e
                                                    mathpi_e = m.pi
                                                    mathep = str(mathep)
                                                    mathpi_e = str(mathpi_e)
                                                    #lee = self.label.text().replace('e', mathep)
                                                    lpi_e = self.label.text().replace('π', mathpi_e).replace('e', mathep)
                                                    #print(lee)
                                                    print(lpi_e)
                                                    evalep = eval(lpi_e)
                                                    print(evalep)
                                                    evalep = str(evalep)
                                                    if len(self.label.text()) > 15:
                                                        Fe = "{0:.15f}"
                                                        FEVal = Fe.format(evalep)
                                                        self.label.setText(FEVal)
                                                    else:
                                                        self.label.setText(evalep)

                                                

                                            except Exception:
                                                self.label.setText('Error')
                                                #print(e)                                      


                            except Exception:
                                try:
                                    #Logg = self.label.text()
                                    '''if sign == '=' and 'log' in self.label.text():
                                        print('iam in log')
                                        ektry = self.label.text().index('(')
                                        LogVal = self.label.text()[ektry+1:]
                                        LogVal = int(LogVal)
                                        try :
                                            LogCal = m.log10(LogVal)
                                            formatter = "{0:.10f}"
                                            FLogVal = formatter.format(LogCal)
                                            FLogVal = str(FLogVal)
                                            print(FLogVal)
                                            
                                        
                                            print(self.label.text()[4:])
                                            if FLogVal == '0.0000000000':
                                                self.label.setText('0')

                                                
                                            elif self.label.text()[4] == '0':
                                                self.label.setText('Error') 

                                            else:
                                                self.label.setText(FLogVal)

                                        except Exception:
                                            self.label.setText('Error')'''
                                    
                                    

                                except Exception:
                                    #Root = self.label.text()
                                    #Logg = self.label.text()
                                    '''if sign == '=' and '√' in self.label.text():
                                        print('iam in root')      
                                        var = self.label.text()[1:]
                                        var = int(var)
                                        try :
                                            sqrtcal = m.sqrt(var)
                                            sqrtcal = str(sqrtcal)
                                            sqrtcal = sqrtcal.strip('.0')
                                            print(sqrtcal)
                                            self.label.setText(sqrtcal)
                                            if '.' in self.label.text() and len(self.label.text())>10:
                                                now = self.label.text().split('.')
                                                if len(now[1]) > 8:
                                                    slicednow = now[1][:9]
                                                    first = now[0]+'.'
                                                    bettercal = first+slicednow
                                                    self.label.setText(bettercal) 

                                        except Exception:
                                            self.label.setText('Error')'''                            
                                                   
                
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.cutbut.setText(_translate("MainWindow", "AC"))
        self.singbut.setText(_translate("MainWindow", "C"))
        self.modbut.setText(_translate("MainWindow", "%"))
        self.divbut.setText(_translate("MainWindow", "/"))
        self.sinbut.setText(_translate("MainWindow", "sin"))
        self.openbut.setText(_translate("MainWindow", "("))
        self.num7but.setText(_translate("MainWindow", "7"))
        self.num8but.setText(_translate("MainWindow", "8"))
        self.num9but.setText(_translate("MainWindow", "9")) 
        self.mulbut.setText(_translate("MainWindow", "*"))
        self.cosbut.setText(_translate("MainWindow", "cos"))
        self.closebut.setText(_translate("MainWindow", ")"))
        self.num4but.setText(_translate("MainWindow", "4"))
        self.num5but.setText(_translate("MainWindow", "5"))
        self.num6but.setText(_translate("MainWindow", "6"))
        self.minbut.setText(_translate("MainWindow", "-"))
        self.tanbut.setText(_translate("MainWindow", "tan"))
        self.pibut.setText(_translate("MainWindow", "π"))
        self.num1but.setText(_translate("MainWindow", "1"))
        self.num2but.setText(_translate("MainWindow", "2"))
        self.num3but.setText(_translate("MainWindow", "3"))
        self.addbut.setText(_translate("MainWindow", "+"))
        self.logbut.setText(_translate("MainWindow", "log"))
        self.ebut.setText(_translate("MainWindow", "e"))
        self.byebut.setText(_translate("MainWindow", "BYE"))
        self.num0but.setText(_translate("MainWindow", "0"))
        self.dotbut.setText(_translate("MainWindow", "."))
        self.eqbut.setText(_translate("MainWindow", "="))
        self.rootbut.setText(_translate("MainWindow", "√"))


   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())