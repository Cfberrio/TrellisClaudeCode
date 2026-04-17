# Implementation Notes

## Status: Phase 0 — Structure Only

Este proyecto está en fase de organización estructural. La implementación de extracción, transformación y reporting está pendiente.

---

## Decisions Made

### 1. Single output per brand, versioned by month
El output final en `output/meta/{brand}/YYYY-MM/` siempre es consolidado Facebook + Instagram. No existe separación por plataforma en el output humano. Cada mes genera su propia carpeta — el output nunca se sobreescribe.

### 2. Platform separation in raw/
`data/raw/meta/{brand}/facebook/` y `.../instagram/` están separados porque las APIs son distintas, los schemas son distintos, y los scripts de extracción son distintos.

### 3. Merge happens at staging → processed
El punto de consolidación es `data/processed/`. El staging normaliza, el processed mergea.

### 4. TikTok reserved slot
`config/platforms.json` tiene TikTok con `"active": false`. No crear carpetas de raw/staging/processed para TikTok hasta que sea activado. La arquitectura de processed/ y output/ ya puede absorberlo sin cambios.

### 5. Domain placement
Este dominio vive en `domains/ops/social-metrics/`, separado de:
- `domains/ads/meta/` — paid ads pipeline
- `domains/ops/social-automation/` — automatización de comentarios

---

## Implementation Sequence (pending)

### Phase 1 — Extraction
- [ ] Configurar autenticación Meta Graph API (Long-Lived Token o System User Token)
- [ ] Implementar `src/meta/facebook/extractor.py`
- [ ] Implementar `src/meta/instagram/extractor.py`
- [ ] Script orquestador en `scripts/meta/run_extract.sh`

### Phase 2 — Normalization + Merge
- [ ] Implementar `src/meta/shared/normalizer.py` — schema común de staging
- [ ] Implementar `src/meta/shared/merger.py` — consolida FB + IG en processed
- [ ] Validadores en `src/common/validators/`

### Phase 3 — Output Generation
- [ ] Generar JSONs de output por marca
- [ ] Generar monthly_metrics_flat.csv
- [ ] Generar monthly_analysis.md con datos reales
- [ ] (Opcional) Generar monthly_metrics_pretty.xlsx

---

## Known Constraints

- **Token expiry:** Los Long-Lived Tokens de usuario expiran a los 60 días. Usar System User Token para producción.
- **Stories expiry:** Las métricas de Instagram Stories expiran a los 7 días. Si no se extrae dentro de la ventana, los datos se pierden.
- **Facebook Insights window:** Los insights de posts están disponibles por 90 días. Planificar extracción mensual.
- **Rate limits:** 200 llamadas/hora por app token. Para 3 marcas con extracción completa, estimar ~50–80 llamadas por marca. Está dentro de límites.

---

## Auth Setup (pending)

Ver `.env.example` para las variables requeridas. El flujo de autenticación se documentará en `scripts/setup/` en la fase de implementación.

---

## Open Questions

- ¿Se centraliza un solo app token para todas las marcas o un token por marca?
- ¿Qué profundidad de historial se extrae en la primera corrida?
- ¿Se automatiza la extracción mensual o es manual por ahora?
