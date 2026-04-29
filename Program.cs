using System;
using Codigo_Limpio.Estructural; // Importamos la carpeta donde están tus clases

namespace Codigo_Limpio
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Prueba Patron......................Adapter...............................");

            // 1. Usando el sistema moderno normalmente
            SistemaModerno moderno = new SistemaModerno();
            Console.WriteLine(moderno.ProcesarDatos("Información en la nube"));

            Console.WriteLine("\n--- INICIANDO INTEGRACIÓN ---");

            // 2. Aquí está tu tarea: Simular integración de sistema legado con moderno
            SistemaLegado legado = new SistemaLegado();

            // Metemos el sistema viejo adentro del adaptador
            AdapterInterface adaptador = new Adaptador(legado);

            // Lo usamos como si fuera moderno
            Console.WriteLine(adaptador.ProcesarDatos("Información en disquete de 1995"));

            Console.ReadLine(); // Pausa la consola para que puedas ver el resultado
        }
    }
}