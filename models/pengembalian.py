from odoo import api, fields, models
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta



class Pengembalian(models.Model):
    _name = 'perpus.pengembalian'
    _description = 'Pengembalian Buku yang Telah Dipinjam'

   
    name = fields.Char(string='name')
    
    # @api.depends('peminjaman_id')
    # def _compute_name(self):
    #     for rec in self :
    #         rec.name = rec.peminjaman_id.id_member

    peminjaman_id = fields.Many2one(comodel_name='perpus.peminjaman', string='Peminjaman',  domain=[('sudah_kembali','=',False)])
    tgl_pinjam = fields.Date(compute='_compute_tgl_pinjam', string='tgl_pinjam')

    
    
    @api.depends('peminjaman_id')
    def _compute_tgl_pinjam(self):
        for rec in self:
            rec.tgl_pinjam = rec.peminjaman_id.tanggal_pinjam

    tgl_standar_kembali = fields.Date(string='tgl_standar_kembali')
    
    @api.onchange('peminjaman_id')
    def _onchange_tgl_standar_kembali(self):
        if self.tgl_pinjam:
            self.tgl_standar_kembali=datetime.strptime(str(self.tgl_pinjam),'%Y-%m-%d') + timedelta(days=7)

    # @api.depends('peminjaman_id')
    # def _compute_nama_peminjam(self):
    #     for record in self:
    #         record = self.env['perpus.peminjaman'].search([('id', '=', record.peminjaman_id.id)]).mapped('id_member')

    tgl_pengembalian = fields.Date(string='Tanggal Pengembalian', default=fields.Date.today())

    denda = fields.Integer(string='Denda', store=True)
    

    @api.onchange('tgl_pengembalian','tgl_standar_kembali')
    def calculate_denda(self):
        d1=datetime.strptime(str(self.tgl_pengembalian),'%Y-%m-%d') 
        if self.tgl_standar_kembali:
            d2=datetime.strptime(str(self.tgl_standar_kembali),'%Y-%m-%d')
            d3=(d1-d2).days
            if d3>0:
                self.denda = d3 * 1000
            else:
                self.denda = 0
        


    @api.model
    def create(self, vals):
        record = super(Pengembalian, self).create(vals)
        if record.tgl_pengembalian:
            self.env['perpus.peminjaman'].search([('id', '=', record.peminjaman_id.id)]).write({'sudah_kembali':True})        
            return record

    def unlink(self):
        for devi in self:
            self.env['perpus.peminjaman'].search([('id', '=', devi.peminjaman_id.id)]).write({'sudah_kembali':False})
        record = super(Pengembalian, self).unlink()
    