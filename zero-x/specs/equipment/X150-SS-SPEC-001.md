# X-150 Modular Gasification System
## Technical Specification for Sewage Sludge Application

---

| Parameter | Value |
|---------------|-----------|
| Application | Municipal Wastewater Treatment |
| Design Capacity | 15,000 Population Equivalent |
| Net Thermal Output | 62.1 kW |
| System Efficiency | 45.5% |

**Document Reference:** X150-SS-SPEC-001  
**Revision:** A  
**Date:** February 2026  
**Status:** For Client Review  
**Priority:** CRITICAL  
**Data Integrity:** VERIFIED

---

## Metadata

| Field | Value |
|-------|-------|
| Document ID | X150-SS-SPEC-001 |
| System | X-150 Modular Gasification |
| Application | Sewage Sludge |
| Source | J Lo (@Jloontour) |
| Imported | 2026-02-05 00:32 PST |
| Owner | Zero-X Labs / Equation Labs |
| Access Level | INTERNAL |
| Change Control | REQUIRED |

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Design Basis](#2-design-basis)
3. [Process Description](#3-process-description)
4. [Stream Table](#4-stream-table)
5. [Energy Balance](#5-energy-balance)
6. [Equipment Specifications](#6-equipment-specifications)
7. [Validated Performance Data](#7-validated-performance-data)
8. [Economic Analysis](#8-economic-analysis)
9. [Operating Modes](#9-operating-modes)
10. [Installation Requirements](#10-installation-requirements)
11. [Appendix A: Technical Data Summary](#appendix-a-technical-data-summary)

---

## 1. Executive Summary

### 1.1 Project Overview
The X-150 Modular Gasification System provides a complete waste-to-energy solution for municipal wastewater treatment plants. This specification covers the application for a 15,000 population equivalent (PE) facility, converting dewatered sewage sludge into valuable synthesis gas while achieving significant cost savings through reduced disposal requirements.

### 1.2 Key Features
- **Containerized Design:** Complete system in 40-ft ISO container for rapid deployment
- **Proven Technology:** Based on validated Cometha Phase 2 results with 116.85 hours operation
- **SYNGAPURE Catalyst:** Proprietary Ni-Ca/Al2O3 catalyst achieving 94% tar removal
- **Turnkey Solution:** Includes dewatering, drying, gasification, and gas cleanup
- **Flexible Operation:** Air or oxygen-steam gasification modes available

### 1.3 Performance Summary

| Metric | Value |
|------------|-----------|
| Wet Sludge Input (70% MC) | 131 kg/h |
| Dried Sludge to Gasifier (15% MC) | 46.2 kg/h |
| Syngas Production | 44.7 Nm3/h |
| Syngas LHV | 5.2 MJ/Nm3 |
| Cold Gas Efficiency | 65% |
| Net Thermal Export | 62.1 kW |
| System Efficiency | 45.5% |

---

## 2. Design Basis

### 2.1 Project Scope

| Item | Specification |
|----------|-------------------|
| Plant Size | 15,000 PE |
| Annual Operating Hours | 8,000 h/year |
| Design Life | 20 years |
| Availability Target | >90% |

### 2.2 Feedstock Specification

| Property | As Received | Dried | Unit |
|--------------|-----------------|-----------|----------|
| Moisture Content | 70 | 15 | wt% |
| Mass Flow Rate | 131 | 46.2 | kg/h |
| Lower Heating Value | 4.5 | 12.5 | MJ/kg |
| Bulk Density | 1,050 | 650 | kg/m3 |

### 2.3 Ultimate Analysis (Dry Ash-Free Basis)

| Element | Content (wt%) |
|-------------|-------------------|
| Carbon (C) | 51.0 |
| Hydrogen (H) | 7.2 |
| Oxygen (O) | 32.5 |
| Nitrogen (N) | 7.8 |
| Sulfur (S) | 1.5 |
| Ash | 35.0 |

### 2.4 Ambient Conditions

| Parameter | Design Value |
|---------------|------------------|
| Temperature Range | -10 to +40 C |
| Design Temperature | 15 C |
| Atmospheric Pressure | 101.325 kPa |
| Relative Humidity | 30-90% |

---

## 3. Process Description

### 3.1 Process Overview

The X-150 system comprises four integrated process stages:

```
Wet Sludge -> Dewatering -> Drying -> Gasification -> Gas Cleanup -> Clean Syngas
(70% MC)     (T-101)      (T-102)   (R-101)         (V-101/E-102/FL-101)
```

### 3.2 Stage 1: Mechanical Dewatering (T-101)
Incoming sludge at 95-97% moisture is mechanically dewatered using a belt filter press to achieve 70% moisture content. This reduces the thermal energy required for subsequent drying.

- **Equipment:** Belt filter press with polymer dosing
- **Capacity:** 150 kg/h wet sludge
- **Power consumption:** 3 kW
- **Polymer dosing:** 3-5 kg/tonne dry solids

### 3.3 Stage 2: Thermal Drying (T-102)
Dewatered sludge is dried from 70% to 15% moisture content using waste heat from the gasification process supplemented by the thermal oil system.

- **Equipment:** Indirect paddle dryer with thermal oil heating
- **Heat duty:** 45 kW
- **Evaporation rate:** 84.8 kg/h water
- **Outlet temperature:** 105°C
- **Residence time:** 45-60 minutes

### 3.4 Stage 3: Gasification (R-101)
Dried sludge enters the fixed-bed downdraft gasifier where it undergoes thermal conversion at 800°C with controlled air injection. The SYNGAPURE catalyst promotes tar cracking and improves gas quality.

**Gasification Zones:**
1. **Drying Zone (100-200°C):** Residual moisture removal
2. **Pyrolysis Zone (200-600°C):** Thermal decomposition to char, tar, and volatiles
3. **Oxidation Zone (800-1100°C):** Partial combustion providing process heat
4. **Reduction Zone (600-800°C):** Catalytic conversion of tar and char to syngas

**Operating Parameters:**
- Temperature: 800°C (oxidation zone up to 1100°C)
- Pressure: Atmospheric (slight negative, -50 Pa)
- Equivalence Ratio (ER): 0.25-0.30
- Air flow: 52.4 Nm³/h
- Residence time: 1.5-2.0 seconds (gas phase)

### 3.5 Stage 4: Gas Cleanup
Raw syngas passes through a multi-stage cleanup system:
1. **Cyclone Separator (V-101):** Removes >95% of particles >10 μm
2. **Gas Cooler (E-102):** Reduces temperature from 350°C to 40°C
3. **Fabric Filter (FL-101):** Final particulate removal to <10 mg/Nm³

---

## 4. Stream Table

| Stream | Description | Flow | Temp | Pressure | Composition/Notes |
|------------|-----------------|----------|----------|--------------|----------------------|
| S-101 | Wet sludge feed | 131 kg/h | 20°C | Atm | 70% moisture, 30% solids |
| S-102 | Dried sludge | 46.2 kg/h | 105°C | Atm | 15% moisture, 85% solids |
| S-103 | Gasification air | 52.4 Nm³/h | 350°C | 1.05 bar | Preheated combustion air |
| S-104 | Raw syngas | 97.1 Nm³/h | 800°C | 0.995 bar | Hot gas with tar/particulates |
| S-105 | Cooled syngas | 44.7 Nm³/h | 40°C | 0.98 bar | Cleaned synthesis gas |
| S-106 | Ash/char residue | 9.2 kg/h | 400°C | Atm | 85% ash, 15% carbon |
| S-107 | Condensate | 7.3 kg/h | 40°C | Atm | Process water with organics |
| S-108 | Thermal oil supply | 2.5 m³/h | 280°C | 3 bar | Therminol 66 |
| S-109 | Thermal oil return | 2.5 m³/h | 250°C | 2.5 bar | Therminol 66 |

### 4.1 Syngas Composition

| Component | Concentration (vol%) |
|---------------|--------------------------|
| Carbon Monoxide (CO) | 15.0 |
| Hydrogen (H₂) | 12.0 |
| Carbon Dioxide (CO₂) | 15.0 |
| Methane (CH₄) | 3.0 |
| Nitrogen (N₂) | 50.0 |
| Water Vapor (H₂O) | 4.5 |
| Hydrogen Sulfide (H₂S) | 0.3 |
| Ammonia (NH₃) | 0.2 |
| **Total** | **100.0** |

**Syngas Properties:**
- Lower Heating Value: 5.2 MJ/Nm³
- Density (STP): 1.15 kg/Nm³
- Tar content: <50 mg/Nm³ (after cleanup)
- Particulate content: <10 mg/Nm³

---

## 5. Energy Balance

### 5.1 Energy Inputs

| Input | Value | Unit |
|-----------|-----------|----------|
| Dried sludge chemical energy | 160.4 | kW (LHV) |
| Dryer heat input | 45.0 | kW |
| Air preheater duty | 7.1 | kW |
| Electrical (blower, pump, controls) | 5.2 | kW |
| **Total Energy Input** | **141.7** | **kW** |

### 5.2 Energy Outputs

| Output | Value | Unit |
|------------|-----------|----------|
| Syngas chemical energy | 64.6 | kW (LHV) |
| Heat recovery (to dryer) | 45.0 | kW |
| Thermal losses | 18.5 | kW |
| Sensible heat in ash | 3.2 | kW |
| Sensible heat in condensate | 5.2 | kW |
| **Total Energy Output** | **136.5** | **kW** |

### 5.3 Efficiency Summary

| Efficiency Metric | Value |
|-----------------------|-----------|
| Cold Gas Efficiency (CGE) | 65% |
| Hot Gas Efficiency | 72% |
| Carbon Conversion | 67% |
| Net System Efficiency | 45.5% |
| Net Thermal Export | 62.1 kW |

---

## 6. Equipment Specifications

*Section continues with detailed equipment specifications...*

---

## Priority Data Points (Critical Monitoring)

### P0 - Critical Performance Metrics

| Parameter | Value | Tolerance | Alert Threshold | Stream |
|-----------|-------|-----------|-----------------|--------|
| Net Thermal Output | 62.1 kW | ±5% | <59 kW or >65 kW | System |
| System Efficiency | 45.5% | ±2% | <43% or >48% | System |
| Syngas LHV | 5.2 MJ/Nm³ | ±0.3 | <4.9 or >5.5 | S-105 |
| Cold Gas Efficiency | 65% | ±3% | <62% | System |
| Moisture Content (Dried) | 15% | ±2% | >18% | S-102 |
| SYNGAPURE Tar Removal | 94% | ±2% | <92% | S-105 |

### P1 - Process Control Setpoints

| Parameter | Value | Unit | Equipment |
|-----------|-------|------|-----------|
| Gasification Temperature | 800 | °C | R-101 |
| Oxidation Zone Max | 1100 | °C | R-101 |
| Dryer Outlet Temperature | 105 | °C | T-102 |
| Thermal Oil Supply | 280 | °C | S-108 |
| Thermal Oil Return | 250 | °C | S-109 |
| Gas Cooler Outlet | 40 | °C | E-102 |
| Air Flow Rate | 52.4 | Nm³/h | S-103 |
| Equivalence Ratio | 0.25-0.30 | - | R-101 |
| Pressure (Gasifier) | -50 | Pa | R-101 |

### P2 - Quality Targets

| Parameter | Value | Unit | Stream |
|-----------|-------|------|--------|
| Tar Content (final) | <50 | mg/Nm³ | S-105 |
| Particulate Content | <10 | mg/Nm³ | S-105 |
| CO Concentration | 15.0 | vol% | S-105 |
| H₂ Concentration | 12.0 | vol% | S-105 |
| H₂S Concentration | 0.3 | vol% | S-105 |

---

## Document Status

| Field | Value |
|-------|-------|
| Completeness | 75% (Sections 7-11 pending) |
| Last Updated | 2026-02-05 00:35 PST |
| Verified By | Global Control Center |
| Next Review | Upon receipt of remaining sections |
