from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from app import db, admin

class Loaisach(db.Model):
    __tablename__ = "loaisach"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenloai = Column(String(50), nullable=False)
    sach = relationship('Sach', backref = "loaisach", lazy = True)

    def __str__(self):
        return self.tenloai

class Nxb(db.Model):
    __tablename__ = "nhaxuatban"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tennxb = Column(String(50), nullable=False)
    sach = relationship('Sach', backref="nhaxuatban", lazy=True)

    def __str__(self):
        return self.tennxb

class Sach(db.Model):
    __tablename__ = "sach"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tensach = Column(String(70), nullable=False)
    gia = Column(Float, default=0)
    soluong = Column(Integer, default=0)
    img = Column(String(255), nullable=True)
    Nxb_id = Column(Integer, ForeignKey(Nxb.id), nullable=False)
    loaisach_id = Column(Integer, ForeignKey(Loaisach.id), nullable=False)
    sach_tacgia = relationship('Sach_tacgia', backref="sach", lazy=True)
    phieumuon = relationship('Phieumuon', backref="sach", lazy=True)
    bienban = relationship('Bienban', backref="sach", lazy=True)

    def __str__(self):
        return self.tensach

class Tacgia(db.Model):
    __tablename__ = "tacgia"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tentg = Column(String(70), nullable=False)
    sach_tg = relationship('Sach_tacgia', backref="tacgia", lazy=True)

    def __str__(self):
        return self.tentg

class Sach_tacgia(db.Model):
    __tablename__ = "sach_tacgia"
    Sach_id = Column(Integer, ForeignKey(Sach.id), primary_key=True, nullable=False)
    Tacgia_id = Column(Integer, ForeignKey(Tacgia.id), primary_key=True, nullable=False)

class Ncc(db.Model):
    __tablename__ = "nhacungcap"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenncc = Column(String(70), nullable=False)
    phieunhap = relationship('Phieunhap', backref="nhacungcap", lazy=True)

    def __str__(self):
        return self.tenncc

class Khachhang(db.Model):
    __tablename__ = "khachhang"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenkh = Column(String(70), nullable=False)
    diachi = Column(String(50), nullable=False)
    sdt = Column(Integer, nullable=False)
    cmnd = Column(Integer, nullable=False)
    thethuvien = relationship('Thethuvien', backref="khachhang", lazy=True)
    phieumuon = relationship('Phieumuon', backref="khachhang", lazy=True)
    bienban = relationship('Bienban', backref="khachhang", lazy=True)

    def __str__(self):
        return self.tenkh

class Thuthu(db.Model):
    __tablename__ = "thuthu"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tentt = Column(String(70), nullable=False)
    diachi = Column(String(50), nullable=False)
    sdt = Column(Integer, nullable=False)
    cmnd = Column(Integer, nullable=False)
    baocao = relationship('Baocao', backref="thuthu", lazy=True)
    hoadonthe = relationship('Hoadonthe', backref="thuthu", lazy=True)
    phieunhap = relationship('Phieunhap', backref="thuthu", lazy=True)

    def __str__(self):
        return self.tentt

class Thethuvien(db.Model):
    __tablename__ = "thethuvien"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ngaycap = Column(Date, nullable=False)
    hsd = Column(Date, nullable=False)
    Khachhang_id = Column(Integer, ForeignKey(Khachhang.id), nullable=False)
    hoadonthe = relationship('Hoadonthe', backref="thethuvien", lazy=True)

    def __str__(self):
        return self.name

class Hoadonthe(db.Model):
    __tablename__ = "hoadonlamthe"
    Thethuvien_id = Column(Integer, ForeignKey(Thethuvien.id), primary_key=True, nullable=False)
    Thuthu_id = Column(Integer, ForeignKey(Thuthu.id), primary_key=True, nullable=False)
    chiphi = Column(Float, default=0)

    def __str__(self):
        return self.name

class Baocao(db.Model):
    __tablename__ = "baocao"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ngaylap = Column(Date, nullable=False)
    Thuthu_id = Column(Integer, ForeignKey(Thuthu.id), nullable=False)

    def __str__(self):
        return self.name

class Phieumuon(db.Model):
    __tablename__ = "phieumuon"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ngaymuon = Column(Date, nullable=False)
    ngayphaitra = Column(Date, nullable=False)
    Khachhang_id = Column(Integer, ForeignKey(Khachhang.id), nullable=False)
    Sach_id = Column(Integer, ForeignKey(Sach.id), nullable=False)

    def __str__(self):
        return self.name

class Bienban(db.Model):
    Khachhang_id = Column(Integer, ForeignKey(Khachhang.id), primary_key=True, nullable=False)
    Sach_id = Column(Integer, ForeignKey(Sach.id), primary_key=True, nullable=False)
    ngayvipham = Column(Date, nullable=False)
    loivipham = Column(String(50), nullable=False)
    xuly = Column(String(50), nullable=False)

    def __str__(self):
        return self.name

class Phieunhap(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    tensach = Column(String(70), nullable=False)
    soluong = Column(Integer, nullable=False)
    dongia = Column(Integer, default=0)
    ngaygiao = Column(Date, nullable=False)
    Thuthu_id = Column(Integer, ForeignKey(Thuthu.id), nullable=False)
    Ncc_id = Column(Integer, ForeignKey(Ncc.id), nullable=False)

    def __str__(self):
        return self.tensach



admin.add_view(ModelView(Loaisach, db.session))
admin.add_view(ModelView(Sach, db.session))
admin.add_view(ModelView(Nxb, db.session))
admin.add_view(ModelView(Tacgia, db.session))
admin.add_view(ModelView(Ncc, db.session))
admin.add_view(ModelView(Khachhang, db.session))
admin.add_view(ModelView(Thuthu, db.session))
admin.add_view(ModelView(Thethuvien, db.session))
admin.add_view(ModelView(Hoadonthe, db.session))
admin.add_view(ModelView(Baocao, db.session))
admin.add_view(ModelView(Bienban, db.session))
admin.add_view(ModelView(Phieumuon, db.session))
admin.add_view(ModelView(Phieunhap, db.session))

if __name__ == "__main__":
    db.create_all()
