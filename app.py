from flask import Flask, render_template, request, redirect
import models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'inikuncinya'

list_dokter = {
    'D01': 'Dr. Budi Hartono',
    'D02': 'Dr. Haryadi',
    'D03': 'Dr. Karisman S',
    'D04': 'Dr. Kartini'
}


@app.route('/')
def index():
    list_pasien = models.tampil_passien()
    return render_template('home.html', list_pasien=list_pasien)


@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    form = models.RegisterForm()
    if request.method == 'POST':
        if form.validate():
            nik = form.nik.data
            nama = form.nama.data
            tanggal_lahir = form.tanggal_lahir.data.strftime('%Y-%m-%d')
            alamat = form.alamat.data
            penyakit = form.penyakit.data
            dokter = form.dokter.data
            tanggal_reservasi = form.tanggal_reservasi.data.strftime(
                '%Y-%m-%d')

            models.tambah_pasien(nik, {
                'nama': nama,
                'tanggal_lahir': tanggal_lahir,
                'alamat': alamat,
                'penyakit': penyakit,
                'dokter': list_dokter[dokter],
                'tanggal_reservasi': tanggal_reservasi
            })
            return redirect('/')
        else:
            errors = form.errors.items()
            return render_template('form.html', form=form, errors=errors)
    return render_template('form.html', form=form)


@app.route('/hapus', methods=['POST'])
def hapus():
    nik = request.form['nik']
    models.hapus_pasien(nik)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
