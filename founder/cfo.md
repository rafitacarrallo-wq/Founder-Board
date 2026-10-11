# CFO — "Comer bien sin pensar" (nombre de trabajo)

> **Todo son estimaciones a validar**, no datos reales. La unidad es *una
> suscripción de pago al mes*; donde el tool dice "al día", **léase "al mes"**
> (se fijó `days_per_month=1` para adaptar un modelo pensado para ventas diarias).
> Lo más importante está en §4: **tres costes que el tool NO modela y que son los
> que deciden si esto vive o muere.**

## 1. Una suscripción de pago (al mes)

| línea | por suscripción/mes |
| --- | ---: |
| Precio bruto (ARPU mezcla anual+mensual) | 4,00 € |
| − Comisión tienda (~15%) | −0,60 € |
| − IA por usuario de pago (estimado) | −0,80 € |
| − Infra/backend por usuario (estimado) | −0,15 € |
| **Contribución** | **2,45 € (61%)** |

## 2. El margen que importa (cifras del tool, relabeladas a /mes)

- **Punto de equilibrio: ~1.633 suscriptores de pago.** Por debajo, pierdes dinero
  cada mes.
- Margen al plan (3.000 suscriptores de pago): **28%** tras todos los costes.
- **Año 1 operativo: −2.430 €** sobre 74.400 € de ingresos.
- Con los 6.350 € de arranque: acumulado **−8.780 €** a fin de año.
- **Caja necesaria antes de que se pague solo: ~20.918 €** (el punto más bajo, mes 6).
- La inversión de arranque **no se recupera dentro del año 1**.

## 3. Qué pasa si… (del tool)

| escenario | margen | equilibrio (subs) | beneficio año 1 |
| --- | ---: | ---: | ---: |
| Plan base | 28% | 1.633 | −2.430 € |
| Precio −10% | 20% | 1.952 | −9.870 € |
| Volumen −20% | 20% | 1.633 | −11.544 € |
| Costes unidad +15% | 22% | 1.804 | −6.754 € |

## 4. Lo que el tool NO ve — y que lo cambia todo 🔴

El modelo de arriba trata cada suscriptor de pago como un café vendido. Un
freemium de IA tiene tres agujeros que el tool no captura y que, con las cifras
realistas del sector, **vuelven el resultado mucho peor**:

1. **El coste de IA de los usuarios GRATIS.** Para tener 3.000 de pago necesitas una
   base gratis enorme. A una conversión del 4% (optimista en freemium), son
   **~75.000 usuarios gratis**. Si cada uno consume solo 0,15 €/mes de IA = **11.250
   €/mes** de coste que arriba no aparece — **más de 3× el beneficio al plan**. Este
   único punto puede hundir el modelo. Mitigación obligatoria: **capar duro la IA
   del tier gratis** (1 sugerencia/día, cachear, modelo barato) y dejar lo caro
   (importar reels con visión) solo en Premium.

2. **CAC (coste de adquirir un cliente).** Los 1.500 €/mes de marketing son un
   placeholder. En una app de consumo por social de pago, el coste por instalación
   va de 2 a 8 €, y a un 4% de conversión a pago, el **CAC por usuario DE PAGO
   puede ser de 50–200 €**. El plan de marketing (`/founder-marketing`) tiene que
   demostrar un canal mucho más barato (orgánico), pero ojo: el panel dice que el
   gancho orgánico (reels) atrae justo a quien **no** paga.

3. **Churn / LTV — el killer más probable.** Una suscripción vive o muere por la
   retención, y el panel gritó el riesgo ("la dejo a las dos semanas"). Con
   contribución 2,45 € y un churn mensual del 15% (normal en apps de consumo), el
   **LTV ≈ 2,45 / 0,15 ≈ 16 €** por cliente. **Si el CAC supera ~16 €, cada cliente
   que entra pierde dinero**, y cuanto más creces, más pierdes. Aquí es donde el
   negocio se rompe, y es exactamente el muro que marcaron el consejo y el panel.

## 5. Veredicto del CFO

**NO es rentable todavía** — ni siquiera con mis estimaciones, que son generosas:

- Año 1 pierde dinero (−2.430 € operativo, −8.780 € con arranque) y exige ~21k € de
  caja, sin un presupuesto del fundador definido.
- Y los tres factores de §4 (IA de los gratis, CAC, churn/LTV) **no están en esos
  números y es donde el modelo realista se vuelve claramente negativo**.

La viabilidad depende por completo de tres cosas que hoy no están probadas:
**(a)** que el coste de IA por usuario sea mínimo, **(b)** que el churn sea bajo
—la retención que el panel dudó—, y **(c)** que el CAC sea bajo —orgánico, cuando
el gancho atrae a los que no pagan—. Si las tres no salen, no hay negocio.

**Números que hay que conseguir de verdad antes de construir:** coste real de IA
por usuario (medir con un prototipo), CAC por canal (gastar 200–500 € en un test),
y churn a 4 semanas (de la prueba del panel real que propone `/founder-launch`).

---
*Fuentes: `founder/numbers.json`, `founder/cfo-tool.md`, `founder/pricing.md`, `founder/panel/results.md`, `founder/board.md`. Cifras del tool = estimaciones; §4 son los riesgos no modelados.*
