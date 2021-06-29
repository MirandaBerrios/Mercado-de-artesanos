$(document).ready(function () {
    fetch("https://fakestoreapi.com/products")
        .then((res) => res.json())
        .then(data => {
            try {
                for (let i = 1; i < data.length; i++) {
                    var identificar1 = document.getElementById("producto"+i).id;
                    var identificar = identificar1.replace("producto", "")
                    var title = data[identificar].title
                    var price = '$' + data[identificar].price
                    var image = data[identificar].image
                    var image_html = `<img id='producto` + identificar + `' class='imagenes_productos mx-auto d-block' 
                                    src="${data[identificar].image}" alt="${data[identificar].description}" width="100px"  heigth="150px">`
                    // $('#nombre'+i).html()
                    // $('#precio'+i).html(title)
                    // $('#imagen'+i).html(price)
    
                    $('#nombre_producto'+i).html(title)
                    $('#precio_producto'+i).html(price)
                    $('#imagen_producto'+i).html(image_html)
                }
            
            } catch (e) {
                console.log() // limpoiar de errores la consola
            }
        })
})