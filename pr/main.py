import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import pygame
from random import randint
import math


class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui',self)
        self.mode = {
            self.m_rad: 'rad',
            self.m_deg: 'deg'
        }
        pygame.init() 
        pygame.mixer.Sound('mo3\VlastKotorayaNeSnilasMoemuOtzu.wav').play()        
        self.run()
        
    def run(self):
        self.setWindowTitle('Warcraft Калькулятор')
        self.zv = ['mo3\OtLICHniyPlan.wav', 'mo3\Konechno.wav', 'mo3\Polegche.wav',
                   'mo3\Razumeetsya.wav', 'mo3\SvetDaetMneSil.wav', 'mo3\YaPozobotschusObEtom.wav',
                   r'mo3\NeNuzhnoKlanyatsya.wav', r'mo3\NuChtoEscho.wav']
        self.ravno_cl = [[], 0]
        self.viv_fl = False
        self.walpapers = ['war.jpg', 'war2.jpg', 'war3.jpg', 'war5.jpg']
        self.walp_cnt = 0
        oImage = QImage(self.walpapers[self.walp_cnt % 4])
        sImage = oImage.scaled(QSize(502,275))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)        
        self.y = None
        self.m_deg.setChecked(True)
        self.m = 'deg'
        self.x = 0
        self.k = [False, False]
        self.nnn = 0
        self.x2 = 0
        self.ur = []
        self.st_kor_func_fl = False
        self.mmm = 0
        self.mode2nd = False
        self.output.setDigitCount(len(str(self.x)))
        self.output.display(self.x)
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.m_rad)
        self.button_group.addButton(self.m_deg)
        self.button_group.buttonClicked.connect(self.mode_ch)
        self.one.clicked.connect(self.app)
        self.two.clicked.connect(self.app)
        self.three.clicked.connect(self.app)
        self.Mista_trigger.clicked.connect(self.app)
        self.five.clicked.connect(self.app)
        self.six.clicked.connect(self.app)
        self.seven.clicked.connect(self.app)
        self.eight.clicked.connect(self.app)
        self.nine.clicked.connect(self.app)
        self.nol.clicked.connect(self.app)
        self.koma.clicked.connect(self.chndg_k)
        self.plus.clicked.connect(self.funk_plus)
        self.minus_2.clicked.connect(self.funk_minus)
        self.delit.clicked.connect(self.devision)
        self.mult.clicked.connect(self.funk_mult)
        self.print.clicked.connect(self.f_ravno)
        self.openSK.clicked.connect(self.op_sk)
        self.closeSK.clicked.connect(self.cl_sk)
        self.mplus.clicked.connect(self.plusm)
        self.minus.clicked.connect(self.minusm)
        self.minsert.clicked.connect(self.m_mc)
        self.mdel.clicked.connect(self.delete_m)
        self.second.clicked.connect(self.chg_2nd)
        self.sbros_all.clicked.connect(self.ccc)
        self.sbros_str.clicked.connect(self.cece)
        self.plus_or_minus.clicked.connect(self.p_or_m)
        self.exp.clicked.connect(self.exp_func)
        self.ystepx.clicked.connect(self.st_kor_func)
        self.koren.clicked.connect(self.koren_f)
        self.ln.clicked.connect(self.ln_f)
        self.log.clicked.connect(self.log_f)
        self.quadrat.clicked.connect(self.quadrat_f)
        self.tab.clicked.connect(self.tab_f)
        self.sin.clicked.connect(self.sin_f)
        self.cos.clicked.connect(self.cos_f)
        self.tg.clicked.connect(self.tg_f)
        self.click.clicked.connect(self.chng_wal_func)
        
    def chng_wal_func(self):
        pygame.init() 
        pygame.mixer.Sound('mo3\TakTOLuchshe.wav').play()         
        self.walp_cnt += 1
        oImage = QImage(self.walpapers[self.walp_cnt % 4])
        sImage = oImage.scaled(QSize(502,275))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))    
        self.setPalette(palette)        
    def all_error(self):
        i, okBtnPressed = QInputDialog.getItem(
            self, 
            "Произошла ошибка",
            "Произошла ошибка. Отправить сообщение об ошибке разработчикам?",
            ("да", "нет"),
            0,
            False
        ) 
        if okBtnPressed:
            pygame.init() 
            pygame.mixer.Sound('mo3\OniPoluchatPoZaslugam.wav').play()
        else:
            pygame.init() 
            pygame.mixer.Sound('mo3\KtoEto.wav').play()            
        self.ccc()
        self.normal_2nd()
    def mode_ch(self, b):
        self.m = self.mode[b]
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []
    def chg_2nd(self):
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        if not self.mode2nd:
            self.mode2nd = True
            self.plus_or_minus.setText('x/y')
            self.quadrat.setText('1/X')
            self.koren.setText('³√')
            self.sin.setText('arcsin')
            self.cos.setText('arccos')
            self.tg.setText('arctg')
            self.log.setText('10ˣ')
            self.ln.setText('eˣ')
            self.ystepx.setText('ˣ√y')
            self.sbros_str.setText('n!')
        else:
            self.normal_2nd()
    def normal_2nd(self):
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        self.plus_or_minus.setText('+/-')
        self.quadrat.setText('x²')
        self.koren.setText('√')
        self.sin.setText('sin')
        self.cos.setText('cos')
        self.tg.setText('tg')
        self.log.setText('log')
        self.ln.setText('ln')
        self.ystepx.setText('yˣ')
        self.sbros_str.setText('CE')
        self.mode2nd = False
    def app(self):
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        try:
            if self.x == None:
                self.x = 0
            if self.k[0]:
                if self.k[1]:
                    self.k[1] = False
                    self.x = str(self.x)[:-1]
                self.x = float(str(self.x) + str(self.sender().text()))
            else:
                self.x = int(str(self.x) + str(self.sender().text()))
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x)
        except Exception:
            self.all_error()
        
    def chndg_k(self):
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        if not '.' in str(self.x):
            self.k = [True, True]
            self.x = float(self.x)
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x)
        
    def funk_plus(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()           
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        if not self.x == None:
            self.ur.append(self.x)
            self.ur.append('+')
        else:
            self.ur[-1] = '+'
        self.x = None
        self.k = [False, False]
        self.output.setDigitCount(len(str(self.x)))
        self.output.display(self.x)
        
    def funk_minus(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        if not self.x == None:
            self.ur.append(self.x)
            self.ur.append('-')
        else:
            self.ur[-1] = '-'
        self.x = None
        self.k = [False, False]
        self.output.setDigitCount(len(str(self.x)))
        self.output.display(self.x)                
                
    def funk_mult(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        if not self.x == None:
            self.ur.append(self.x)
            self.ur.append('*')
        else:
            self.ur[-1] = '*'  
        self.x = None
        self.k = [False, False]
        self.output.setDigitCount(len(str(self.x)))
        self.output.display(self.x)        
                
    def devision(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        if not self.x == None:
            self.ur.append(self.x)
            self.ur.append('/')
        else:
            self.ur[-1] = '/'  
        self.x = None
        self.k = [False, False]
        self.output.setDigitCount(len(str(self.x)))
        self.output.display(self.x)        
    
    def f_ravno(self):     
        try:
            if self.st_kor_func_fl:
                if self.mode2nd:
                    self.x = self.st_kor_func2 ** (1 / self.x)
                    self.st_kor_func_fl = False
                else:
                    self.x = self.st_kor_func2 ** self.x
                    self.st_kor_func_fl = False
            else:
                oskvernen = False
                if self.ravno_cl[0] == self.ur:
                    self.ravno_cl[1] += 1
                else:
                    self.ravno_cl[1] = 0
                if self.ravno_cl[1] >= 10:
                    oskvernen = True
                    pygame.init()                     
                    pygame.mixer.Sound(r'mo3\NeOkvernyaiMenyaKursorom.wav').play()    
                self.viv_fl = True
                if not oskvernen:
                    pygame.init() 
                    pygame.mixer.Sound('mo3\YaPozobotschusObEtom.wav').play()                    
                if self.ur != []:
                    if not str(self.ur[-1]).isdigit():
                        self.ur.append(self.x)
                n = 0
                while '*' in self.ur:
                    a = self.ur[self.ur.index('*') - 1]
                    b = self.ur[self.ur.index('*') + 1]
                    n = self.ur.index('*') - 1
                    if len(self.ur) != 3:
                        del self.ur[n : n + 3]
                        self.ur.insert(n, a * b)
                    else:
                        n += 1
                        self.ur.insert(n - 1, a*b)
                        self.ur.insert(n, ('*'))                       
                        self.ur.insert(n + 1, b)                        
                        del self.ur[n + 2 : n + 5]                        
                        break
                while '/' in self.ur:           
                    a = self.ur[self.ur.index('/') - 1]
                    b = self.ur[self.ur.index('/') + 1]
                    n = self.ur.index('/') - 1
                    if len(self.ur) != 3:
                        del self.ur[n : n + 3]
                        self.ur.insert(n, a / b)
                    else:
                        n += 1
                        self.ur.insert(n - 1, a / b)
                        self.ur.insert(n, ('/'))                       
                        self.ur.insert(n + 1, b)                        
                        del self.ur[n + 2 : n + 5]                        
                        break 
                while '+' in self.ur:
                    a = self.ur[self.ur.index('+') - 1]
                    b = self.ur[self.ur.index('+') + 1]
                    n = self.ur.index('+') - 1
                    if len(self.ur) != 3:
                        del self.ur[n : n + 3]
                        self.ur.insert(n, a + b)
                    else:
                        n += 1
                        self.ur.insert(n - 1, a + b)
                        self.ur.insert(n, ('+'))                       
                        self.ur.insert(n + 1, b)                        
                        del self.ur[n + 2 : n + 5]                        
                        break 
                while '-' in self.ur:
                    a = self.ur[self.ur.index('-') - 1]
                    b = self.ur[self.ur.index('-') + 1]
                    n = self.ur.index('-') - 1
                    if len(self.ur) != 3:
                        del self.ur[n : n + 3]
                        self.ur.insert(n, a - b)
                    else:
                        n += 1
                        self.ur.insert(n - 1, a - b)
                        self.ur.insert(n, ('-'))                       
                        self.ur.insert(n + 1, b)                        
                        del self.ur[n + 2 : n + 5]                        
                        break 
                self.x = self.ur[0]
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x)  
            self.ravno_cl[0] = self.ur
        except Exception:
            self.all_error()        
        
    def op_sk(self):
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        self.y = self.ur[:]
        self.ur = []
    
    def cl_sk(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        try:
            self.ur.append(self.x)
            if self.y != None:
                if not self.ur[-1].isdigit():
                    self.ur = self.ur[:-1]
                while '*' in self.ur:
                    a = self.ur[self.ur.index('*') - 1]
                    b = self.ur[self.ur.index('*') + 1]
                    n = self.ur.index('*') - 1
                    del self.ur[n : n + 3]
                    self.ur.insert(n, a * b)
                while '/' in self.ur:
                    a = self.ur[self.ur.index('/') - 1]
                    b = self.ur[self.ur.index('/') + 1]
                    n = self.ur.index('/') - 1
                    del self.ur[n : n + 3]
                    self.ur.insert(n, a / b)    
                while '+' in self.ur:
                    a = self.ur[self.ur.index('+') - 1]
                    b = self.ur[self.ur.index('+') + 1]
                    n = self.ur.index('+') - 1
                    del self.ur[n : n + 3]
                    self.ur.insert(n, a + b)
                while '-' in self.ur:
                    a = self.ur[self.ur.index('-') - 1]
                    b = self.ur[self.ur.index('-') + 1]
                    n = self.ur.index('-') - 1
                    del self.ur[n : n + 3]
                    self.ur.insert(n, a - b)               
                if self.y[-1].is_digit():
                    self.y.append('*')
                self.x = self.ur[0]
                self.ur = self.y[:]
                self.y = None
                self.output.setDigitCount(len(str(self.x)))
                self.output.display(self.x) 
        except Exception:
            self.all_error()        
    def plusm(self):
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        self.mmm += self.x
        self.x = 0
        self.output.setDigitCount(len(str(self.x)))
        self.output.display(self.x)        
    def minusm(self):
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        self.mmm -= self.x
        self.x = 0
        self.output.setDigitCount(len(str(self.x)))
        self.output.display(self.x)           
    def m_mc(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        self.x = self.mmm
        self.output.setDigitCount(len(str(self.x)))
        self.output.display(self.x)
    def delete_m(self):
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        self.mmm = 0
    def ccc(self):
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        self.x = 0
        st_kor_func_fl = False
        self.k = [False, False]
        self.nnn = 0
        self.ur = []
        self.mmm = 0
        self.fl_exp_func = False
        self.mode2nd = False
        self.x2 = 0
        self.output.setDigitCount(len(str(self.x)))
        self.output.display(self.x)        
    def cece(self):
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        if self.mode2nd:
            n = int(self.x)
            if n == self.x:
                self.x = 1
                while n != 0:
                    self.x *= n
                    n -= 1
                self.output.setDigitCount(len(str(self.x)))
                self.output.display(self.x)
            else:
                self.all_error()
        else:
            if len(self.ur) == 3:
                self.ur = []
            self.x = 0
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x)
            self.k = [False, False]
            
    def p_or_m(self):
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        if not self.mode2nd:
            self.x = -1 * self.x
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x)
        else:
            if self.x != self.ur[-2]:
                self.x2 = self.x
                self.x = self.ur[-2]
            else:
                self.x = self.x2
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x)
    def exp_func(self):
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        self.x = math.pi
        self.output.setDigitCount(len(str(self.x)))
        self.output.display(self.x)
    def st_kor_func(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        if self.mode2nd:
            self.st_kor_func_fl = True
            self.st_kor_func2 = self.x
            self.x = None
            self.k = [False, False]
        else:
            self.st_kor_func_fl = True
            self.st_kor_func2 = self.x            
            self.x = None
            self.k = [False, False]  
            
    def koren_f(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        try:
            if self.mode2nd:
                self.x = self.x ** (1 / 3)
            else:
                self.x = self.x ** 0.5
           
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x)
        except Exception:
            self.all_error()            
    def ln_f(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        try:
            if not self.mode2nd:
                self.x = math.log(self.x, math.e)
                self.k = [False, False]
            else:
                self.x = math.e ** self.x
                self.k = [False, False]
        
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x)            
        except Exception:
            self.all_error()
    def log_f(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        try:
            if not self.mode2nd:
                self.x = math.log10(self.x)
                self.k = [False, False]
            else:
                self.x = 10 ** self.x
                self.k = [False, False]
            
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x)
        except Exception:
            self.all_error()        
    def quadrat_f(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        try:
            if self.mode2nd:
                self.x = 1 / self.x
                self.k = [False, False]
            else:
                self.x = self.x ** 2
                self.k = [False, False]
            
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x) 
        except Exception:
            self.all_error()        
    def tab_f(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        try:
            if self.x != 0:
                x = self.x
                self.x = float(str(self.x)[:-1])
                if x == self.x:
                    try:
                        self.x = int(self.x)
                        self.x = int(str(self.x)[:-1])
                    except:
                        self.x = 0
                if self.x == int(self.x):
                    self.x = int(self.x)
                    self.k = [False, False]                    
                elif '.' in str(self.x):
                    x = str(self.x).split('.')
                    if x[1] == '0':
                        self.k = [True, True]
                self.output.setDigitCount(len(str(self.x)))
                self.output.display(self.x)
        except Exception:
            self.all_error()        
    def sin_f(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        try:
            if self.mode2nd:
                self.x = math.asin(self.x)
                if self.m == 'deg':
                    self.x = math.degrees(self.x)
            else:
                if self.m == 'deg':
                    self.x = math.radians(self.x)
                self.x = math.sin(self.x)
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x) 
        except Exception:
            self.all_error()        
    def cos_f(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        try:
            if self.mode2nd:
                self.x = math.acos(self.x)
                if self.m == 'deg':
                    self.x = math.degrees(self.x)
            else:
                if self.m == 'deg':
                    self.x = math.radians(self.x)
                self.x = math.cos(self.x)
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x) 
        except Exception:
            self.all_error()        
    def tg_f(self):
        pygame.init() 
        pygame.mixer.Sound(self.zv[randint(0, 7)]).play()          
        if self.viv_fl:
            self.viv_fl = False
            self.ur = []        
        try:
            if self.mode2nd:
                self.x = math.atan(self.x)
                if self.m == 'deg':
                    self.x = math.degrees(self.x)
            else:
                if self.m == 'deg':
                    self.x = math.radians(self.x)
                self.x = math.tan(self.x)
            self.output.setDigitCount(len(str(self.x)))
            self.output.display(self.x)
        except Exception:
            self.all_error()        

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calc()
    ex.show()     
    sys.exit(app.exec())    