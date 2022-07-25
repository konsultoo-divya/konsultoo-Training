from odoo import models, fields, api


class EmployeeDepartmentKsc(models.Model):
    _name = 'employee.department.ksc'
    _description = 'Employee Mgmt Ksc'

    department_name = fields.Char(string="Department Name", required=True,help='about employee department name')
    employees_ids = fields.One2many('employee.ksc', 'employee_name_id', string="employee_ids",help='about employees ids one department have many employee')
    department_manager = fields.Many2one('res.users', string='Department Manager',help='about manager id')


