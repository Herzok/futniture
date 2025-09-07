from datetime import timedelta
from odoo.exceptions import UserError
from odoo import fields, models

class ActionsWorkDevice(models.AbstractModel):
    _name = "furniture.devices.actions"
    _description = "actions for work device"
    
    def action_take_work(self):
        self.write({
                'status': 'in_process',
            })
    def action_finish_work(self):
        self.write({
                'status': 'done',
                'date_end': fields.Datetime.now(),
            })
        

class ActionsFurniture(models.AbstractModel):
    _name = "furniture.orders.actions"
    _description = "Common actions for furniture orders"
    
    def action_take(self):
        self.write({
                'date_start': fields.Datetime.now(),
                'status': 'in_process',
                'date_end': fields.Datetime.now() + timedelta(days=3),
                'employee_id': self.env.user.id
            })
    
    def action_finish(self):
        for rec in self:
            if rec.date_end:
                if rec.date_end > fields.Datetime.now():
                    rec.write({
                    "date_end": fields.Datetime.now(),
                    "status": "done"
                    })
                else: 
                    rec.write({"status": "unfinished"})
                    self.env.cr.commit()
                    raise UserError('Время на выполнение истекло')
                    
            else:
                raise UserError('Нет даты окончания работы')
                
    def action_confirm_reject(self):
        for rec in self:
            if not rec.reason:
                raise UserError("Укажите причину брака")
            rec.status = 'defective'
            
    def action_confirm_cancel(self):
        for rec in self:
            if not rec.reason:
                raise UserError("Укажите причину невозможности исполнения")
            rec.status = 'cancel'
    
    def open_reject_wizard(self):
        self.ensure_one()
        view = self.env.ref('furniture_orders.view_furniture_order_reject_wizard_form')
        return {
        'name': "Причина брака",
        'type': 'ir.actions.act_window',
        'res_id': self.id,
        'res_model': 'furniture.orders',
        'views': [(view.id, 'form')],
        'target': 'new',
        }
    
    def open_cancel_wizard(self):
        self.ensure_one()
        view = self.env.ref('furniture_orders.view_furniture_order_cancel_wizard_form')
        return {
        'name': "Причина невыполнения",
        'type': 'ir.actions.act_window',
        'res_id': self.id,
        'res_model': 'furniture.orders',
        'views': [(view.id, 'form')],
        'target': 'new',
        }