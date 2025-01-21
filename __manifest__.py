{
    "name": "Evaluación de Desempeño",
    "version": "1.0",
    "summary": "Módulo para gestionar el desempeño de los empleados de la empresa",
    "category": "Productivity",
    "author": "Héctor Martín",
    "website": "https://tuweb.com",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "icon": "/evaluacion_desempeno/static/description/icon53.png",
    "data": [
        "views/evaluacion_desempeno_views.xml",
        "security/ir.model.access.csv"
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
    "description": """
                    Módulo de Odoo para la gestión del desempeño con el que se califica a nuestros empleados
                    """,
}