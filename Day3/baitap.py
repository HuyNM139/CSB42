class TaiKhoan:
    def __init__(self,stk,ten,so_du=0):
        self.stk=stk
        self.ten=ten
        self.so_du=so_du
    def nap_tien(self,so_tien):
        if so_tien>0:
            self.so_du+=so_tien
    def rut_tien(self,so_tien):
        if 0<so_tien<=self.so_du:
            self.so_du-=so_tien
    def lay_so_du(self):
        return self.so_du
class TaiKhoanTietKiem(TaiKhoan):
    def __init__(self,stk,ten,so_du=0,lai_suat=0.0):
        super().__init__(stk,ten,so_du)
        self.lai_suat=lai_suat
    def ap_dung_lai(self):
        self.so_du+=self.so_du*self.lai_suat