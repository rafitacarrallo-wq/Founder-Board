# Operaciones — proyecto "Comer bien sin pensar" (app)

> Una app no abre a las 7am como un café, pero igual tiene un "día uno" que hay
> que poder operar. Aquí: el ciclo diario, los proveedores (que son los costes de
> IA e infra del CFO), el equipo, las rutinas, las herramientas, los permisos en
> España y los riesgos.

## 1. El ciclo diario (qué ve el cliente marcado 👁️)

1. 👁️ El usuario abre la app y pide "qué ceno hoy" → la app llama al modelo de IA.
2. 👁️ Importa un reel → servicio de extracción (visión/transcripción) devuelve receta.
3. Backend registra uso (para control de coste de IA por usuario).
4. 👁️ Soporte: responder dudas/quejas del día (crítico para la garantía 30 días).
5. Monitorizar coste de IA del día y errores (alertas si se dispara).
6. Publicar 1 pieza de contenido (TikTok/IG) — es adquisición, no opcional.
7. Revisar altas, activaciones (¿hicieron su 1ª cena?) y cancelaciones del día.

## 2. Proveedores (= los costes variables del CFO)

| input | proveedores reales | precio / cómo | notas |
| --- | --- | --- | --- |
| **Modelo de IA** (el coste nº1) | Anthropic (Claude Haiku para lo barato), OpenAI, Google Gemini, o modelo abierto autoalojado | por tokens; Haiku/modelos pequeños son los baratos | **medir coste real por usuario con un prototipo**; usar modelo barato + caché para el tier gratis |
| **Extracción de reels** | API de transcripción + visión del mismo proveedor, o Whisper autoalojado | por minuto/imagen | punto frágil: depende de acceso a TikTok/IG (ver riesgos) |
| **Infra/hosting** | Supabase, Render, Fly.io, AWS | desde ~0–25 €/mes y escala | base fija baja; crece con usuarios |
| **Pasarela/suscripciones** | RevenueCat (gestiona suscripciones in-app) + Apple/Google | RevenueCat gratis hasta ~2,5k$/mes de ingresos | la comisión de tienda (15%) ya está en el CFO |
| **Integración súper** (bonus fase 2) | APIs/afiliación de súper online (p. ej. agregadores de la compra) | a negociar | probablemente no exista API limpia → riesgo de alcance |

Si al pedir presupuestos el coste real de IA difiere de los 0,80 €/usuario del
`numbers.json`, **actualízalo y re-corre `/founder-cfo`** — es el número que decide todo.

## 3. Personas

- **Mes 1–6: el fundador solo** (desarrollo + soporte + contenido). Coste reflejado
  como "fundador" en el CFO (2.000 €/mes, ajustable: si es a tiempo parcial sin
  sueldo, baja, pero cuenta el coste de oportunidad).
- **Freelance puntual:** diseñador de marca/logo (one-off), y un editor de vídeo
  para TikTok si el contenido no escala (≈15–25 €/vídeo). 
- Nada de plantilla fija hasta pasar el punto de equilibrio (~1.633 subs de pago).
- Cotizaciones de autónomo y fiscalidad: que lo confirme un gestor (§6).

## 4. Rutinas (SOPs de una página)

- **Lanzamiento diario de contenido:** 1) revisa qué hook toca (ver marketing), 2)
  graba 20–40s, 3) publica TikTok+IG+Reels, 4) responde comentarios 1h.
- **Soporte / queja:** 1) responde <24h, 2) si la receta falló, pide disculpa +
  ofrece otra, 3) si pide la garantía, **devuelve sin fricción** (es la promesa), 4)
  anota el motivo (para producto).
- **Control de coste de IA (diario):** 1) mira el gasto del día por usuario, 2) si
  un usuario/segmento dispara coste, revisa límites del tier gratis, 3) alerta si el
  coste/usuario supera el supuesto del CFO.
- **Cierre semanal:** retención a 14 días, activación, CAC por canal, churn,
  coste IA/usuario. Si retención <25% → parar adquisición y arreglar producto.

## 5. Herramientas (stack mínimo)

| función | producto | precio |
| --- | --- | --- |
| Suscripciones in-app | RevenueCat | gratis hasta ~2,5k$/mes |
| Backend + DB + auth | Supabase | gratis→25 €/mes |
| Analítica producto | PostHog (free tier) | gratis→según volumen |
| Soporte | email + Crisp/Intercom (free/low) | 0–25 €/mes |
| Contabilidad | gestor online (Quipu/Declarando) o gestoría | ~15–40 €/mes |
| Repos/CI | GitHub (ya en uso) | gratis |

## 6. Licencias, permisos y seguros (España — confirma cada uno)

- **Alta de autónomo** (RETA) y **alta censal en Hacienda** (modelo 036/037) →
  seg-social.es y sede.agenciatributaria.gob.es.
- **RGPD / LOPDGDD**: política de privacidad, base legal del tratamiento, y cuidado
  con datos de salud si infieres dieta/alergias (categoría especial). → aepd.es.
- **IVA del servicio digital / suscripciones** y **ventas vía Apple/Google** (ellos
  gestionan parte del IVA, pero confírmalo) → agenciatributaria.gob.es.
- **Condiciones de uso de TikTok/Instagram**: revisar si la extracción de su
  contenido respeta sus términos (riesgo legal y técnico, ver §7).
- **Cumplimiento App Store / Google Play** (guidelines de suscripciones y de IA).
- **Seguro de RC profesional** (opcional al inicio, recomendable).
> Las reglas cambian y dependen de tu caso: confírmalo con un **gestor/abogado**.
> Esto no es asesoría legal.

## 7. Registro de riesgos (los 10 principales)

| riesgo | prob. | impacto | plan |
| --- | --- | --- | --- |
| TikTok/IG cierran o prohíben la extracción de reels | media | **alto** (mata el diferenciador) | no apoyar el core en reels; que la app valga sin ellos |
| Coste de IA por usuario más alto de lo estimado | **alta** | **alto** | capar IA del tier gratis, caché, modelo barato; medir desde el día 1 |
| Churn alto (no se quedan) | **alta** | **alto** | la garantía y la retención son el foco nº1; test real antes de escalar |
| CAC > LTV (adquisición cara) | media | alto | solo orgánico hasta validar CAC < 5 € |
| La IA recomienda algo malo y rompe la confianza | media | medio | plan de recuperación + feedback 1 toque |
| Dependencia de un solo proveedor de IA | media | medio | abstraer el proveedor para poder cambiar |
| Fundador solo se quema / enferma | media | medio | automatizar soporte, documentar, no prometer SLA |
| Rechazo en App Store (políticas IA/suscripción) | media | medio | leer guidelines antes, tener plan B de pago web |
| Incidente de datos (RGPD) | baja | **alto** | minimizar datos, cifrado, no tratar salud sin base legal |
| Un gigante (Google/Mercadona) lanza lo mismo gratis | media | alto | nicho + rapidez + marca; no competir en features sino en "la que sí usas" |

## Actualización al CFO
Ningún coste real nuevo todavía (todo sigue estimado). El número a cerrar con
proveedores reales antes de construir es **el coste de IA por usuario**.

---
*Fuentes: `founder/idea.md`, `founder/offer.md`, `founder/numbers.json`, `founder/cfo.md`, `founder/marketing.md`.*
