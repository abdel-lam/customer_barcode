odoo.define("customer_barcode.db", function (require) {
    "use strict";

    var PosDB = require("point_of_sale.DB");
    var models = require("point_of_sale.models");

    models.load_fields("res.partner", ["ref"]);

    PosDB.include({
        _partner_search_string: function (partner) {
            var res = this._super(partner).replace("\n", "");
            if (res.ref) {
               res += "|" + partner.ref;
                }
            res += "\n";
            return res;
            }

    });
});