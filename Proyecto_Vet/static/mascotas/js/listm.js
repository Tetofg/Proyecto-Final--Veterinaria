$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },

        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                text: 'Descargar Excel <i class="fas fa-file-excel"></i>',
                titleAttr: 'Excel',
                className: 'btn btn-success btn-flat btn-xs'
            },
            {
                extend: 'pdfHtml5',
                text: 'Descargar Pdf <i class="fas fa-file-pdf"></i>',
                titleAttr: 'PDF',
                className: 'btn btn-danger btn-flat btn-xs',
                download: 'open',
                orientation: 'landscape',
                pageSize: 'LEGAL',
                customize: function (doc) {
                    doc.styles = {
                        header: {
                            fontSize: 18,
                            bold: true,
                            alignment: 'center'
                        },
                        subheader: {
                            fontSize: 13,
                            bold: true
                        },
                        quote: {
                            italics: true
                        },
                        small: {
                            fontSize: 8
                        },
                        tableHeader: {
                            bold: true,
                            fontSize: 11,
                            color: 'white',
                            fillColor: '#2d4154',
                            alignment: 'center'
                        }
                    };
                    doc.content[1].table.widths = ['5%','15%','10%','10%','15%','10%','15%','15%'];
                    doc.content[1].margin = [0, 35, 0, 0];
                    doc.content[1].layout = {};
                    doc['footer'] = (function (page, pages) {
                        return {
                            columns: [
                                {
                                    alignment: 'left',
                                    text: ['Fecha de creación: ', {text: "Hoy"}]
                                },
                                {
                                    alignment: 'right',
                                    text: ['página ', {text: page.toString()}, ' de ', {text: pages.toString()}]
                                }
                            ],
                            margin: 20
                        }
                    });

                }
            }
        ],

        columns: [
            {"data": "id"},
            {"data": "name"},
            {"data": "cat.name"},
            {"data": "vaccine"},
            {"data": "sta"},
            {"data": "breed"},
            {"data": "rescue_date"},
            {"data": "illness"}
        ],
        columnDefs: [
            {
                targets: [-5],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var html = '';
                    $.each(row.vaccine, function(key, value){
                        html+='<span class= "badge badge-info">'+value.name+'</span>';
                    });
                    return html;
                }
            },
            {
                targets: [-4],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var html = '';
                    var a = data;
                    if (data == 'in_adoption'){
                        html+='<span class= "badge badge-success">En Adopcion</span>';
                        return html;
                    }else{
                        html+='<span class= "badge badge-success">Adoptado</span>';
                        return html;
                    }

                }
            },
            
        ],
        initComplete: function (settings, json) {

        }
    });
});