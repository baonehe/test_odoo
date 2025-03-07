from odoo import models, fields, api
from odoo.exceptions import UserError

class EmployeeSkill(models.Model):
    _name = 'employee.skills'
    _description = 'Employee Skills'

    name = fields.Char(string="Skill Name", required=True)
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    critical = fields.Boolean(string="Critical Skill")

    def send_critical_skill_email(self):
        """Send an email notification if the skill is critical"""
        if not self.critical:
            raise UserError("This skill is not marked as critical.")

        mail_template = self.env.ref('employee_skills.email_template_notify_hr')
        if mail_template:
            mail_template.send_mail(self.id, force_send=True)
        else:
            raise UserError("Email template not found.")
