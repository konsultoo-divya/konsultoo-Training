from odoo import models, fields, api

class EmployeeKsc(models.Model):
    _name = 'employee.ksc'
    _description = 'Employee Ksc'

    name_of_the_employee = fields.Char(string='Employee Name',help='about name',  translate=True)
    department_name_of_the_employee = fields.Char(string='Employee Department',help='about Department')
    job_position_of_the_employee = fields.Char(string='Job Position',help='about job position')
    salary = fields.Float(string="Salary", digits=(6, 2),help='about salary')
    date = fields.Date(string="Hire date",help='about hire date')
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')])
    job_type = fields.Selection([('permanent', 'Permanent'), ('ad hoc', 'Ad Hoc')],help='about job type')