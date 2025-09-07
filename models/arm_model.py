from odoo import models, fields


class FurnitureOrders(models.Model):
    _name = 'furniture.orders'
    _description = 'orders for creation furniture'
    _inherit = ["furniture.orders.actions"]
    
    name_order = fields.Char('name order', translate=True)
    number_order = fields.Char('number order')
    desc = fields.Text('desc order')
    status = fields.Selection(
        [
            ('ready_for_prod','Готов к производству'),
            ('done','Завершен'),
            ('in_process','В процессе'),
            ('defective','Брак'),
            ('unfinished', 'Просрочен в работе'),
            ('cancel','Отменен')
        ],
        string="Status",
        default='ready_for_prod',
        required=True)
    date_start = fields.Datetime('date start')
    date_end = fields.Datetime('date end')
    reason = fields.Text('reason')
    employee_id = fields.Many2one(
        'res.users',
        string="Оператор аппарата"
    )
    
    _sql_constraints = [
        ('customer_order_unique', 'unique(number_order)', 'Order number must be unique!')
    ]
    
class Devices(models.Model):
    _name = 'furniture.devices'
    _description = 'device for employee'
    
    name_device=fields.Char('Название аппарата')
    status = fields.Selection(
        [
            ('working','normal work'),
            ('broken','broken device'),
            ('cleaning','clear device'),
            ('repairing','repair device'),
            ('change_details', 'Unfinished'),
        ],
        string="Status",
        required=True)
    
class DeviceWork(models.Model):
    _name = 'furniture.devices_work'
    _description = 'device for employee'
    _inherit = ["furniture.devices.actions"]
    
    device_id=fields.Many2one(
        'furniture.devices',
        string="Аппарат"
    )
    type = fields.Selection(
        [
            ('change','Замена оборудования'),
            ('plan_service','Плановое обслуживание'),
            ('repair','Починка оборудования'),
        ],)
    status = fields.Selection(
        [
            ('in_process','В процессе'),
            ('done','Завершено'),
            ('planed','Запланировано'),
        ],)
    desc_work = fields.Text('описание работ')
    date_start = fields.Datetime('date start work')
    date_end = fields.Datetime('date end work')