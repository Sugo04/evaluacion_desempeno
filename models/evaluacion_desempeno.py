from odoo import models, fields, api

class EvaluacionDesempeno(models.Model):
    _name = "evaluacion.desempeno"
    _description = "Evaluacion del Desempeño Empleado."
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Título de Evaluación", required=True, tracking=True)
    employee_id = fields.Many2one('res.users', string="Empleado", required=True, tracking=True)
    fecha_evaluacion = fields.Date(string="Fecha de Evaluación", required=True, tracking=True)
    comentarios = fields.Text(string="Comentarios del Evaluador", tracking=True)
    puntuacion = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    ], string="Puntuación", required=True, tracking=True)
    
    state = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado')
    ], string="Estado", default='pendiente', tracking=True)

    color = fields.Integer(string='Color Index')
    
    @api.model
    def create(self, vals):
        record = super(EvaluacionDesempeno, self).create(vals)
        return record

    def action_en_proceso(self):
        self.write({'state': 'en_proceso'})

    def action_finalizar(self):
        self.write({'state': 'finalizado'})