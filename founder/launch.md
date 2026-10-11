# Lanzamiento — proyecto "Comer bien sin pensar" (app)

> Regla de oro del pack: **el test barato primero**, antes de construir la app
> entera. Aquí el negocio es de suscripción, así que el test es una oferta de socio
> fundador pagada por adelantado + una prueba de que la gente SE QUEDA.

## 1. El test antes de gastar (haz esto ANTES de desarrollar)

El panel dio 37% de compra, pero avisó: el muro es la **retención**, no el interés.
Así que el test tiene dos partes:

**Test A — ¿pagan? (1–2 semanas, ~100–300 €):**
- Landing con el pitch v2 (garantía 30 días + socio fundador) y botón **"Reserva tu
  plaza de socio fundador — 29,99 €/año de por vida"** con pago real (Stripe).
- Tráfico: los primeros vídeos de TikTok/IG (orgánico) + 100–200 € de ads para
  medir CAC.
- **Línea de éxito (escríbela antes):** **≥50 pre-pagos de socio fundador en 2
  semanas con CAC < 5 €.** Si no llega, el problema es oferta/precio/mercado →
  volver a `/founder-offer` o `/founder-pricing`, no construir.

**Test B — ¿se quedan? (el que de verdad importa):**
- Prototipo mínimo (aunque sea medio manual / "mago de Oz": tú generas los menús
  con IA por detrás) para 20–30 de esos fundadores.
- **Línea de éxito:** **≥40% siguen usándolo a las 2 semanas** y ≥25% a las 4.
- Si la retención es baja, **no escalar**: el CFO ya mostró que con churn alto el
  LTV (~16 €) no cubre el CAC. Arreglar producto (onboarding, acierto, anti-repetición)
  antes de gastar en marketing.

> Si el test real queda muy por debajo del panel, **cree al comprador real**, no al
> simulado.

## 2. La cuenta atrás (fija tu fecha; aquí, semanas relativas)

Pon fecha objetivo realista (sugerido: **~10–12 semanas** desde hoy, condicionado a
pasar el Test A/B). Camino crítico marcado 🔴.

| semana | legal/dinero | producto | marca | marketing |
| --- | --- | --- | --- | --- |
| S−10 | — | 🔴 prototipo mago-de-Oz para Test B | nombre + checks (Noca/…) | landing Test A online |
| S−9 | — | medir coste IA/usuario real 🔴 | logo concepto | arrancar TikTok/IG orgánico |
| S−8 | alta autónomo + 036 | construir MVP core ("qué ceno hoy") | perfiles sociales | cerrar 3 micro-creadores |
| S−6 | política RGPD + privacidad 🔴 | importar reels (con revisión) | ficha App Store | hooks 1–4 publicados |
| S−4 | RevenueCat + Apple/Google dev | lista de la compra + anti-repetición | ASO | lista de espera socio fundador |
| S−2 | revisar guidelines de store 🔴 | garantía 30 días implementada | onboarding pulido | hooks 5–8 + recordatorio cierre |
| S−1 | — | 🔴 soft open amigos y beta (fundadores) | — | aviso lanzamiento |
| **S0** | — | **lanzamiento público** | — | día 0 campaña (abajo) |

**Camino crítico:** prototipo→medir IA→MVP core→RGPD→revisión de store. Si uno de
esos resbala, se mueve la fecha.

## 3. Día de lanzamiento (run sheet)

| hora | qué | si algo falla |
| --- | --- | --- |
| 08:00 | app publicada y verificada en iOS/Android | si store rechaza → plan B pago web, avisar lista |
| 09:00 | post lanzamiento en TikTok+IG+Reels (Hook 1) | — |
| 10:00 | email a lista de espera + socios fundadores | — |
| 12:00 | monitor: altas, activación (1ª cena), **coste IA/usuario** | si IA se dispara → activar límites tier gratis |
| 14:00 | responder comentarios/soporte (<1h) | queja → SOP de queja + garantía |
| 18:00 | 2º push (Hook 4 reels) en hora de "qué ceno" | — |
| 21:00 | corte del día: nº altas, CAC, errores | registrar para revisión |

Recordatorio: **socio fundador cierra en S0+7** (urgencia real, con fecha).

## 4. Los primeros 30 días

**Números semanales (umbral que obliga a cambiar):**
- **Retención a 14 días** → si <25%, **parar adquisición** y arreglar producto.
- **Coste de IA por usuario** → si > supuesto del CFO (0,80 € pago / límite gratis),
  ajustar límites/modelo.
- **CAC por canal** → si > 5 €, cortar ese canal.
- Activación (% que hace su 1ª cena) → si <50%, arreglar onboarding.
- Conversión gratis→pago → alimenta de nuevo al CFO.

**Revisiones:**
- **Día 7:** ¿la gente activa y vuelve? ¿el coste de IA aguanta?
- **Día 14:** ¿retención ≥25%? Si no, foco total en producto, no en crecer.
- **Día 30:** ¿unidad económica real (CAC vs LTV) positiva? Si no, **no escalar el
  gasto**; iterar o reconsiderar (ver el veredicto del plan).

---
*Fuentes: `founder/offer.md`, `founder/pricing.md`, `founder/cfo.md`, `founder/marketing.md`, `founder/brand.md`, `founder/ops.md`.*
