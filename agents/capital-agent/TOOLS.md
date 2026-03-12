# TOOLS.md - Agent Capital Tools & Commands

## Command Triggers

| Command | Action |
|---------|--------|
| `/model [project]` | Build comprehensive financial model |
| `/roi [inputs]` | Calculate ROI, IRR, NPV, payback |
| `/optimize [parameter]` | Find optimal configuration |
| `/rank [projects]` | Rank opportunities 1-10 |
| `/bankability [project]` | Assess lender readiness |
| `/sensitivity [variable]` | Run sensitivity analysis |
| `/fuel [type]` | Get fuel pricing and availability |
| `/compare [scenarios]` | Compare project configurations |

## Financial Model Template

### Standard X-150 Model Structure

```
INPUTS:
├── Project Parameters
│   ├── Project life: 20 years
│   ├── Construction: 12 months
│   ├── Operating hours: 8,300/year
│   └── Currency: EUR
├── CAPEX
│   ├── X-150 unit: €500,000
│   ├── Installation: €100,000
│   ├── Grid connection: €100,000
│   ├── CHP/Trigeneration: €80,000
│   ├── CCM (if applicable): €150,000
│   └── Contingency (10%): €93,000
├── OPEX (Annual)
│   ├── Fuel: €50,000 (variable)
│   ├── Labor: €30,000 (fixed)
│   ├── Maintenance: €35,000 (mixed)
│   ├── Insurance: €10,000 (fixed)
│   └── Admin: €10,000 (fixed)
├── Revenues (Annual)
│   ├── Electricity: €180,000
│   ├── Heat: €150,000 (if CHP)
│   ├── Cooling: €150,000 (if trigeneration)
│   ├── Biochar: €200,000
│   └── Carbon credits: €100,000
└── Financing
    ├── Debt/equity ratio: 70/30
    ├── Interest rate: 6%
    ├── Tenor: 12 years
    └── DSCR requirement: 1.25x

OUTPUTS:
├── Returns
│   ├── Project IRR: XX%
│   ├── Equity IRR: XX%
│   ├── NPV (10%): €XXX,XXX
│   └── Payback: X.X years
├── Coverage
│   ├── Min DSCR: X.XX
│   ├── Avg DSCR: X.XX
│   └── LLCR: X.XX
├── Metrics
│   ├── LCOE: €0.XX/kWh
│   ├── Cost per tonne CO2: €XX
│   └── Revenue per MWh: €XXX
└── Ranking: X/10
```

## Fuel & Feedstock Pricing Database

### Biomass Fuels (EUR/tonne, delivered)

| Fuel Type | Low | Base | High | Energy Content | Availability |
|-----------|-----|------|------|----------------|--------------|
| Wood Pellets | €180 | €220 | €280 | 4.8 MWh/t | High (EU) |
| Wood Chips | €80 | €120 | €160 | 3.5 MWh/t | High (local) |
| Olive Pomace | €40 | €60 | €90 | 3.0 MWh/t | Med (Mediterranean) |
| Palm Kernel Shells | €50 | €80 | €120 | 4.0 MWh/t | High (tropics) |
| Coconut Shells | €60 | €90 | €130 | 4.2 MWh/t | Med (coastal) |
| Rice Husks | €20 | €40 | €70 | 3.0 MWh/t | High (Asia) |
| Bagasse | €10 | €25 | €50 | 2.0 MWh/t | High (sugar regions) |
| Sawdust | €30 | €50 | €80 | 3.5 MWh/t | High (forestry) |
| RDF (Refuse Derived Fuel) | -€30 | -€10 | €20 | 4.0 MWh/t | High (urban) |
| Sewage Sludge | -€50 | -€30 | -€10 | 2.5 MWh/t | High (wastewater plants) |

**Negative prices = gate fees (you get paid to take the waste)**

### Waste Disposal Gate Fees (EUR/tonne)

| Waste Type | Gate Fee Range | Notes |
|------------|----------------|-------|
| Wood waste (clean) | €20-50 | Construction, pallets |
| Agricultural residues | €10-30 | Straw, husks |
| Food processing waste | €40-100 | Depends on moisture |
| Industrial sludge | €80-200 | Dewatering required |
| RDF/SRF | -€20-€30 | You get paid |
| Mixed waste | €50-150 | Pre-processing needed |

## Revenue Pricing Benchmarks

### Electricity (EUR/kWh)

| Market | Industrial | Commercial | Residential | Notes |
|--------|------------|------------|-------------|-------|
| Germany | €0.18-0.25 | €0.22-0.30 | €0.30-0.40 | High grid fees |
| France | €0.12-0.18 | €0.15-0.22 | €0.20-0.28 | Nuclear baseload |
| Italy | €0.15-0.22 | €0.18-0.28 | €0.25-0.35 | High prices |
| Spain | €0.10-0.16 | €0.13-0.20 | €0.18-0.28 | Solar competition |
| Netherlands | €0.14-0.20 | €0.17-0.25 | €0.22-0.32 | Grid constraints |
| UK | £0.12-0.18 | £0.15-0.25 | £0.20-0.35 | CfD available |
| Ghana | $0.08-0.15 | $0.12-0.20 | $0.15-0.30 | Diesel baseline |
| Nigeria | $0.10-0.20 | $0.15-0.30 | $0.20-0.40 | Grid unreliable |

### Heat (EUR/kWhth)

| Application | Price Range | Notes |
|-------------|-------------|-------|
| District heating | €0.03-0.06 | Long-term contracts |
| Industrial process | €0.04-0.10 | Steam or hot water |
| Greenhouse heating | €0.03-0.08 | Seasonal demand |
| Drying applications | €0.05-0.12 | High temperature premium |

### Cooling (EUR/kWhc)

| Application | Price Range | COP Impact |
|-------------|-------------|------------|
| Data centers | €0.08-0.15 | High value, baseload |
| Commercial AC | €0.06-0.12 | Seasonal variation |
| Industrial process | €0.05-0.10 | Continuous demand |
| Cold storage | €0.04-0.08 | 24/7 operation |

### Biochar (EUR/tonne)

| Quality | Bulk | Premium | Notes |
|---------|------|---------|-------|
| Uncertified | €150-250 | - | Basic agricultural use |
| EBC-Basic | €250-400 | €450-600 | Standard certification |
| EBC-Agro | €400-600 | €700-900 | Premium agricultural |
| EBC-AgroOrganic | €600-900 | €1000-1500 | Organic farming |
| Activated | - | €2000-5000 | Water filtration |

### Carbon Credits (EUR/tonne CO2)

| Market | Price Range | Notes |
|--------|-------------|-------|
| EU ETS | €60-100 | Compliance market |
| Puro.earth CORC | €80-150 | Biochar carbon removal |
| Verra VCS | €5-15 | Voluntary market |
| Gold Standard | €10-25 | Premium voluntary |
| CORSIA | €5-20 | Aviation offset |

## Optimization Algorithms

### Fuel Blend Optimization

**Objective:** Minimize cost per MWh while meeting ash/moisture constraints

```python
# Pseudo-code
minimize: total_fuel_cost
subject to:
  - moisture_content < 15%
  - ash_content < 5%
  - energy_density > 3.5 MWh/t
  - supply_security > 90%
  - blend_ratio_constraints
```

### Output Mix Optimization

**Objective:** Maximize revenue given heat/cooling demand constraints

```python
# Pseudo-code
maximize: total_revenue
subject to:
  - electrical_output <= 150 kWe
  - thermal_output <= 350 kWth
  - cooling_output <= 262 kWc (if trigeneration)
  - demand_constraints
  - equipment_efficiency
```

## Bankability Checklist

### Technical Bankability
- [ ] Technology proven (1,000+ hours operation)
- [ ] O&M plan documented
- [ ] Fuel supply secured (contract or abundant local source)
- [ ] Grid connection agreement (if applicable)
- [ ] Environmental permits obtained
- [ ] Insurance available

### Commercial Bankability
- [ ] Offtake agreement (PPA, heat purchase, etc.)
- [ ] Creditworthy counterparty
- [ ] Price escalation mechanisms
- [ ] Term matching project life
- [ ] Take-or-pay provisions (if applicable)

### Financial Bankability
- [ ] Min DSCR > 1.25x
- [ ] Avg DSCR > 1.40x
- [ ] LLCR > 1.35x
- [ ] Equity IRR > 15%
- [ ] Payback < 7 years
- [ ] Positive NPV at 10% discount

## Sensitivity Analysis Framework

### Key Variables to Test

| Variable | Base Case | Range | Impact |
|----------|-----------|-------|--------|
| Fuel price | €100/t | ±30% | HIGH |
| Electricity price | €0.15/kWh | ±25% | HIGH |
| Operating hours | 8,300h | ±10% | MEDIUM |
| CAPEX | €1,000,000 | ±15% | MEDIUM |
| Carbon credit price | €100/t | ±50% | MEDIUM |
| Interest rate | 6% | ±2% | MEDIUM |
| Maintenance cost | €50,000/y | ±25% | LOW |

### Tornado Diagram Construction

1. Run base case → record NPV
2. Vary each variable ±20%
3. Calculate NPV impact for each
4. Sort by absolute impact
5. Visualize as horizontal bars

## Discounted Cash Flow (DCF) Formula

```
NPV = Σ (CFt / (1 + r)^t) for t = 0 to n

Where:
- CFt = Cash flow in year t
- r = Discount rate (WACC or hurdle rate)
- t = Year (0 = construction, 1 = first operation)
- n = Project life (20 years)

IRR: The discount rate where NPV = 0

Payback: Year when cumulative cash flow turns positive
```

## LCOE Calculation

```
LCOE = (CAPEX × CRF + OPEX_fixed) / Annual_generation + OPEX_variable

Where:
- CRF = Capital Recovery Factor = [r(1+r)^n] / [(1+r)^n - 1]
- r = Discount rate
- n = Economic life
```

## Quick Reference: Project Rankings

### Exceptional (9-10/10)
- Ghana palm oil (gate fees + high power prices)
- Data center trigeneration (premium cooling value)
- Carbon-negative projects (credits + biochar)

### Strong (7-8/10)
- Industrial CHP (stable heat demand)
- District heating (long-term contracts)
- Waste-to-energy (negative fuel cost)

### Acceptable (5-6/10)
- Grid-connected power (market prices)
- Seasonal applications (greenhouses)
- Remote mini-grids (high diesel replacement)

### Marginal (3-4/10)
- Low power price markets
- High fuel cost regions
- Unproven applications

### Poor (1-2/10)
- Competitive grid access
- Expensive biomass transport
- Regulatory uncertainty
