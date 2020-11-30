/* define metodo con distintos tipos de variables para js*/
function ver()
{
    //definicion de variables
  var nombre='juan';
  var edad=10;
  var altura=1.80;
  var soltero=true;
  //document.write hace referencia a una pagina donde mostrará los valores de las variables
  document.write('El nombre es: ' + nombre);
  document.write('<br>');
  document.write('La edad es: ' + edad);
  document.write('<br>');
  document.write('La altura es: ' + altura);
  document.write('<br>');
  document.write('El estado civil es: '+ soltero);
}
function Ingresar()
{
    var nom;
    var edad;
    nom = prompt('Ingrese su nombre');
    edad = prompt('Ingrese su edad');
    document.write('Hola ' + nom + ' tu edad es: '+ edad);
  
  }

  function Sumita()
{
  var valor1, valor2;
  valor1 = prompt('Ingrese un numero: ');
  valor2 = prompt('Ingrese otro numero: ');
  var suma = parseInt(valor1) + parseInt(valor2);
  alert('La suma de los numeros es: '+ suma);
}

/*definir metodo que permita ingresar dos números, mostrar en un document lo siguiente: 
 a. la multplicacion de ambos números
 b. el doble del primer número
 c. el cuadrado del segundo número*/
 function Calculos()
 {
   var valor1, valor2;
   valor1 = prompt('Ingrese un numero: ');
   valor2 = prompt('Ingrese otro numero: ');
   var multi = parseInt(valor1) * parseInt(valor2);
   var doblenum = parseInt(valor1) * 2;
   var cuadrado = parseInt(valor1)**2;
   alert('La multiplicacion de los numeros es: '+ multi);
   alert('el doble del segundo numero es: '+ doblenum);
   alert('La multiplicacion de los numeros es: '+ cuadrado);
 }

 function MayorEdad()
 {
 var edad;
 var nom;

nom = prompt('Ingrese un nombre');
edad=prompt('Ingrese una edad')

if (parseInt(edad) >=18)
{
  alert ('Ustred es mayor de edad')
}
else if(parseInt<=17)
{
  alert ('Ustred es menor de edad')
}
 }

 /*ingresar un numero y mostrar mensaje que indique:
    Si el numero es positivo y par
    Si el numero es positivo e impar 
    Si el numero es negativo y par 
    Si el numero es negativo e impar 
    Si el numero es igual a cero 
    */
 function Verifica()
 {
  var num;
  num = prompt('Ingrese un numero');

  if (parseInt(num)<0 && parseInt(num)%2==0)
  {
    alert ('el numero ingresado es negativo e impar');
  }
  else if (parseInt(num)>0 && parseInt(num)%1==0)
  {
    alert ('el numero ingresado es positivo e impar');
  }
  if (parseInt(num)<0 && parseInt(num)%2==1)
  {
    alert ('el numero ingresado es negativo y par');
  }
  else if (parseInt(num)>0 && parseInt(num)%1==1)
  {
    alert ('el numero ingresado es positivo y par');
  }
  else if (parseInt(num)==0)
  {
  alert ('el numero ingresado es 0');
  }
 }

 function Ciclos()
 {
    //ciclo while
     var num, x, suma=0; 
     x=1; 
     while(x<=10)
     {
        num=prompt('Digite un numero');
        suma = suma + parseInt(num);
        x++; 
     }
     
     alert(' Con ciclo while La suma de los 10 números es: '+ suma);  
 
     //ciclo for 
     
     suma=0;
     for(x=1; x<=10; x++)
     {
       num=prompt('Digite un numero');
       suma = suma + parseInt(num);
     }
     
     alert(' Con ciclo for La suma de los 10 números es: '+ suma);  
 
 }

