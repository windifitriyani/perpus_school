from odoo import api, fields, models


class Buku(models.Model):
    _name = 'perpus.buku'
    _description = 'Daftar Buku'

    kode = fields.Char(string='Kode Buku', required=True)
    name = fields.Char(string='Judul Buku')
    img = fields.Binary(string='Image')
    penulis = fields.Char(string='Penulis')
    penerbit = fields.Char(string='Penerbit')
    tahun_terbit = fields.Char(string='Tahun Terbit')
    jenis_buku = fields.Selection(string='Jenis Buku', selection=[('buku produktif', 'Buku Produktif'), ('buku pelajaran', 'Buku Pelajaran'),])
    buku_mapel_kelas = fields.Selection(string='Buku Mapel Kelas', selection=[('x', 'X'), ('xi', 'XI'), ('xii', 'XII')])
    stok = fields.Integer(string='Stok')
    
    