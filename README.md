# Proyect_Pac-UIDE
<!--
Plantilla del README.md · Proyecto integrador · Fase 3 (Lógica de Programación)
Copien este archivo en la raíz del repositorio con el nombre README.md, completen
los textos entre
corchetes y borren estos comentarios. Los ejemplos usan el dominó solo como guía.
-->
# [Nombre del juego]
Proyecto integrador de primer nivel · Lógica de Programación · UIDE · Paralelo [X]
Juego por turnos para dos jugadores con modo local y, más adelante, modo
multijugador cliente-servidor en red LAN.
## Integrantes
- [Nombre y apellido]
- [Nombre y apellido]
- [Nombre y apellido]
## Cómo ejecutarlo
Requiere Python 3. Desde la carpeta del repositorio:
```
python juego.py (menú)
python game_logic.py (validación de la jugada y fin de la partida)
```
## Estructura del repositorio
| Archivo | Qué hace | Estado |
|---|---|---|
| `juego.py` | [Menú que se repite hasta «Salir» (parte de DF1)] | [Terminado /
Iniciado] |
| `game_logic.py` | [Validación de la jugada (DF2) y fin de la partida (DF3)] |
[Terminado / Iniciado] |
| `server.py` | [Comentario con lo que hará el servidor (Jugador 1)] | [Pendiente]
|
| `client.py` | [Comentario con lo que hará el cliente (Jugador 2)] | [Pendiente] |
| `diseno/` | Diagramas `.rap` de la Fase 2 | [Subido] |
## Del diseño al código
| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió al traducirlo |
|---|---|---|
| DF1 Partida completa (solo el menú) | [`juego.py`, líneas …] | [...] |
| DF2 Validación de la jugada | [`game_logic.py`, líneas …] | [...] |
| DF3 Fin de la partida | [`game_logic.py`, líneas …] | [...] |
<!-- El bucle de turnos de DF1 (la partida completa) se programa en la Fase 4. -->
<!-- Ejemplo (dominó): DF2 · game_logic.py, líneas 20-31 · El Loop de RAPTOR pasó a
ser un while que se repite
mientras el número de ficha no esté en la mano del jugador o no encaje en un
extremo. -->
## Video explicativo
[Enlace al video] (máximo 5 minutos: el menú, la validación con una jugada
inválida, el fin de la partida y cómo
tradujimos un diagrama a código).
## Licencia
Este proyecto se distribuye bajo la licencia [MIT]. El texto completo está en el
archivo `LICENSE`.
## Declaración de autoría
Declaramos que el código de este repositorio fue escrito por los integrantes del
equipo, salvo los recursos
citados en la sección «Créditos».
## Créditos
| Recurso (código, librería, imagen…) | Autor o fuente | Dónde se usa | Licencia |
|---|---|---|---|
| [...] | [...] | [...] | [...] |
### Uso de IA
<!-- Si no usaron IA, escriban: «No se usaron herramientas de IA». -->
| Herramienta | Para qué la usamos | Qué revisamos o cambiamos nosotros |
|---|---|---|
| [...
