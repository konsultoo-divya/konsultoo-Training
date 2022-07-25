from odoo import models, fields, api


class EmployeeDepartmentShiftKsc(models.Model):
    _name = 'employee.department.shift.ksc'
    _description = 'Employee Mgmt Shift Ksc'
    _rec_name = 'shift'

    shift = fields.Selection([('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening'), ('night','Night')], string='Shift', help='about the shift selection')
    employee_ids = fields.One2many('employee.ksc', 'shift_id', string='Employee Ids',help='about employee ids')