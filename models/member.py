from odoo import api, fields, models


class Member(models.Model):
    _name = 'perpus.member'
    _description = 'Daftar Member'

    name = fields.Char(string='Nama')
    id_member = fields.Char(string='Id_Member')
    alamat = fields.Char(string='Alamat')
    kelas = fields.Selection(string='Kelas', selection=[('x', 'X'), ('xi', 'XI'),('xii', 'XII')])
    jurusan = fields.Selection(string='Jurusan', selection=[('rpl', 'RPL'), ('mm', 'MM'), ('tkj', 'TKJ'), ('otkp', 'OTKP'), ('akl', 'AKL'), ('kky', 'KKY'), ('tbsm', 'TBSM')])
    jenis_kelamin = fields.Selection(string='Jenis Kelamain', selection=[('laki-laki', 'Laki-Laki'), ('perempuan', 'Perempuan'),])
    
    
   
    
    
    