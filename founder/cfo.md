# Unit economics: Demo-to-Deal (sprint de rediseno de demo y pitch GTM, consultor solo)

> **Nota del CFO (léela primero).** Dos avisos de lectura: (1) la herramienta
> imprime el símbolo `$`, pero **todas las cifras están en euros**. (2) El modelo usa
> `days_per_month = 1`, así que donde pone **"a day" hay que leer "al mes"**: la
> unidad es un **sprint al mes**. Y no hay sueldo del fundador en los costes fijos:
> **el beneficio operativo ES lo que se lleva el fundador** (antes de impuestos).
>
> - **El margen.** Cada sprint deja **~8.487 €** de contribución (**89%**). Margen a
>   plan (2 sprints/mes): **86%**. El punto de equilibrio es ~**0,06 sprints al mes**
>   (la herramienta lo redondea hacia arriba a "1"): es decir, **el primer sprint del
>   mes ya cubre meses de gastos fijos**. Este no es un negocio con problema de
>   margen.
> - **La línea que manda: el volumen (la rampa), no el coste.** El negocio está capado
>   por las horas del fundador (máx. ~2 sprints/mes). Por eso el what-if que de verdad
>   mueve el resultado es el de volumen: a mitad de rampa (volumen 0,5) el año 1 cae de
>   ~**149.500 €** a ~**74.400 €**. Bajar el precio un 10% apenas toca el margen (de 86%
>   a ~85%): el precio **no** es la palanca; el número de sprints lo es.
> - **El techo.** A plena capacidad (2 sprints/mes a 9.500 €) el año 1 ronda los
>   **~150.000 €**. Es un buen ingreso para una persona, pero **es el techo**: confirma
>   el aviso del consejo (lente de Monopolio y de Producto) de que el negocio es
>   anti-escala mientras dependa solo de las horas del fundador.
> - **Caja.** Necesitas muy poca: **~6.020 €** (5.500 € de arranque + el mes 1 sin
>   ingresos). El dinero de arranque se recupera en el **mes 2**. El riesgo financiero
>   es bajísimo; el riesgo real es de **demanda/confianza**, no de caja.
> - **Tres formas de mejorar el resultado (con su número):**
>   1. **Subir la capacidad / productizar** (playbook + assets para entregar más rápido,
>      o licenciar el método). Es LA palanca: cada sprint/mes extra ≈ **+8.487 €/mes ≈
>      +100.000 €/año**. Ataca directamente el techo.
>   2. **Añadir el nivel "Best" (refuerzo 60 días) a ~12.000 €:** +~2.500 € de
>      contribución por cada sprint que suba de nivel.
>   3. **Construir referencias directas de VCs** y reducir la comisión de partner
>      (hoy ~5% = 475 €/sprint): +**475 €/sprint** y además baja el CAC.
> - **Condiciones de dinero del consejo:** la disposición a pagar se validó con
>   Van Westendorp (9.500 € está en rango, ver `pricing.md`); el margen financia de
>   sobra el descuento de cohorte fundadora (4.900 € siguen dejando ~79%) y la
>   garantía (coste esperado ~150-400 €/sprint). La condición pendiente **no es
>   financiera**: es generar los **casos reales** que suban la conversión por encima
>   del 8-15% del panel.
> - La herramienta no es asesoría fiscal ni legal: **un asesor/gestor debe revisar la
>   estructura (autónomo vs. sociedad), el IVA y los impuestos** antes de mover dinero.
>   Los ingresos son antes de impuestos; en la UE el IVA va aparte según el cliente.

Every number below comes from the input file. Nothing is looked up or guessed.

## One sprint

| line | per sprint |
| --- | ---: |
| Price | $9,500.00 |
| Comision de pago (~2,5%) | -$238.00 |
| Diseno freelance del entregable (deck/narrativa) | -$260.00 |
| Creditos de grabacion/transcripcion del roleplay | -$40.00 |
| Comision de referido/partner (blended ~5%) | -$475.00 |
| **Contribution** (what each sprint leaves to pay the fixed costs) | **$8,487.00** (89%) |

## The margin that matters

Fixed costs: $520 a month (Stack software (CRM, Sales Navigator, scheduling, email, grabacion) $260, Gestoria + seguro RC profesional $200, Web/hosting/suscripciones varias $60).

- **Break-even: 1 sprints a day.** Below that you lose money every month.
- **Profit margin at your plan** (2 a day): **86%** of every sale, after every cost.
- Capacity: 2 a day.

## Year 1, month by month

| month | sprints a day | revenue | profit | cumulative (after $5,500 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | $0 | -$520 | -$6,020 |
| 2 | 1 | $9,500 | $7,967 | $1,947 |
| 3 | 1 | $9,500 | $7,967 | $9,914 |
| 4 | 1 | $9,500 | $7,967 | $17,881 |
| 5 | 2 | $19,000 | $16,454 | $34,335 |
| 6 | 2 | $19,000 | $16,454 | $50,789 |
| 7 | 2 | $19,000 | $16,454 | $67,243 |
| 8 | 2 | $19,000 | $16,454 | $83,697 |
| 9 | 2 | $19,000 | $16,454 | $100,151 |
| 10 | 2 | $19,000 | $16,454 | $116,605 |
| 11 | 2 | $19,000 | $16,454 | $133,059 |
| 12 | 2 | $19,000 | $16,454 | $149,513 |

- **Year 1 operating profit: $155,013** on $180,500 of revenue.
- After the $5,500 startup spend: $149,513.
- Startup money earned back: month 2.
- Cash you need before it pays for itself: **$6,020**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 86% | 1 | $155,013 |
| Price -10% | 84% | 1 | $136,963 |
| Volume -20% | 85% | 1 | $122,762 |
| Unit costs +15% | 84% | 1 | $152,126 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
