from odoo import models, fields, api
from datetime import datetime
from datetime import date
class EmployeeKsc(models.Model):
    _name = 'employee.ksc'
    _description = 'Employee Ksc'

    name_of_the_employee = fields.Char(string='Name of The Employee',  translate=True)
    department_name_of_the_employee = fields.Char(string='Department Name of The Employee')
    job_position_of_the_employee = fields.Char(string='Job Position of employee')
    salary = fields.Float(string="Salary", digits=(6,2))
    date = fields.Date(string="Hire date")
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')])
    job_type = fields.Selection([('permanent', 'Permanent'), ('ad hoc', 'Ad Hoc')])
