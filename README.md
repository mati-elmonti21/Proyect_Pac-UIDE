

Proyecto integrador de primer nivel · Lógica de Programación · UIDE · Paralelo [C]

Juego por turnos para dos jugadores con modo local y, más adelante, modo multijugador cliente-servidor en red LAN.

## Integrantes

- Martin Montaño
- Edgar Pilco

## Cómo ejecutarlo

Requiere Python 3. Desde la carpeta del repositorio:
## Estructura del repositorio

| Archivo | Qué hace | Estado |
|---|---|---|
| `juego.py` | Menú que se repite hasta «Salir» (parte de DF1) | Terminado |
| `game_logic.py` | Validación de la jugada (DF2) y fin de la partida (DF3) | Terminado |
| `server.py` | Estructura inicial del servidor correspondiente al Jugador 1 | Iniciado |
| `client.py` | Estructura del cliente correspondiente al Jugador 2 | Iniciado |
| `diseno/` | Diagramas `.rap` de la Fase 2 | Subido |

## Del diseño al código

| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió al traducirlo |
|---|---|---|
| DF1 Partida completa (solo el menú) | [`juego.py`, líneas …] | El menú diseñado en RAPTOR se tradujo a instrucciones de Python para mostrar las opciones y permitir la interacción del usuario. |
| DF2 Validación de la jugada | [`game_logic.py`, líneas …] | Las decisiones del diagrama se implementaron mediante condiciones en Python para comprobar si una jugada es válida. |
| DF3 Fin de la partida | [`game_logic.py`, líneas …] | Las condiciones del diagrama se implementaron en Python para comprobar cuándo termina la partida y determinar al ganador. |

## Video explicativo

[Enlace al video] (máximo 5 minutos: el menú, la validación con una jugada inválida, el fin de la partida y cómo tradujimos un diagrama a código).

## Licencia

Este proyecto se distribuye bajo la licencia MIT. El texto completo está en el archivo `LICENSE`.

## Declaración de autoría

Declaramos que el código de este repositorio fue escrito por los integrantes del equipo, salvo los recursos citados en la sección «Créditos».

## Créditos

| Recurso (código, librería, imagen…) | Autor o fuente | Dónde se usa | Licencia |
|---|---|---|---|
| Python | Python Software Foundation | Desarrollo del videojuego | PSF License |

### Uso de IA

| Herramienta | Para qué la usamos | Qué revisamos o cambiamos nosotros |
|---|---|---|
