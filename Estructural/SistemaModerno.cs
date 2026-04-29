using System;

namespace Codigo_Limpio.Estructural
{
    public class SistemaModerno : AdapterInterface
    {
        public string ProcesarDatos(string dato)
        {
            return $"[SISTEMA MODERNO] Procesando datos actuales: {dato}";
        }
    }
}