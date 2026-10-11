# Founder Board

Proyecto para **testear una idea de negocio antes de lanzarla**, usando el pack
de 11 skills *founder* para Claude Code.

La idea: poner el negocio delante de un consejo de administración, una scout de
competidores, un panel de 100 compradores simulados, un CFO y más — y salir con
un plan de negocio completo y un veredicto calculado a partir de los números
(Rentable / Todavía no / Incompleto), **antes** de gastar dinero averiguándolo
por las malas.

## Las 11 skills

Instaladas en `.claude/skills/`. Se usan como comandos en Claude Code:

| comando | rol | qué hace |
| --- | --- | --- |
| `/founder-board` | Consejo | Tres miembros, cada uno aplicando un framework publicado (Ofertas, Monopolio, Producto), puntúan la idea, nombran lo que la mataría y votan. |
| `/founder-competitors` | Scout de competidores | Mapea competidores directos, indirectos y sustitutos desde fuentes públicas, con precios, posicionamiento y quejas de clientes. |
| `/founder-consumer` | Panel de consumidores | Genera 100 compradores simulados de tu cliente objetivo y ve quién compra, quién no y por qué. |
| `/founder-pricing` | Estrategia de precios | Convierte las respuestas del panel en un rango de precio aceptable y recomienda qué probar. |
| `/founder-offer` | Arquitecto de oferta | Construye la oferta (bonos, garantía, urgencia real, nombre) que responde a las objeciones y la re-testea. |
| `/founder-cfo` | CFO | Economía unitaria: margen real, punto de equilibrio, año 1 mes a mes, caja necesaria, payback. |
| `/founder-marketing` | Dir. de marketing | Posicionamiento, canales, campaña de 30 días, 10 ganchos y cuánto pagar por cliente. |
| `/founder-brand` | Diseño de marca | Nombres (con checks de marca/dominio/handle), voz, promesa y brief del look. |
| `/founder-ops` | Operaciones | Proveedores, personal, rutinas de día uno, herramientas, permisos y registro de riesgos. |
| `/founder-launch` | Lanzamiento | Un test real barato primero, cuenta atrás con fechas, run sheet del día y primeros 30 días. |
| `/founder-plan` | Plan de negocio | Compila todo en un plan con veredicto calculado desde los números. |

## Orden de uso

Cada skill lee lo que escribieron las anteriores en la carpeta `founder/`:

```
board → competitors → consumer → pricing → offer → cfo → marketing → brand → ops → launch → plan
```

También puedes lanzar cualquiera por separado. `/founder-consumer --quick` sobre
una idea que solo estás pensando es una buena forma de ver si merece la pena.

## Idioma

Las instrucciones de las skills (`SKILL.md`) están en inglés (son prompts
afinados, no se tocan). Los **resultados** se generan en **español** por defecto.
Si al validar el mercado resulta ser anglosajón/global, marca y marketing pasan
a inglés.

## Las herramientas

Cuatro scripts de Python (solo librería estándar, Python 3.8+, nada que instalar):

```bash
python3 .claude/skills/founder-cfo/unit_economics.py founder/numbers.json --out founder/cfo.md
python3 .claude/skills/founder-consumer/panel.py init --customer founder/customer.json --pitch founder/pitch.md
python3 .claude/skills/founder-pricing/van_westendorp.py founder/panel/answers --price 6.50
python3 .claude/skills/founder-plan/compile.py --dir founder
```

## Crédito

El pack *founder-skill* es de Jake Schincariol — https://github.com/Jakeschincariol/founder-skill
(licencia MIT). Este repo lo usa para validar un negocio propio.
