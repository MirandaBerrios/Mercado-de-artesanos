$(document).ready(function () {
    var cont = 0 // Para que no cambie el dinero más de una vez
    const form_peso = new Intl.NumberFormat('es-CL', {
        style: 'currency',
        currency: 'CLP',
        //minimumFractionDigits: 0

    })


    $("#slc_money").click(function () {
        fetch("https://mindicador.cl/api")
            .then((res) => res.json())
            .then(data => {
                var elementos = document.getElementsByClassName("precio-producto").length;
                if (cont < 1) {
                    for (var i = 1; i <= elementos-1; i++) {
                        var posicion_dolar = '#precio_producto' + i
                        var posicion = 'precio_producto' + i
                        var valor_1 = (document.getElementById(`${posicion}`).textContent)
                        var valor = parseFloat(valor_1.replace("$", ""))
                        const precio_dolar = data.dolar.valor
                        console.log(precio_dolar, i);
                        var precio_clp_notfix = (parseFloat(precio_dolar * valor).toFixed(0))
                        const precio_clp = form_peso.format(precio_clp_notfix)
                        $(`${posicion_dolar}`).html(precio_clp)
                        console.log(precio_clp);
                    }
                    cont = cont + 1
                }
            }
            )
    })
    $("#slc_clp").click(function () {
        console.log('si');
        fetch("https://mindicador.cl/api")
            .then((res) => res.json())
            .then(data => {
                var elementos = document.getElementsByClassName("valor_dollar").length;
                for (var i = 1; i <= elementos; i++) {
                    var posicion = 'precio' + i
                    var posicion_dolar = '#precio' + i
                    var valor = parseFloat(document.getElementById(`${posicion}`).textContent)
                    var precio_dolar = data.dolar.valor
                    var precio_clp = (valor / precio_dolar).toFixed(2)
                    console.log(precio_clp)

                    $(`${posicion_dolar}`).html(precio_clp)
                }
            }
            )
    })
})