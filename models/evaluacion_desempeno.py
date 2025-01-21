from odoo import models, fields, api

class EvaluacionDesempeno(models.Model):
    _name="evaluacion.desempeno"
    _description="Evaluacion del Desempeño Empleado"

    titulo = fields.Char(string="Título de la Evaluación", required=True)
    empleado_id = fields.Many2one('hr.employee', string="Empleado", required=True)
    fecha_evaluacion = fields.Date(string="Fecha de Evaluación", default=fields.Date.today)
    comentarios = fields.Text(string="Comentarios del Evaluador")
    puntuacion = fields.Selection([
        (str(i), str(i)) for i in range(1, 11)
    ], string="Puntuación", required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado'),
    ], string="Estado", default='pendiente')

    # Restricciones de acceso
    def _check_manager_role(self):
        # Aquí se verifica si el usuario tiene el rol de gerente de RRHH
        if not self.env.user.has_group('hr.group_hr_manager'):
            raise PermissionError("No tienes permisos para realizar esta acción.")

    # Métodos para controlar permisos
    @api.model
    def create(self, vals):
        self._check_manager_role()
        return super(EvaluacionDesempeno, self).create(vals)

    def write(self, vals):
        self._check_manager_role()
        return super(EvaluacionDesempeno, self).write(vals)

    # Método para obtener evaluaciones del empleado
    def get_evaluaciones_empleado(self):
        return self.search([('empleado_id', '=', self.env.user.employee_id.id)])