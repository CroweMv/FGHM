# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import UserError


class Sale(models.Model):
   _inherit = 'sale.order'
   

    
