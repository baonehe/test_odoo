import pytest
from odoo.tests.common import TransactionCase
from unittest.mock import patch


@pytest.fixture
def create_employee(env):
    """Tạo employee giả lập để dùng trong test"""
    return env['hr.employee'].create({'name': 'Test Employee'})


@pytest.fixture
def create_skill(env, create_employee):
    """Tạo kỹ năng và liên kết với employee"""
    def _create_skill(name, critical):
        return env['employee.skills'].create({
            'name': name,
            'employee_id': create_employee.id,
            'critical': critical,
        })
    return _create_skill


class TestEmployeeSkills(TransactionCase):

    def test_email_not_sent_for_non_critical_skill(self):
        """Test rằng email không được gửi khi critical=False"""
        skill = self.env['employee.skills'].create({
            'name': 'Python',
            'employee_id': self.env['hr.employee'].create({'name': 'Test User'}).id,
            'critical': False,
        })

        with patch('your_module.models.employee_skills.send_email') as mock_send_email:
            skill.trigger_email_notification()
            mock_send_email.assert_not_called()

    def test_email_sent_for_critical_skill(self):
        """Test rằng email được gửi khi critical=True"""
        skill = self.env['employee.skills'].create({
            'name': 'Security',
            'employee_id': self.env['hr.employee'].create({'name': 'Test User'}).id,
            'critical': True,
        })

        with patch('your_module.models.employee_skills.send_email') as mock_send_email:
            skill.trigger_email_notification()
            mock_send_email.assert_called_once()
