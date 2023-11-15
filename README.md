<div align="center">
  <h1>Mutants ☢️</h1>
  <h3>Germán Geredus</h3>
  <p>Legajo: 51550</p><br>
  <div>
    <a href="https://www.linkedin.com/in/germangere">
      <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin">
    </a>
    <a href="mailto:germangere@gmail.com">
      <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
    </a>
    <a href="https://wa.me/+5492615793559">
      <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="Whatsapp">
    </a>
  </div>
</div>

## Acerca del proyecto
Este es el trabajo práctico integrador correspondiente a la materia Programación I incluida en la Tecnicatura Universitaria en Programación, de la Universidad Tecnológica Nacional.

Magneto nos pidió que le ayudemos en su reclutamiento de mutantes para luchar contra los X-MEN, por lo tanto solicitó que desarrollemos un programa que detecte si un humano es mutante, basándonos en el análisis de su cadena ADN.

El programa debe contener una función que reciba el ADN y analice los datos ingresados. Las cadenas de ADN están formadas por 6 grupos de 6 letras que sólo pueden ser A, T, C, G. Si hay más de una secuencia de cuatro letras iguales, ya sea de forma oblicua, horizontal o vertical, significa que el ADN corresponde a un mutante. El resultado debe ser mostrado al usuario.

## Cómo lo resolví
Mi solución consiste en realizar la función de detección de manera eficiente, para favorecer la rapidez en la evaluación del ADN. Esto pude lograrlo en primera instancia validando que los datos ingresados sean correctos, accediendo a la menor cantidad de datos posibles en cada evaluación, como así también retornando el resultado la mínima vez que se cumplan las condiciones establecidas.

El programa presenta un menú de consola, en la que el usuario puede probar el desarrollo con ejemplos establecidos para ADN mutante, ADN humano y ADN inválido, o bien, ingresar una cadena de ADN personalizada. Una vez validada la información y analizado el ADN, el programa muestra el resultado correspondiente y ofrece al usuario las opciones del menú principal.


## Cómo correr el programa
Para ejecutar el programa se pueden seguir los siguientes pasos:
- Instalar Python 3.11
- Descargar los archivos de este repositorio
- Descomprimir los archivos en una carpeta
- Abrir una consola de ejecución en la carpeta donde se encuentran los archivos
- Ejecutar el siguiente comando:
    ```
    python main.py
    ```
- Seguir las instrucciones del programa