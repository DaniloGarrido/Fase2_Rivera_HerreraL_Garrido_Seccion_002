window.onload = function lblprecio()
{  var precioferta1=40000;
    var precioferta2=67000;
    var precioferta3=60000;
    var precioferta4=12000;
    var precioferta5=150000;
    var precioferta6=74000;
   

  document.getElementById('lbloferta1').innerHTML='Precio: $' + Intl.NumberFormat('es-CL').format(precioferta1);
  document.getElementById('lbloferta2').innerHTML='Precio: $' + Intl.NumberFormat('es-CL').format(precioferta2);
  document.getElementById('lbloferta3').innerHTML='Precio: $' + Intl.NumberFormat('es-CL').format(precioferta3);
  document.getElementById('lbloferta4').innerHTML='Precio: $' + Intl.NumberFormat('es-CL').format(precioferta4);
  document.getElementById('lbloferta5').innerHTML='Precio: $' + Intl.NumberFormat('es-CL').format(precioferta5);
  document.getElementById('lbloferta6').innerHTML='Precio: $' + Intl.NumberFormat('es-CL').format(precioferta6);



}
window.onload = function lblcarrusel(){
  var promocion=59900;
  var promocion2=27500;
  var promocion3=37900;

  document.getElementById('lbloferta7').innerHTML='Precio: $' + Intl.NumberFormat('es-CL').format(promocion);
  document.getElementById('lbloferta8').innerHTML='Precio: $' + Intl.NumberFormat('es-CL').format(promocion2);
  document.getElementById('lbloferta9').innerHTML='Precio: $' + Intl.NumberFormat('es-CL').format(promocion3);
  alert('hola')

}
function cuestionario(){
  alert('Solicitud ingresada')

}