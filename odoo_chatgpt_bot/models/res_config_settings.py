# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    openapi_api_key = fields.Char(string="openAPI Key")
    openapi_chatgpt_role = fields.Char(string="定义AI角色描述")
    limit_channel_count = fields.Integer(string="频道对话次数")

    def set_values(self):
        """
        set values
        """
        super(ResConfigSettings, self).set_values()
        ir_config = self.env['ir.config_parameter'].sudo()
        ir_config.set_param("odoo_chatgpt_bot.openapi_api_key", self.openapi_api_key)
        ir_config.set_param("odoo_chatgpt_bot.limit_channel_count", self.limit_channel_count)
        ir_config.set_param("odoo_chatgpt_bot.openapi_chatgpt_role", self.openapi_chatgpt_role)

    @api.model
    def get_values(self):
        """
        get vuales
        """
        res = super(ResConfigSettings, self).get_values()
        config = self.env['ir.config_parameter'].sudo()
        openapi_api_key = config.get_param(key='odoo_chatgpt_bot.openapi_api_key', default='xxxxxx')
        limit_channel_count = config.get_param(key='odoo_chatgpt_bot.limit_channel_count', default=20)
        openapi_chatgpt_role = config.get_param(key='odoo_chatgpt_bot.openapi_chatgpt_role', default="个人AI小助手")
        res.update(
            openapi_api_key=openapi_api_key,
            limit_channel_count=limit_channel_count,
            openapi_chatgpt_role=openapi_chatgpt_role,
        )
        return res
