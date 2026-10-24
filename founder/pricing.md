# Precios — Demo-to-Deal (nombre de trabajo)

> Las respuestas de precio son de **compradores simulados**: sirven para elegir
> qué testear con compradores reales, no como prueba. El margen viene del tool del
> CFO; el rango, de `pricing-curve.md` (Van Westendorp sobre las 100 respuestas).

## 1. Lo que dijeron los compradores (Van Westendorp)

| punto | precio | qué significa |
| --- | ---: | --- |
| PMC | ~2.480 € | por debajo, demasiados lo ven "demasiado barato para ser bueno" |
| OPP | ~3.011 € | mínima resistencia (tantos "barato" como "caro") |
| IPP | ~5.022 € | tantos lo llaman ganga como caro |
| PME | ~11.956 € | por encima, demasiados no comprarían |

**Rango aceptable: ~2.480 € a ~11.956 €.** Medianas: demasiado barato 2.000 €,
ganga 4.000 €, empieza a ser caro **9.500 €**, demasiado caro 14.000 €.

Lectura clave: **9.500 € está dentro del rango, pero en la parte alta** (justo en
la mediana de "empieza a ser caro"). El punto de equilibrio psicológico (IPP) está
en ~5.000 €. Es decir: el precio no es imposible, pero al comprador frío le pesa, y
por eso el panel solo compró al 8% al precio pelado y sin pruebas.

## 2. Lo que cobran los competidores (de `competitors.md`)

- Coaching suelto de pitch: 1.500-5.625 € (Pitch Perfect, Matt Boardman).
- Programa intensivo comparable: ~15.000 $ (Trebal & Chowsky).
- Alternativa que "lo cubre todo": fractional VP a 6.000-15.000 $/mes (3 meses =
  18.000-45.000 $).

9.500 € queda **por encima del coaching suelto** y **muy por debajo** del coste
acumulado de un fractional o una agencia. Coherente con vender un resultado de
negocio, no horas.

## 3. Lo que necesita el negocio (del CFO)

| precio | contribución/sprint | margen a plan | beneficio año 1 (con el ramp) |
| --- | ---: | ---: | ---: |
| 6.500 € | ~5.487 € | 79% | ~98.000 € |
| **9.500 €** | **~8.487 €** | **86%** | **~155.000 €** |
| 12.000 € | ~10.987 € | 89% | ~202.500 € |

El margen es enorme a cualquier precio del rango: el cuello de botella **no es el
precio ni el coste, es la confianza y el volumen** (horas del fundador). Esto cambia
la estrategia: el precio no hay que bajarlo para ganar dinero, hay que estructurarlo
para **comprar prueba y vencer la desconfianza**.

## 4. La decisión

**Mantener 9.500 € como precio de referencia del sprint completo** (está en rango y
el margen lo permite), pero **no venderlo en frío a ese precio**: el panel demuestra
que así solo entra el 8%. En su lugar, una escalera + una oferta de arranque que
ataquen directamente el killer nº1 (sin pruebas no hay venta):

### La escalera (good / better / best)

| nivel | qué es | precio a testear | para quién |
| --- | --- | ---: | --- |
| **Good — Demo Audit** | solo la auditoría de fricción (1 semana), con informe y 3 arreglos accionables | ~2.900 € (cerca de OPP) | el escéptico y el frugal: entrada de bajo riesgo que alimenta el sprint |
| **Better — el Sprint** | el sprint completo de 3 semanas (auditoría + narrativa de 7 min + roleplay) | 9.500 € | el presionado por el board (compra al 67%) |
| **Best — Sprint + Refuerzo** | sprint + 60 días de refuerzo/ensayo en vivo para que la narrativa sobreviva a la semana 4 (cierra la "costura" del consejo) | ~12.000 € | el que quiere que su equipo lo interiorice, no solo un guion |

El "Best" no pasa de ~12.000 € (justo en el PME): por encima, el panel dice que
demasiados se caen.

### La oferta de arranque (ataca el killer: la prueba)

**Cohorte fundadora: 5 plazas**, sprint completo a **4.900 €** (cerca del IPP, el
precio-ganga) **a cambio de** una métrica de proceso acordada de antemano (p. ej.
tasa de avance a 2ª reunión enterprise, antes vs. después) + permiso para publicar
el caso + testimonio. Urgencia **real** (5 plazas, cohorte con fecha), nunca falsa.
Esto convierte el mayor "no" (sin casos) en el motor de los primeros casos. No
entrena al mercado a esperar descuentos porque es explícitamente fundacional y
limitada.

> Nota: 4.900 € sigue dejando ~79% de margen (CFO). No es "comprar clientes a
> pérdida"; es invertir margen en generar la prueba que desbloquea el precio pleno.

## 5. Qué testear con compradores reales (antes de fijar nada)

1. **Dos precios de entrada:** el **Demo Audit a ~2.900 €** vs. el **Sprint fundador
   a 4.900 €**. Dos landing pages, mismo tráfico, medir reservas/pre-ventas.
2. **El ancla del sprint pleno:** 6.500 € vs. 9.500 € a compradores que **no** están
   presionados por el board (el segmento caliente paga 9.500 sin pestañear; la duda
   es el resto).
3. En todos, **segmentar por urgencia de board**: es la única variable que en el
   panel mueve la compra (67% vs. 0%).

## 6. Objeciones de precio del panel (verbatim, para que marketing las responda)

- "No tengo runway para soltar 9.500 € fijos por un sprint de 3 semanas cuando mi
  ciclo enterprise tarda meses en cerrar. Arreglar el pitch no me arregla el pipeline
  a tiempo." (P025)
- "Casi no tengo runway y 9.500 € es una barbaridad para algo que, siendo técnica,
  creo que puedo arreglar yo misma." (P019)
- "Pago 9.500 € cuando vea retorno medible, no antes." (P001)

Las tres se responden con lo mismo: **prueba** (casos con cifras) + **riesgo
compartido** (parte del fee ligada a una métrica de proceso) + una **entrada barata**
(el audit) que no exige confiar 9.500 € de golpe.

---
_Precio dentro de rango pero alto para el comprador frío; el margen no es el
problema. Si se adopta la escalera, actualizar `numbers.json` con el mix real de
audit/sprint/best y re-correr `/founder-cfo`. Siguiente: `/founder-offer`._
