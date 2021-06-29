$(document).ready(function(){
    $('.min_product[id]').click(function(){
        var x = $(this).attr('id')
        var id_producto = parseInt(x.replace('producto',''))
        const PRODCUTO_ID = id_producto
        localStorage.setItem("ID_PRODUCTO",PRODCUTO_ID)
        
    })
    var id_producto = localStorage.getItem("ID_PRODUCTO")
    fetch("https://fakestoreapi.com/products")
        .then((res) => res.json())
        .then(data=>{
            console.log(id_producto+" :)");
            var id_local = localStorage.getItem("ID_PRODUCTO")
            var title = data[id_local].title
            var price = data[id_local].price
            var description = data[id_local].description
            var image = data[id_local].image
            var image_html = `<img id='producto` + id_local + `' class='imagenes_productos mx-auto d-block' 
                            src="${data[id_local].image}" alt="${data[id_local].description}" width="200px"  heigth="300px">`
                    
            $('#titulo_producto').html(title)
            $("#precio_producto1").html('$ '+price)
            $("#descripcion_titulo").html(title)
            $("#descripcion_producto").html(description)
            $('#imagen_producto').html(image_html)
        })
})

