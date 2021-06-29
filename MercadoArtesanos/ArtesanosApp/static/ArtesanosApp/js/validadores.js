$(document).ready(function () {

    $("#btnEnviar").click(function () {
        var contra = "";
        contra = $("#contraseña").val();

        var recontra = "";
        recontra = $("#recontraseña").val();

        if (contra.length < 5) {
            document.getElementById("mensajeContra").classList.remove('desactive')
            document.getElementById("mensajeContra").classList.add('activate')
            return false; //impide que el formulario se envie de forma erronea
        } else {
            document.getElementById("mensajeContra").classList.add('desactive')

        }

        if (contra !== recontra) {
            document.getElementById("mensajeRecontra").classList.remove('desactive') //Removemos una clase 
            document.getElementById("mensajeRecontra").classList.add('activate') //Agregamos una clase 

        } else {
            document.getElementById("mensajeRecontra").classList.add('desactive')
        }
    })
});


//load regiones, pronvincias y comunas
$(document).ready(function () {
    fetch('https://apis.digital.gob.cl/dpa/regiones')
        .then((respuesta) => respuesta.json())
        .then(data => {
            //load regiones
            for (var i = 0; i < 16; i++) {
                var codigoRegion = data[i].codigo
                var nombreRegion = data[i].nombre //json.strinify se ocupa para convertir un json a string
                var Reg1 = JSON.stringify(nombreRegion)
                var Reg = Reg1.replace('.', '')
                var claseRegion = Reg.replace(/\s/g, '') //(/\s/g,'') se utiliza para quitar los espacios de un string
                var cRegion = "<option id = " + codigoRegion + " class =" + claseRegion + " " + ">" + nombreRegion + "</option>"
                document.getElementById("Regiones").innerHTML += cRegion // innerhtml += agrega la variable al codigo html 
            }

            // load provincias
            $("select#Regiones").click(function () {
                $("#Provincias option").remove()  // el remove se ocupara para elimnar los option del select
                $("#Comunas option").remove()  // el remove se ocupara para elimnar los option del select
                var alfa = document.getElementById("Regiones").value
                var gama = alfa.replace('.', '')
                var beta = gama.replace(/\s/g, '')
                //var zeta = document.querySelectorAll("id."+beta)
                var zeta = $('.' + beta).attr('id') // con esto sacamos el id de la clase que estamos recolectando de beta
                var codeRegion = document.getElementById(zeta).id



                fetch('https://apis.digital.gob.cl/dpa/regiones/' + codeRegion + '/provincias')
                    .then((res) => res.json())
                    .then(data => {
                        for (var i = 0; i < data.length; i++) {
                            var nombreProv = data[i].nombre
                            var codeProv = data[i].codigo
                            var Prov = JSON.stringify(nombreProv)
                            var claseProvincias = Prov.replace(/\s/g, '')
                            var cProvincias = "<option id =" + codeProv + " class =" + claseProvincias + " " + ">" + nombreProv + "</option>"
                            document.getElementById("Provincias").innerHTML += cProvincias
                        }
                    })
            })
            //Load comunas
            $("select#Provincias").click(function () {
                $("#Comunas option").remove()  // el remove se ocupara para elimnar los option del select

                var alfaProv = document.getElementById("Provincias").value
                var gamaProv = alfaProv.replace('.', '')
                var betaProv = gamaProv.replace(/\s/g, '') // white space replace for nothing
                var zetaProv = $('.' + betaProv).attr('id') // con esto sacamos el id de la clase que estamos recolectando de beta
                var codeProv = document.getElementById(zetaProv).id

                var alfaReg = document.getElementById("Regiones").value
                var gamaReg = alfaReg.replace('.', '')
                var betaReg = gamaReg.replace(/\s/g, '')
                var zetaReg = $('.' + betaReg).attr('id') // con esto sacamos el id de la clase que estamos recolectando de beta
                var codeRegion = document.getElementById(zetaReg).id

                fetch('https://apis.digital.gob.cl/dpa/regiones/' + codeRegion + '/provincias/' + codeProv + '/comunas')
                    .then((res) => res.json())
                    .then(data => {
                        for (let i = 0; i < data.length; i++) {
                            var nombreCom = data[i].nombre
                            var codigoCom = data[i].codigo
                            var Com = JSON.stringify(nombreCom)
                            var claseCom = Com.replace(/\s/g, '')
                            var cCom = "<option id =" + codigoCom + " class =" + claseCom + " " + ">" + nombreCom + "</option>"
                            document.getElementById("Comunas").innerHTML += cCom
                        }
                    })
            })
        })
})

