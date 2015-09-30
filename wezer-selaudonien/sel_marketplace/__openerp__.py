# -*- coding: utf-8 -*-
#
#
#    Website Marketplace for SELAUDONIEN
#    Valeureux.org
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

{
    'name': 'Website Custom Marketplace For Selaudonien',
    'category': 'Website',
    'summary': 'Custom addition to Website marketplace module',
    'version': '1.0',
    'description': """
Custom Theme
Website Marketplace

        """,
    'author': 'Author Name • Valeureux.org',
    'depends': [
        'website',
        'marketplace',
        'marketplace_groups',
        'website_base_community'
    ],
    'data': [
        'views/templates/edit_announcement.xml',
        'views/templates/new_announcement.xml',
    ],
    'installable': True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
