$(document).ready(function(){

    var cont = 0
    const form_peso = new Intl.NumberFormat('es-CL', {
        style: 'currency',
        currency: 'CLP',
        //minimumFractionDigits: 0

    })

    $("#slc_money1").click(function () {
        fetch("https://mindicador.cl/api")
        .then((res) => res.json())
        .then(data => {
            if (cont < 1) {
                var posicion_dolar = '#precio_producto1' 
                var posicion = 'precio_producto1' 
                var valor_1 = (document.getElementById(`${posicion}`).textContent)
                var valor = parseFloat(valor_1.replace("$", ""))
                const precio_dolar = data.dolar.valor
                var precio_clp_notfix = (parseFloat(precio_dolar * valor).toFixed(0))
                const precio_clp = form_peso.format(precio_clp_notfix)
                
                $(`${posicion_dolar}`).html(precio_clp)
                
                cont = cont + 1
            }
        }
        )
    })
})