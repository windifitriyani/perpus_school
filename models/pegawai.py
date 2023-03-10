from odoo import api, fields, models


class Pegawai(models.Model):
    _name = 'perpus.pegawai'
    _description = 'Pegawai yang ada di perpus'

    kode_pegawai = fields.Char(string='Kode Pegawai')
    nama = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    ttl = fields.Char(string='Tempat Tanggal Lahir')
    jenis_kelamin = fields.Char(string='Jenis Kelamin')
    
    
