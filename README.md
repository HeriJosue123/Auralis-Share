# Auralis Share

> Transferencia y administración de archivos entre Android y Windows, directamente entre tus dispositivos.

## 🚧 Estado del proyecto

**En desarrollo — Fase 0 / planificación**

Auralis Share es un proyecto experimental y educativo creado para desarrollar una alternativa propia a herramientas de transferencia de archivos entre dispositivos.

La meta es construir una aplicación real, mantenible y segura que permita mover archivos grandes entre Android y Windows sin depender inicialmente de servicios de almacenamiento en la nube.

## 💡 ¿Qué es Auralis Share?

Auralis Share busca conectar un teléfono Android y una PC Windows dentro de la misma red local para que puedan comunicarse directamente.

Por ejemplo:

```
📱 Android
    ↕
  Wi-Fi
    ↕
💻 Windows
```

La idea es poder:

- 📤 Enviar archivos de Android a Windows.
- 📥 Enviar archivos de Windows a Android.
- 📁 Transferir múltiples archivos y carpetas.
- 🚀 Transferir archivos de varios GB mediante streaming.
- 🔄 Reanudar transferencias interrumpidas.
- 📊 Mostrar progreso, velocidad y estado.
- 🔐 Autenticar y autorizar dispositivos.
- 🗂️ Explorar posteriormente el almacenamiento accesible del Android desde Windows.

## 🎯 Objetivo

Crear una solución propia que priorice:

- Transferencias directas por LAN.
- Buen rendimiento con archivos grandes.
- Seguridad.
- Control del usuario.
- Arquitectura modular.
- Compatibilidad con las restricciones modernas de Android.
- Posibilidad de ampliar el proyecto en el futuro.

La primera versión **no dependerá de Internet ni de almacenamiento en la nube** para realizar las transferencias locales.

## 🧩 Arquitectura prevista

La arquitectura se desarrollará por etapas y podrá evolucionar durante el proyecto.

### Android

- Kotlin
- Jetpack Compose
- APIs nativas de Android
- Foreground Services para transferencias prolongadas

### Windows

- C#
- .NET
- Avalonia UI

### Comunicación

Inicialmente:

- mDNS / ZeroConf para descubrimiento en la red local.
- HTTP para comunicación y transferencia.
- WebSockets cuando sean necesarios para eventos y estado en tiempo real.

### Archivos grandes

Las transferencias utilizarán streaming para evitar cargar archivos completos en memoria.

Se contempla soporte para:

- HTTP Range
- Reanudación
- Transferencias parciales
- Verificación de integridad mediante SHA-256

## 🔐 Seguridad

La detección de un dispositivo no significa que este tenga acceso a los archivos.

El flujo previsto será:

```
DESCUBRIR
   ↓
IDENTIFICAR
   ↓
SOLICITAR CONEXIÓN
   ↓
AUTENTICAR
   ↓
AUTORIZAR
   ↓
CONECTAR
```

Se contempla posteriormente el uso de:

- PIN de emparejamiento.
- Códigos QR.
- Dispositivos de confianza.
- Tokens de sesión.
- Comunicación cifrada mediante TLS.

## 🗂️ Explorador remoto

Una de las funciones principales previstas para futuras fases será permitir que Windows explore y administre el almacenamiento accesible del Android.

Ejemplo:

```
📱 Android
├── 📁 DCIM
│   └── 📁 Camera
├── 📁 Download
├── 📁 Pictures
├── 📁 Music
└── 📁 Documents
```

Las operaciones disponibles dependerán de las APIs y permisos permitidos por las versiones modernas de Android.

## 🛠️ Desarrollo por fases

El proyecto se construirá progresivamente:

1. **Conexión básica y Ping/Pong**
   - Crear las aplicaciones base.
   - Descubrir dispositivos en LAN.
   - Levantar servidores locales.
   - Comprobar comunicación Android ↔ Windows.

2. **Transferencia de archivos**
   - Streaming.
   - Progreso.
   - Velocidad.
   - Cancelación.
   - Primeras pruebas con archivos grandes.

3. **Reanudación**
   - Transferencias parciales.
   - HTTP Range.
   - Recuperación después de cortes.

4. **Seguridad y emparejamiento**
   - Autenticación.
   - PIN/QR.
   - Dispositivos confiables.
   - TLS.

5. **Múltiples archivos y carpetas**
   - Colas de transferencia.
   - Estructuras de carpetas.
   - Transferencias por lotes.

6. **Explorador remoto**
   - Navegación.
   - Descarga.
   - Subida.
   - Operaciones de archivos permitidas por Android.

7. **Pulido y distribución**
   - Pruebas con dispositivos reales.
   - Optimización.
   - APK Android.
   - Aplicación Windows.

8. **Futuro**
   - Conexiones fuera de la red local.
   - Linux/macOS.
   - Funciones adicionales de sincronización.

## 📌 Principios del proyecto

Auralis Share seguirá algunas reglas:

- No implementar todo de golpe.
- Una fase a la vez.
- Probar cada fase antes de continuar.
- Priorizar dispositivos reales sobre simulaciones.
- Evitar dependencias innecesarias.
- No introducir servicios externos sin una razón clara.
- Mantener separadas la interfaz, red, transferencia y lógica de negocio.
- No sacrificar seguridad por comodidad.

## 📱💻 Plataformas iniciales

| Plataforma | Tecnología | Estado |
|---|---|---|
| Android | Kotlin + Jetpack Compose | 🚧 Planificado |
| Windows | C# + .NET + Avalonia | 🚧 Planificado |

## ⚠️ Aviso

Auralis Share se encuentra actualmente en desarrollo.

Las tecnologías, protocolos y decisiones descritas en este README representan la arquitectura inicial y pueden cambiar conforme se realicen pruebas y validaciones.

---

**Auralis Share** — De dispositivo a dispositivo. Sin nube. Bajo nuestro control. 🔥
