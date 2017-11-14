(function (a) {
    a.EditcreateModal = function (b) {
        defaults = {title: "", message: "Your Message Goes Here!", closeButton: true, scrollable: false};
        var b = a.extend({}, defaults, b);
        var c = (b.scrollable === true) ? 'style="max-height: 420px;overflow-y: auto;z-index: 9999999;"' : "";
        html = '<div class="modal fade" id="myModal" style="z-index: 9999999">';
        html += '<div class="modal-dialog">';
        html += '<div class="modal-content">';
        html += '<div class="modal-header modal_bg_info">';
        html += '<a class="modal_bg_close" data-dismiss="modal"><span><i class="fa fa-remove fa-2x" style="cursor: pointer"></i></span></a>';
        if (b.title.length > 0) {
            html += '<h4 class="modal-title">' + b.title + "</h4>"
        }
        html += "</div>";
        html += '<div class="modal-body" ' + c + ">";
        html += b.message;
        html += "</div>";
        html += '<div class="modal-footer">';
        if (b.closeButton === true) {
            html += '<button type="button" class="btn modal_bg_info" data-dismiss="modal">Cerrar</button>'
        }
        html += "</div>";
        html += "</div>";
        html += "</div>";
        html += "</div>";
        a("body").prepend(html);
        a('.modal-content').resizable({
            minHeight: 650,
            maxHeight: 850,
            minWidth: 500
        });
        a('.modal-dialog').draggable();

        a("#myModal").modal().on("hidden.bs.modal", function () {
            a(this).remove()
        })
    }
})(jQuery);
