from email.policy import default
from odoo.exceptions import ValidationError
from odoo import api, fields, models
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class PeminjamanBuku(models.Model):
    _name = 'perpus.peminjaman'
    _description = 'New Description'

    peminjamanbukudetail_ids = fields.One2many(
        comodel_name='perpus.peminjamanbukudetail',
        inverse_name='name',
        string='Detail Peminjaman Buku')

    name = fields.Many2one(comodel_name='perpus.member', string='Id Member')
    

    tanggal_pinjam = fields.Date('Tanggal Peminjaman', default = fields.Date.today())
    tanggal_kembali = fields.Date(string='tanggal_kembali')
    
    # @api.depends('tanggal_pinjam')
    # def _compute_tanggal_kembali(self):
    #     for rec in self:
    #         self.tanggal_kembali=datetime.strptime(str(self.tanggal_pinjam),'%Y-%m-%d')+relativedelta(days=+7)
     
    @api.onchange('tanggal_pinjam')
    def _onchange_tanggal_kembali(self):
        self.tanggal_kembali=datetime.strptime(str(self.tanggal_pinjam),'%Y-%m-%d')+relativedelta(days=+7) 
   
    sudah_kembali = fields.Boolean(string='Sudah Dikembalikan', default=False)
    

class PeminjamanBukuDetail(models.Model):
    _name = 'perpus.peminjamanbukudetail'
    _description = 'New Description'

    name = fields.Many2one(comodel_name='perpus.peminjaman', string='Peminjaman')
    
    buku_id = fields.Many2one(
        comodel_name='perpus.buku',
        string='Judul Buku',
        domain=[('stok', '>', '1')])
    name = fields.Char(string='Name')
    
    