from django.db import models

class TacGia(models.Model):
    # định nghĩa các trường của model Tác giả
    ma_tac_gia = models.CharField(max_length=8, primary_key=True)
    ten_tac_gia = models.CharField(max_length=50)
    
    class Meta:
        # sắp xếp data theo thứ tự mã tác giả
        ordering = ['ma_tac_gia']
    
    def __str__(self):
        return f'{self.ma_tac_gia}, {self.ten_tac_gia}'
    
class TheLoai(models.Model):
    # định nghĩa các trường của model Thể loại
    ma_the_loai = models.CharField(max_length=8, primary_key=True)
    ten_the_loai = models.CharField(max_length=50)
    
    class Meta:
        # sắp xếp data theo thứ tự mã thể loại
        ordering = ['ma_the_loai']
    
    def __str__(self):
        return f'{self.ma_the_loai}, {self.ten_the_loai}'

class Sach(models.Model):
    # định nghĩa các trường của model Sách
    ma_sach = models.CharField(max_length=8, primary_key=True)
    ten_sach = models.CharField(max_length=50)
    nam_xuat_ban = models.DateField()
    nha_xuat_ban = models.CharField(max_length=50)
    gia = models.IntegerField()
    so_luong = models.IntegerField()
    tac_gia = models.ManyToManyField(TacGia)
    the_loai = models.ManyToManyField(TheLoai)
    
    class Meta:
        # sắp xếp data theo thứ tự mã sách
        ordering = ['ma_sach']
    
    def __str__(self):
        return f'{self.ma_sach}, {self.ten_sach}, {self.ten_the_loai}, {self.nam_xuat_ban}, {self.nha_xuat_ban}, {self.gia}, {self.so_luong}'
    
class TheThanhVien(models.Model):
    # định nghĩa các trường của model Thẻ thư viện
    ma_the = models.CharField(primary_key=True, max_length=8)
    cccd = models.CharField(max_length=12)
    ho_va_ten = models.CharField(max_length=50)
    dia_chi = models.CharField(max_length=200)
    sdt = models.CharField(max_length=10)
    ngay_cap = models.DateField()
    
    # sắp xếp data theo thứ tự mã thẻ    
    class Meta:
        ordering = ['ma_the']
    
    def __str__(self):
        return f'{self.ma_the}, {self.cccd}, {self.ho_va_ten}, {self.dia_chi}, {self.sdt}, {self.ngay_cap}'
    
class KyHanMuonSach(models.Model):
    ky_han = models.CharField(max_length=50, primary_key=True)
    so_ngay = models.IntegerField()
    bieu_phi = models.IntegerField()
    
    class Meta:
        ordering = ['ky_han']
        
    def __str__(self):
        return f'{self.ky_han}, {self.so_ngay}, {self.bieu_phi}'
    
class BieuMauMuonTra(models.Model):
    # định nghĩa các trường của model Biểu mẫu mượn - trả
    ma_bieu_mau = models.CharField(max_length=8, primary_key=True)
    ma_the = models.ForeignKey(TheThanhVien, on_delete=models.SET_DEFAULT("Unknown"))
    ngay_muon = models.DateField(auto_now_add=True)
    ky_han = models.ForeignKey(KyHanMuonSach)
    ngay_tra = models.DateField()
    tinh_trang = models.BooleanField()
    
    class Meta:
        ordering = ['ma_bieu_mau']
    
    def __str__(self):
        return f'{self.ma_bieu_mau}, {self.ma_the}, {self.ngay_muon}, {self.ky_han}, {self.ngay_tra},  {self.tinh_trang}'
    
class ChiTietBieuMauMuonTra(models.Model):
    # định nghĩa các trường của model Chi tiết biểu mẫu
    ma_bieu_mau = models.ForeignKey(BieuMauMuonTra, on_delete=models.SET_DEFAULT("Unknown"))
    ma_sach = models.ForeignKey(Sach)
    so_luong = models.IntegerField()
    so_sach_nhan_lai = models.IntegerField()
    
    class Meta:
        ordering = ['ma_bieu_mau', 'ma_the']
        unique_together = (("ma_bieu_mau", "ma_sach"),)
    
    def __str__(self):
        return f'{self.ma_bieu_mau}, {self.ma_sach}, {self.so_luong}, {self.so_sach_nhan_lai}'