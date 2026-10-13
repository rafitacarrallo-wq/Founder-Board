# Brief para el consejo — Idea: capa de inteligencia Go-To-Market (GTM) para B2B SaaS

Este documento se basta por sí solo. Léelo entero antes de votar.

## PROBLEMA
Las empresas que venden software o servicios y tienen un motor de go-to-market real
(sobre todo SaaS B2B, y en especial las product-led / PLG) suelen tener sus datos
de GTM **repartidos en herramientas que no se hablan entre sí**: el CRM, la
analítica de producto, el billing, el marketing y el BI. Duele más en empresas
**sin equipo de datos ni de RevOps dedicado**, que acaban cosiendo los datos a mano
en hojas de cálculo. Resultado: no pueden responder con fiabilidad a las preguntas
que más mueven ingresos — de dónde vienen los leads y dónde se atascan, qué
usuarios van a activar y pagar de verdad, y cuánto cobrar. Deciden a ciegas o por
intuición, o queman tiempo y dinero cableando datos en vez de vender.

## SOLUCIÓN
Una **capa de inteligencia GTM** que se conecta a las herramientas que la empresa
ya usa, **unifica automáticamente todos esos datos en un único modelo del customer
journey** (lead → signup → activación → pago → expansión) resolviendo identidades
entre herramientas, y responde de serie a tres preguntas: (1) atribución y salud del
funnel, (2) predicción de qué cuentas van a activar y convertir, y (3) análisis de
pricing. Entrega las respuestas en **lenguaje claro y accionable usando IA**, de modo
que un fundador o un comercial no técnico obtiene **el criterio de un equipo de
datos sin montar uno ni saber SQL**.

## Contexto del fundador (importante para juzgar la viabilidad real)
- Técnico (sabe construir software), con ganas de ser muy bueno en IA/agentes.
- Recursos: **tiempo parcial y poco dinero** al arrancar. Sin equipo.
- Quiere un negocio propio y asume el riesgo; acepta que no hay proyección garantizada.

## Preguntas abiertas / datos que nadie tiene aún (no inventar)
- Competencia: el espacio está MUY poblado (CDPs y GTM/PLG analytics: Segment,
  RudderStack, Hightouch, Census, June, Pocus, Koala, Correlated, Common Room,
  HubSpot, Mixpanel/Amplitude, etc.). ¿Qué hueco real queda? → /founder-competitors.
- ¿Las empresas SIN equipo de datos de verdad pagan por esto, o es justo el
  segmento con menos presupuesto y menos capacidad de conectar sus herramientas? →
  /founder-consumer.
- Integraciones: mantener conectores con muchas herramientas de terceros es un coste
  y una fragilidad enormes (APIs que cambian). ¿Viable a tiempo parcial y sin equipo?
- Identity resolution entre herramientas es técnicamente difícil y propenso a error;
  si falla, las respuestas pierden toda credibilidad.
- Confianza: ¿un fundador actúa sobre una predicción/atribución de una IA que no
  entiende? ¿Y datos sensibles de clientes (seguridad, cumplimiento)?
- CAC y canal para vender B2B siendo un fundador solo y a tiempo parcial.

Si tu lente necesita un número que nadie tiene, nómbralo como pregunta abierta y di
qué skill lo responde. No inventes cifras.
