# X-150 Master Specifications Document

**Document Reference:** X150-MASTER-SPEC-001  
**Revision:** A  
**Date:** January 29, 2026  
**Authority Source:** X-150 TECH SHEET.pdf (Page 3)  
**Status:** AUTHORITY DOCUMENT  
**Priority:** CRITICAL  
**Data Integrity:** VERIFIED

---

## Metadata

| Field | Value |
|-------|-------|
| Document ID | X150-MASTER-SPEC-001 |
| System | X-150 Modular Gasification Platform |
| Authority | X-150 TECH SHEET.pdf |
| Source | J Lo (@Jloontour) |
| Imported | 2026-02-05 00:50 PST |
| Owner | Zero-X / Exventure Engineering |
| Access Level | INTERNAL |
| Related Docs | X150-SS-SPEC-001 (Sewage Sludge Variant) |

---

## 1. Physical Specifications

| Parameter | Value | Source |
|-----------|-------|--------|
| Dimensions | Length: 12m, Width: 3.5m, Height: 6m | Tech Sheet p.3 |
| Container Type | Standard 40ft container | Complete Info Doc p.17 |
| Weight (empty) | ~15 tonnes | Complete Info Doc p.17 |
| Footprint | 42 m² (single unit) | Complete Info Doc p.18 |

---

## 2. Operational Modes

### 2.1 MODE 1: Air Gasification

| Parameter | Wood Pellets | Fermentation Pellets | Source |
|-----------|--------------|----------------------|--------|
| Fuel mass flow | ~150 kg/h (w=10%, d=6-8mm) | 80-100 kg/h | Tech Sheet p.3 |
| Gasification agent flow | ~270 kg/h | 110-140 kg/h | Tech Sheet p.3 |
| Gas mass flow | ~400 kg/h | 152-205 kg/h | Tech Sheet p.3 |
| Coke ash output | ~20 kg/h | ~35 kg/h | Tech Sheet p.3 |
| Heat output | ~35 kW | ~20 kW | Tech Sheet p.3 |

### 2.2 MODE 2: Oxygen-Steam Gasification

| Parameter | Wood Pellets | Fermentation Pellets | Source |
|-----------|--------------|----------------------|--------|
| Fuel mass flow | ~150 kg/h | 80-100 kg/h | Tech Sheet p.3 |
| O₂ flow | ~38 kg/h | 20-26 kg/h | Tech Sheet p.3 |
| Steam flow | ~60 kg/h | 32-40 kg/h | Tech Sheet p.3 |
| Gas mass flow | ~225 kg/h | 104-131 kg/h | Tech Sheet p.3 |
| Coke ash output | ~23 kg/h | ~35 kg/h | Tech Sheet p.3 |
| Heat output | ~20 kW | ~12 kW | Tech Sheet p.3 |

---

## 3. Electrical Requirements

| Parameter | Value | Source |
|-----------|-------|--------|
| Power connection | 400 V, 32 A | Tech Sheet p.3 |
| Startup power | 12 kW | Complete Info Doc p.18 |
| Parasitic load | 8-12 kW (continuous) | Complete Info Doc p.18 |

---

## 4. Performance Metrics

| Parameter | Value | Source |
|-----------|-------|--------|
| Energy conversion efficiency | >85% | Engineering Report p.3 |
| Total efficiency | 42-53% (feedstock dependent) | Complete Info Doc p.2 |
| Operating temperature | 800-1000°C | Complete Info Doc p.1 |
| System availability | >95% | Complete Info Doc p.18 |
| Maintenance requirement | 200-400 hours/year | Complete Info Doc p.18 |

---

## 5. Output Configurations

| Configuration | Output per 150 kg/h unit | Source |
|--------------|--------------------------|--------|
| **VOLT** (Electricity) | 150 kW | Complete Info Doc p.3 |
| **HEAT** (Thermal) | 150 kW | Complete Info Doc p.4 |
| **CHILL** (Cooling) | 150 kW refrigeration | Complete Info Doc p.4 |
| **H2** (Hydrogen) | 15-25 kg/day | Complete Info Doc p.5 |
| **SAF** (Aviation Fuel) | 20-40 liters/day | Complete Info Doc p.5 |
| **RNG** (Natural Gas) | 30-60 Nm³/day | Complete Info Doc p.6 |

---

## 6. SYNGAPURE™ Catalyst (Add-on)

| Parameter | Value | Source |
|-----------|-------|--------|
| Tar removal efficiency | 94% | Complete Info Doc p.2 |
| Input tar content | ~8 ppm | Complete Info Doc p.2 |
| Output tar content | 0.48 ppm | Complete Info Doc p.2 |
| Operating temperature | 400-600°C | Complete Info Doc p.19 |
| Validated hours | 1,300+ (Paris COMETHA) | Complete Info Doc p.8 |

---

## 7. Hydrogen Production (with full purification)

| Parameter | Value | Source |
|-----------|-------|--------|
| Hydrogen purity | >99.99% | Gasification Machine PDF p.2 |
| Production rate | 1 ton/day (marketing claim) | Gasification Machine PDF p.2 |
| H₂ output (verified) | 15-25 kg/day per 150 kg/h unit | Complete Info Doc p.5 |

---

## 8. Byproducts

| Parameter | Value | Source |
|-----------|-------|--------|
| Ash/Biochar | 20-35 kg/h | Tech Sheet p.3, Complete Info Doc |
| Wastewater | Minimal (closed-loop) | Complete Info Doc p.18 |

---

## 9. Environmental Compliance

| Parameter | Value | Source |
|-----------|-------|--------|
| Emissions | EU IED compliant | Complete Info Doc p.18 |
| Noise level | <75 dB at 10m | Complete Info Doc p.18 |

---

## Document Control

| Rev | Date | Description | Author |
|---------|----------|-----------------|------------|
| A | Jan 29, 2026 | Initial compilation | Exventure Engineering |

---

**Copyright © 2026 Exventure GmbH. All rights reserved.**  
This document contains proprietary information.

---

## Cross-Reference Notes

### Relationship to X150-SS-SPEC-001 (Sewage Sludge Variant)

| Parameter | Master Spec (General) | Sewage Sludge Spec | Variance |
|-----------|----------------------|-------------------|----------|
| Weight (empty) | ~15 tonnes | 15,230 kg | ✅ Aligned |
| Container | 40ft standard | 40-ft High Cube | Similar |
| Footprint | 42 m² | (15m x 4m pad) | Aligned |
| Operating temp | 800-1000°C | 800°C (nominal) | Within range |
| Availability | >95% | ≥90% | Slightly conservative |
| Maintenance | 200-400 hrs/yr | (Part of OPEX calc) | Aligned |

### Key Differences
- Master spec covers **multiple feedstocks** (wood pellets, fermentation pellets)
- Sewage sludge spec is **specialized application** with unique drying/dewatering stages
- Master spec lists **all 6 output configurations** (VOLT/HEAT/CHILL/H2/SAF/RNG)
- Sewage sludge spec focuses on **thermal export** (62.1 kW) and heat recovery

### Questions for Clarification

1. **Hydrogen Production:** Master spec shows 15-25 kg/day H₂, but sewage sludge spec doesn't mention H₂ output configuration — is H2 production viable with sewage sludge feedstock?

2. **Output Configuration:** Should sewage sludge units be configured for HEAT (thermal) only, or can they be retrofitted for VOLT/Electricity output?

3. **Ash/Biochar:** Master spec shows 20-35 kg/h ash output — sewage sludge spec shows 9.2 kg/h ash/char. Is the lower output due to 35% ash content in sewage sludge vs. wood pellets?

4. **Availability Target:** Master spec claims >95% availability, sewage sludge guarantees ≥90%. Which is the standard commitment for client contracts?

5. **Dimensions:** Master spec shows 12m x 3.5m x 6m — sewage sludge spec container is 12.2m x 2.4m x 2.9m. Is the master spec referring to a different container variant or including external equipment?
