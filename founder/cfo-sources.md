# Fuentes y supuestos de los números — Demo-to-Deal

Todas las cifras en **euros**. Marcadas por origen: [dato] del usuario/factura,
[público] de una fuente pública verificable, [estimación] mía con razonamiento.
**Nada aquí está confirmado con cotizaciones reales todavía** — es un modelo para
decidir, no cuentas cerradas. Hay que validar cada línea con un presupuesto real
antes de comprometer dinero (lo pide `/founder-ops`).

## Precio
- **9.500 €/sprint** — [estimación] ancla a testear, respaldada por Van Westendorp
  (rango 2.480-11.956 €, ver `pricing.md`) y por el comparable Trebal & Chowsky
  (~15.000 $, `competitors.md`).

## Coste variable por sprint (~1.013 €)
- Comisión de pago **238 €** — [público] ~2,5% de 9.500 €, típico de Stripe/pasarela
  para transferencia/tarjeta B2B. Confirmar con la pasarela elegida.
- Diseño freelance del entregable **260 €** — [estimación] maquetación del deck/
  narrativa por un freelance; ~1 jornada. Confirmar con presupuesto.
- Créditos de grabación/transcripción **40 €** — [estimación] prorrateo mensual de
  una herramienta tipo Fathom/Otter/tl;dv por sprint.
- Comisión de referido/partner (blended ~5%) **475 €** — [estimación] media ponderada:
  no todos los deals pagan comisión; los que vienen por VC/partner pueden llevar
  10-20%. Ajustar cuando se cierre el acuerdo de canal.

## Costes fijos mensuales (~520 €)
- Stack software **260 €** — [estimación] CRM + LinkedIn Sales Navigator (~100 €/mes
  [público]) + scheduling + email + grabación. Confirmar con los planes elegidos.
- Gestoría + seguro RC profesional **200 €** — [estimación] gestoría de autónomo en
  España (~60-100 €/mes [público]) + seguro de responsabilidad civil profesional.
  Confirmar con gestoría y aseguradora.
- Web/hosting/suscripciones varias **60 €** — [estimación].

## Arranque (una vez, ~5.500 €)
- Marca + web **2.500 €** — [estimación]; ver `/founder-brand`.
- Constitución/legal + contratos tipo **800 €** — [estimación]; depende de autónomo
  vs. sociedad (consultar gestor).
- Contenido + primer caso de estudio **1.200 €** — [estimación].
- Sales Navigator anual + alta de herramientas **500 €** — [estimación].
- Colchón inicial **500 €** — [estimación].

## Volumen
- `capacity_per_day`=2, `plan_per_day`=1,5, `ramp_per_day`=[0,1,1,1,2,2,2,2,2,2,2,2]
  — [estimación] sprints al mes (con `days_per_month`=1). La rampa arranca en 0
  (mes de prospección/montaje) y sube a la capacidad de una persona.
- **Chequeo con el panel:** el panel compró al 8% en frío y a precio pleno. La rampa
  de 1-2 sprints/mes **asume** que el canal de referencias de VCs + la cohorte
  fundadora + los casos reales elevan la conversión muy por encima de ese 8%. Si no
  se generan casos, la rampa real será más lenta (ver what-if de volumen 0,5 en
  `cfo.md`): es el supuesto más frágil del modelo.

> Pendiente para `/founder-ops`: cotizaciones reales de gestoría, seguro RC, pasarela
> de pago y herramientas; y cerrar el % real de comisión de partner.
