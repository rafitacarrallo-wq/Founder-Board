# Founder Board

Proyecto para **testear una idea de negocio antes de lanzarla**, usando el pack
de 11 skills *founder* para Claude Code.

La idea: poner el negocio delante de un consejo de administración, una scout de
competidores, un panel de 100 compradores simulados, un CFO y más — y salir con
un plan de negocio completo y un veredicto calculado a partir de los números
(Rentable / Todavía no / Incompleto), **antes** de gastar dinero averiguándolo
por las malas.

## Instalar como plugin (usarlo en cualquier repo)

Este repo es a la vez un **marketplace** y un **plugin** de Claude Code. Instálalo
una vez y las 11 skills quedan disponibles en cualquier sesión y cualquier carpeta,
no solo dentro de este repo:

```
/plugin marketplace add rafitacarrallo-wq/Founder-Board
/plugin install founder@founder-board
```

En Claude Code 2.1.275 o posterior es un solo paso:

```
/plugin install founder --marketplace rafitacarrallo-wq/Founder-Board
```

## Las 11 skills

Van en `skills/`. Como plugin, los comandos quedan bajo el namespace `/founder:`
(escribe `/founder` y el autocompletado te las lista todas):

| comando | rol | qué hace |
| --- | --- | --- |
| `/founder:founder-board` | Consejo | Tres miembros, cada uno aplicando un framework publicado (Ofertas, Monopolio, Producto), puntúan la idea, nombran lo que la mataría y votan. |
| `/founder:founder-competitors` | Scout de competidores | Mapea competidores directos, indirectos y sustitutos desde fuentes públicas, con precios, posicionamiento y quejas de clientes. |
| `/founder:founder-consumer` | Panel de consumidores | Genera 100 compradores simulados de tu cliente objetivo y ve quién compra, quién no y por qué. |
| `/founder:founder-pricing` | Estrategia de precios | Convierte las respuestas del panel en un rango de precio aceptable y recomienda qué probar. |
| `/founder:founder-offer` | Arquitecto de oferta | Construye la oferta (bonos, garantía, urgencia real, nombre) que responde a las objeciones y la re-testea. |
| `/founder:founder-cfo` | CFO | Economía unitaria: margen real, punto de equilibrio, año 1 mes a mes, caja necesaria, payback. |
| `/founder:founder-marketing` | Dir. de marketing | Posicionamiento, canales, campaña de 30 días, 10 ganchos y cuánto pagar por cliente. |
| `/founder:founder-brand` | Diseño de marca | Nombres (con checks de marca/dominio/handle), voz, promesa y brief del look. |
| `/founder:founder-ops` | Operaciones | Proveedores, personal, rutinas de día uno, herramientas, permisos y registro de riesgos. |
| `/founder:founder-launch` | Lanzamiento | Un test real barato primero, cuenta atrás con fechas, run sheet del día y primeros 30 días. |
| `/founder:founder-plan` | Plan de negocio | Compila todo en un plan con veredicto calculado desde los números. |

También siguen funcionando por lenguaje natural ("testea mi idea", "haz los
números"): Claude invoca la skill correcta por su descripción, estés donde estés.

## Orden de uso

Cada skill lee lo que escribieron las anteriores en la carpeta `founder/`:

```
board → competitors → consumer → pricing → offer → cfo → marketing → brand → ops → launch → plan
```

También puedes lanzar cualquiera por separado. `/founder:founder-consumer --quick`
sobre una idea que solo estás pensando es una buena forma de ver si merece la pena.

## Idioma

Las instrucciones de las skills (`SKILL.md`) están en inglés (son prompts
afinados, no se tocan). Los **resultados** se generan en **español** por defecto.
Si al validar el mercado resulta ser anglosajón/global, marca y marketing pasan
a inglés.

## Las herramientas

Cuatro scripts de Python (solo librería estándar, Python 3.8+, nada que instalar):

```bash
python3 skills/founder-cfo/unit_economics.py founder/numbers.json --out founder/cfo.md
python3 skills/founder-consumer/panel.py init --customer founder/customer.json --pitch founder/pitch.md
python3 skills/founder-pricing/van_westendorp.py founder/panel/answers --price 6.50
python3 skills/founder-plan/compile.py --dir founder
```

> Nota: las skills llaman a estos scripts con `${CLAUDE_SKILL_DIR}` (la carpeta de
> cada skill), así que funcionan igual estén en `skills/` dentro del repo o
> instaladas como plugin en cualquier otro sitio. Las rutas de arriba son solo para
> ejecutarlos a mano desde la raíz del repo.

## Crédito

El pack *founder-skill* es de Jake Schincariol — https://github.com/Jakeschincariol/founder-skill
(licencia MIT). Este repo lo usa para validar un negocio propio.
