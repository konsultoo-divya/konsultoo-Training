from odoo import models, fields, api


class EmployeeLeaveKsc(models.Model):
    _name = 'employee.leave.ksc'
    _description = 'Employee Leave Ksc'

    employee_id = fields.Many2one('employee.ksc', string='Employee Id',help='about employee name')
    department_id = fields.Many2one('employee.department.ksc', string='Department',help='about department many to one')
    start_date = fields.Date(string='Start date',help='about start date')
    end_date = fields.Date(string='end_date',help='about the end date')
    status = fields.Selection([('draft', 'Draft,'), ('approved', 'Approved,'), ('refused,', 'Refused,'), ('cancelled','Cancelled')], default='Draft',help='about to state')
    leave_description = fields.Char(string='Leave Description', required=True ,help='about the help description')
