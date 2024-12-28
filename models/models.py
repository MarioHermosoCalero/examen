# -*- coding: utf-8 -*-

from odoo import api, fields, models, api, _
from dateutil.relativedelta import *
from datetime import date

class autoescuela(models.Model):
    _name = 'examen.autoescuela'
    _description = 'Permite definir las características de una autoescuela'
   

class profesor(models.Model):
    _name = 'examen.profesor'
    _description = 'Permite definir las características de un profesor de autoescuela'
 
  
class examen(models.Model):
    _name = 'examen.examen'
    _description = 'Permite definir las características de un examen \
            de conducir realizado o pendiente de realizar'
    

class alumno(models.Model):
    _name = 'examen.alumno'
    _description = 'Permite definir las características de un alumno'
    