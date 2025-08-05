
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http
from odoo.http import request

class MyWebsiteController(http.Controller):

    @http.route('/', type='http', auth='public', website=True)
    def homepage(self, **kw):
        announced = request.env.ref('event.event_stage_announced').id
        event = request.env['event.event'].sudo().search(
            [('stage_id', '=', announced)], limit=1
        )
        return request.render('website.homepage', {
            'event': event,
        })

class WebsiteSaleSkipDelivery(WebsiteSale):

    @http.route(['/shop/checkout'], type='http', auth="public", website=True, sitemap=False)
    def checkout(self, **post):
        res = super().shop_checkout(**post)
        order = request.website.sale_get_order()
        if order:
            # Remove carrier or set dummy one if required
            order.carrier_id = None
            request.session['sale_order_delivery'] = True  # Mark delivery as done

        # IMPORTANT: Call parent via method resolution order
        return request.redirect('/shop/confirm_order')

class L10nBRWebsiteSale(WebsiteSale):

    def _check_cart_and_addresses(self, order_sudo):
        """ Check whether the cart and its addresses are valid, and redirect to the appropriate page
        if not.

        :param sale.order order_sudo: The cart to check.
        :return: None if both the cart and its addresses are valid; otherwise, a redirection to the
                 appropriate page.
        """
        if redirection := self._check_cart(order_sudo):
            return redirection

        return redirection