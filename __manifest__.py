
{
    "name": "Sequential Code for Customers",
    "version": "14.0.1.0.0",
    "category": "Points of Sale",
    "author": "Lamrabti Abdellatif",
    "website": "",
    "license": "AGPL-3",
    "depends": ["base","point_of_sale"],
    "data": ["data/lead_sequence.xml"],
    "assets": {
        'point_of_sale.assets': [
            '/customer_barcode/static/src/js/db.js'],
    },
    "installable": True,
}
