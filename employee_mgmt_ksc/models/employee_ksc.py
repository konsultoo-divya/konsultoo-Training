from odoo import models, fields, api


class Employeeksc(models.Model):
    _name = 'employee.ksc'
    _description = 'Employee Ksc'

    employee_name_id = fields.Many2one('employee.department.ksc', string="Employee Name Id",help='about employee name')
    shift_id = fields.Many2one('employee.department.shift.ksc', string='Shift Id',help='about the shift id')
    name_of_the_employee = fields.Char(string="Name Of The Employee")
    Department_name_of_the_employee = fields.Many2one('employee.department.ksc', string='Department Name of The Employee' , required=True)
    job_position_of_employee = fields.Char(string="Employee Job Position")
    salary = fields.Float(string='Salary', digits=(6, 2))
    hire_date = fields.Date(string='Hire Date')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('transgender)', 'Transgender)')],
                              default='female', string="Gender")
    job_type = fields.Selection([('permanent', 'Permanent'), ('ad hoc', 'Ad Hoc')])
    is_manager = fields.Boolean(string="Is Manager",help='about is manager')
    manager_id = fields.Many2one('employee.ksc', string='Manger',help='about the manager')
    related_user = fields.Many2one('res.users', string='Related User',help='about related user id')
    employee_ids = fields.One2many('employee.ksc', 'manager_id', string='Employee Ids',help='about the many to one employee id')
    increment_percentage = fields.Float(string='Increment Percentage')





