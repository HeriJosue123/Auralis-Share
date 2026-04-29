using System;

namespace Codigo_Limpio.Estructural
{
    // Hereda de la interfaz para que el sistema crea que es moderno
    public class Adaptador : AdapterInterface
    {
        // Variable de solo lectura para el sistema viejo
        private readonly SistemaLegado _sistemaViejo;

        // Constructor que recibe el sistema viejo
        public Adaptador(SistemaLegado sistemaViejo)
        {
            _sistemaViejo = sistemaViejo;
        }

        // Cumple la regla moderna, pero por dentro llama al método viejo
        public string ProcesarDatos(string dato)
        {
            return _sistemaViejo.ProcesarAntiguo(dato);
        }
    }
}