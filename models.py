from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import InputRequired, ValidationError

list_pasien = {}


def ValidateNIK(form, field):
    if len(field.data) != 16:
        raise ValidationError('NIK tidak sesuai.')


class RegisterForm(FlaskForm):
    nik = StringField('Nomor Induk Kependudukan', validators=[
                      InputRequired('NIK harus diisi.'), ValidateNIK])
    nama = StringField('Nama Pasien', validators=[
                       InputRequired('Nama harus diisi.')])
    tanggal_lahir = DateField('Tanggal Lahir', validators=[
                              InputRequired('Tanggal lahir harus diisi')])
    alamat = StringField('Alamat Pasien', validators=[
                         InputRequired('Alamat harus diisi.')])
    penyakit = StringField('Penyakit', validators=[
                           InputRequired('Penyakit harus diisi.')])
    dokter = SelectField('Dokter', validators=[
                         InputRequired('Dokter harus dipilih.')], choices=[
        ('D01', 'Dr. Budi Hartono'),
        ('D02', 'Dr. Haryadi'),
        ('D03', 'Dr. Karisman S'),
        ('D04', 'Dr. Kartini')
    ])
    tanggal_reservasi = DateField('Tanggal Reservasi', validators=[
                                  InputRequired('Tanggal reservasi harus diisi.')])
    kirim = SubmitField('Kirim')


def tampil_passien():
    return list_pasien


def tambah_pasien(nik, pasien):
    list_pasien[nik] = pasien


def hapus_pasien(nik):
    list_pasien.pop(nik)
