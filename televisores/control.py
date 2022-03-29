class Control:
    def __init__(self):
        self._tv=None
    
    def turnOn(self):
        self._tv.turnOn()
    
    def turnOff(self):
        self._tv.turnOff()
        
    def canalUp(self):
        self._tv.canalUp()
    
    def canalDown(self):
        self._tv.canalDown()
    
    def volumenUp(self):
        self._tv.volumenUp()
    
    def volumeDown(self):
        self._tv.volumeDown()
    
    def setCanal(self,canal):
        self._tv.setCanal(canal)
    
    def enlazar(self,tv):
        self._tv=tv
        self._tv.setControl(self)
    
    def setTv(self,tv):
        self._tv=tv
    
    def getTv(self):
        return self._tv

