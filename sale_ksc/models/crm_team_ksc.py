from odoo import api, models, fields


class CrmTeamKsc(models.Model):
    _name = 'crm.team.ksc'
    _description = 'Crm Team Ksc'

    name = fields.Char(string='name',help='about name')
    team_leader_id = fields.Many2one('res.users', string='team_leader_id', help='about team leader id')
