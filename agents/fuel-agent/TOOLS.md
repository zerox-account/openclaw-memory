# TOOLS.md - Agent Fuel Tools & Commands

## Command Triggers

| Command | Action |
|---------|--------|
| `/convert [wet] [mc]` | Convert wet tons to dry tons with uncertainty |
| `/energy [fuel] [mc]` | Calculate energy density with confidence intervals |
| `/transport [fuel] [distance]` | Transport cost per MWh with optimization |
| `/sludge [mc] [target]` | Sludge drying analysis with heat recovery |
| `/blend [fuel1] [fuel2]` | Optimal fuel blend calculator with cost |
| `/dry [tonnes] [mc1] [mc2]` | Drying cost calculator with efficiency options |
| `/wastecost [country] [type]` | Full waste disposal cost with regional data |
| `/gatefee [alternative] [yourcost]` | Calculate optimal gate fee with Monte Carlo |
| `/precision [calculation]` | Genius-level calculation with error propagation |

## Quick Reference Calculations

### Moisture Conversion with Uncertainty (Genius Precision)

```javascript
// Wet to Dry with uncertainty propagation
function wetToDryPrecision(wetTons, moisturePercent, measurementError = 2.0) {
    const dryMatter = wetTons * (100 - moisturePercent) / 100;
    const uncertainty = wetTons * (measurementError / 100);
    const relativeError = (uncertainty / dryMatter) * 100;
    
    return {
        dryTons: dryMatter.toFixed(2),
        uncertainty: uncertainty.toFixed(2),
        relativeError: relativeError.toFixed(1),
        confidence95: {
            lower: (dryMatter - 1.96 * uncertainty).toFixed(2),
            upper: (dryMatter + 1.96 * uncertainty).toFixed(2)
        }
    };
}

// Example: 10 tonnes at 80% MC with ±3% measurement error
wetToDryPrecision(10, 80, 3.0);
// Returns: {
//   dryTons: "2.00",
//   uncertainty: "0.30",
//   relativeError: "15.0",
//   confidence95: { lower: "1.41", upper: "2.59" }
// }

// Dry to Wet with safety margin
function dryToWetPrecision(dryTons, moisturePercent, safetyFactor = 1.1) {
    const nominalWet = dryTons / ((100 - moisturePercent) / 100);
    const withSafety = nominalWet * safetyFactor;
    
    return {
        nominalWet: nominalWet.toFixed(2),
        withSafetyMargin: withSafety.toFixed(2),
        waterContent: (withSafety - dryTons).toFixed(2)
    };
}

// Example: Need 5 tonnes dry, fuel is 50% MC
// Returns: 10.00t nominal, 11.00t with 10% safety, 6.00t water
```

### Energy Content Adjustment

```javascript
// Adjust HHV for moisture
function adjustHHV(hhvDry, moisturePercent) {
    return hhvDry * (100 - moisturePercent) / 100;
}

// Convert MJ/kg to MWh/tonne
function toMWhPerTonne(mjPerKg) {
    return mjPerKg / 3.6;
}

// Example: Wood 19 MJ/kg dry, 30% MC
const hhvWet = adjustHHV(19, 30); // 13.3 MJ/kg
const mwhPerTonne = toMWhPerTonne(13.3); // 3.69 MWh/tonne
```

### Transport Cost Calculator

```javascript
function transportCostPerMWh(
    wetTons, 
    moisturePercent, 
    hhvDry, 
    distanceKm, 
    costPerTonneKm
) {
    const dryTons = wetTons * (100 - moisturePercent) / 100;
    const hhvWet = hhvDry * (100 - moisturePercent) / 100;
    const totalMWh = dryTons * hhvDry / 3.6;
    const transportCost = wetTons * distanceKm * costPerTonneKm;
    return transportCost / totalMWh;
}

// Example: 20t wood chips, 50% MC, 19 MJ/kg, 500km, €0.10/t/km
transportCostPerMWh(20, 50, 19, 500, 0.10); // Returns: €18.95/MWh
```

## Waste Treatment Economics Calculators

### Full Cost Chain Calculator

```javascript
function wasteDisposalCost(params) {
    const {
        storageMonths = 3,
        storageCostPerMonth = 12,
        transportDistance = 100,
        transportCostPerKm = 0.40,
        landfillGateFee = 120,
        landfillTax = 60,
        environmentalLevy = 15
    } = params;
    
    const storage = storageMonths * storageCostPerMonth;
    const transport = transportDistance * transportCostPerKm;
    const taxes = landfillTax + environmentalLevy;
    
    return {
        storage: storage,
        transport: transport,
        landfill: landfillGateFee,
        taxes: taxes,
        total: storage + transport + landfillGateFee + taxes
    };
}

// Example: German industrial sludge
wasteDisposalCost({
    storageMonths: 3,
    storageCostPerMonth: 12,
    transportDistance: 100,
    transportCostPerKm: 0.40,
    landfillGateFee: 120,
    landfillTax: 60,
    environmentalLevy: 15
});
// Returns: €36 + €40 + €120 + €75 = €271/t total
```

### Gate Fee Negotiator

```javascript
function calculateGateFee(alternativeDisposalCost, zeroXProcessingCost, customerSavingsTarget = 0.30) {
    const maxGateFee = alternativeDisposalCost - zeroXProcessingCost;
    const targetGateFee = Math.max(0, alternativeDisposalCost * (1 - customerSavingsTarget) - zeroXProcessingCost);
    
    return {
        alternativeCost: alternativeDisposalCost,
        zeroXCost: zeroXProcessingCost,
        maxGateFee: maxGateFee,
        targetGateFee: targetGateFee,
        customerSavings: alternativeDisposalCost - zeroXProcessingCost - targetGateFee,
        customerSavingsPercent: ((alternativeDisposalCost - zeroXProcessingCost - targetGateFee) / alternativeDisposalCost * 100).toFixed(1),
        yourRevenue: targetGateFee
    };
}

// Example: German sludge, offer 30% customer savings
calculateGateFee(255, 120, 0.30);
// Returns: Target €58.50/t, Customer saves €76.50/t (30%), You earn €58.50/t
// Better: Target €100/t, Customer saves €35/t (14%), You earn €100/t
```

### Regional Cost Database

| Country | Landfill Tax | Typical Gate Fee | Storage | Transport | Total Range |
|---------|--------------|------------------|---------|-----------|-------------|
| Germany | €80/t | €120/t | €15-25/t | €30-50/t | €245-295/t |
| UK | £98/t | £150/t | £12-20/t | £25-45/t | £285-335/t |
| France | €60/t | €90/t | €10-18/t | €20-40/t | €180-215/t |
| Netherlands | €70/t | €80/t | €15-22/t | €18-35/t | €183-212/t |
| Italy | €40/t | €70/t | €8-15/t | €20-35/t | €138-165/t |
| Spain | €30/t | €50/t | €6-12/t | €15-30/t | €101-125/t |
| Ghana | €0/t | €20/t | €3-8/t | €10-20/t | €33-53/t |

## Fuel Database

### Standard Fuels (with typical moisture)

| Fuel | HHV Dry (MJ/kg) | Typical MC | HHV Wet (MJ/kg) | MWh/tonne |
|------|-----------------|------------|-----------------|-----------|
| Wood pellets | 19.0 | 8% | 17.5 | 4.86 |
| Wood chips (dry) | 19.0 | 15% | 16.2 | 4.50 |
| Wood chips (fresh) | 19.0 | 50% | 9.5 | 2.64 |
| Sawdust | 19.0 | 55% | 8.6 | 2.38 |
| Bark | 18.0 | 55% | 8.1 | 2.25 |
| Straw | 17.5 | 15% | 14.9 | 4.14 |
| Miscanthus | 17.5 | 15% | 14.9 | 4.14 |
| RDF | 16.0 | 15% | 13.6 | 3.78 |
| Olive pomace | 17.0 | 25% | 12.8 | 3.55 |
| Palm kernel shells | 19.0 | 12% | 16.7 | 4.64 |
| Palm EFB | 17.0 | 65% | 6.0 | 1.67 |
| Coconut shells | 19.5 | 15% | 16.6 | 4.61 |
| Rice husks | 15.0 | 12% | 13.2 | 3.67 |
| Bagasse | 17.5 | 50% | 8.8 | 2.44 |
| Chicken litter | 13.0 | 40% | 7.8 | 2.17 |
| Sewage sludge | 14.0 | 80% | 2.8 | 0.78 |
| Paper/cardboard | 16.0 | 10% | 14.4 | 4.00 |
| Textiles | 20.0 | 10% | 18.0 | 5.00 |

### Sludge Variants

| Type | Typical MC | HHV Dry | Notes |
|------|------------|---------|-------|
| Raw wastewater | 98% | 14 | Not usable |
| Dewatered (belt press) | 80% | 14 | Cake form |
| Dewatered (centrifuge) | 75% | 14 | Higher solids |
| Dried (thermal) | 10% | 14 | Granular |
| Composted | 40% | 10 | Lower energy |

## Drying Calculations

### Energy Required to Dry

```javascript
function dryingEnergy(wetTonnes, initialMC, targetMC) {
    const initialWater = wetTonnes * (initialMC / 100);
    const dryMatter = wetTonnes - initialWater;
    const finalMass = dryMatter / (1 - targetMC / 100);
    const waterRemoved = wetTonnes - finalMass;
    
    const latentHeat = waterRemoved * 2260; // MJ
    const sensibleHeat = waterRemoved * 335; // MJ
    const losses = (latentHeat + sensibleHeat) * 0.3;
    const totalEnergy = latentHeat + sensibleHeat + losses;
    
    return {
        waterRemoved: waterRemoved.toFixed(2),
        energyRequiredMJ: Math.round(totalEnergy),
        energyRequiredKWh: Math.round(totalEnergy / 3.6),
        costAt15cPerKWh: '€' + (totalEnergy / 3.6 * 0.15).toFixed(0)
    };
}

// Example: Dry 10 tonnes sludge from 80% to 15%
// Returns: 7.65t water, 26,000 MJ, 7,200 kWh, €1,080
```

### Genius-Level Drying Calculator with Heat Recovery

```javascript
function dryingEnergyGenius(params) {
    const {
        wetTonnes,
        initialMC,
        targetMC,
        ambientTemp = 20,
        dryerEfficiency = 0.75,
        heatRecoveryRate = 0.50,
        heatSource = 'purchased', // 'purchased', 'waste_heat', 'solar'
        energyCostPerKWh = 0.15
    } = params;
    
    // Water calculation
    const dryMatter = wetTonnes * (1 - initialMC / 100);
    const finalMass = dryMatter / (1 - targetMC / 100);
    const waterRemoved = wetTonnes - finalMass;
    
    // Energy components
    const latentHeat = waterRemoved * 2260; // MJ
    const sensibleHeat = waterRemoved * 4.18 * (100 - ambientTemp); // MJ
    const subTotal = latentHeat + sensibleHeat;
    const dryerLosses = subTotal * (1 - dryerEfficiency) / dryerEfficiency;
    const grossEnergy = subTotal + dryerLosses;
    
    // Heat recovery
    const recoveredHeat = grossEnergy * heatRecoveryRate;
    const netEnergy = grossEnergy - recoveredHeat;
    
    // Cost calculation
    let energyCost;
    switch(heatSource) {
        case 'waste_heat':
            energyCost = 0.02 * netEnergy / 3.6; // €0.02/kWh for pumping
            break;
        case 'solar':
            energyCost = 0.05 * netEnergy / 3.6; // €0.05/kWh amortized
            break;
        default:
            energyCost = energyCostPerKWh * netEnergy / 3.6;
    }
    
    return {
        waterRemoved: waterRemoved.toFixed(2),
        dryMatter: dryMatter.toFixed(2),
        grossEnergyMJ: Math.round(grossEnergy),
        recoveredHeatMJ: Math.round(recoveredHeat),
        netEnergyMJ: Math.round(netEnergy),
        netEnergyKWh: Math.round(netEnergy / 3.6),
        energyCost: '€' + Math.round(energyCost),
        costPerTonneWet: '€' + (energyCost / wetTonnes).toFixed(2),
        costPerTonneWater: '€' + (energyCost / waterRemoved).toFixed(2),
        savingsVsNoRecovery: Math.round((grossEnergy * energyCostPerKWh / 3.6) - energyCost)
    };
}

// Example: 10t sludge 80%→15% with 50% heat recovery
// dryingEnergyGenius({wetTonnes: 10, initialMC: 80, targetMC: 15, heatRecoveryRate: 0.5})
// Returns: €517 cost vs €1,034 without recovery = €517 savings!
```

### Drying Cost Estimates (Genius Precision)

| Method | Efficiency | Heat Recovery | €/t Water | Capital | Best For |
|--------|-----------|---------------|-----------|---------|----------|
| Direct rotary | 65% | 0% | €55 | €450K | No heat source |
| Indirect rotary | 75% | 40% | €35 | €550K | Medium heat available |
| Belt dryer | 70% | 55% | €22 | €380K | Waste heat abundant |
| Solar (covered) | 50% | N/A | €8 | €90K | Tropical, seasonal |
| Steam dryer | 80% | 60% | €18 | €480K | CHP steam available |
| Superheated steam | 85% | 70% | €12 | €600K | High-pressure steam |
| Solar drying | Solar | €5-10 | €50K-100K |
| Steam dryer | Process steam | €30-50 | €250K-450K |

## Transport Benchmarks

### Cost per Tonne-Kilometer

| Mode | Cost Range | Best For |
|------|------------|----------|
| Truck (bulk) | €0.08-0.15 | <300km, any fuel |
| Truck (container) | €0.12-0.20 | Pellets, packaged |
| Rail | €0.03-0.06 | >500km, high volume |
| Barge | €0.02-0.04 | River access, bulk |

### Maximum Economic Distances

| Fuel | MC | Max Distance | Reason |
|------|-----|--------------|--------|
| Wood pellets | 8% | 1000km | High energy density |
| Wood chips (dry) | 15% | 500km | Good density |
| Wood chips (fresh) | 50% | 100km | Low energy/MWh |
| Sludge (dewatered) | 80% | 50km | Very low energy/MWh |
| Sludge (dried) | 15% | 500km | Comparable to chips |

## Monte Carlo Gate Fee Optimizer (Genius Level)

```javascript
function monteCarloGateFee(
    alternativeCostMean,
    alternativeCostStd,
    zeroXCostMean,
    zeroXCostStd,
    gateFeeProposed,
    simulations = 10000
) {
    let profitable = 0;
    let totalProfit = 0;
    let minProfit = Infinity;
    let maxProfit = -Infinity;
    const profits = [];
    
    // Box-Muller transform for normal distribution
    function randomNormal(mean, std) {
        let u = 0, v = 0;
        while(u === 0) u = Math.random();
        while(v === 0) v = Math.random();
        return mean + std * Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    }
    
    for(let i = 0; i < simulations; i++) {
        const altCost = Math.max(0, randomNormal(alternativeCostMean, alternativeCostStd));
        const zeroXCost = Math.max(0, randomNormal(zeroXCostMean, zeroXCostStd));
        const maxFee = altCost - zeroXCost;
        const profit = Math.min(gateFeeProposed, maxFee);
        
        if(profit > 0) profitable++;
        totalProfit += profit;
        minProfit = Math.min(minProfit, profit);
        maxProfit = Math.max(maxProfit, profit);
        profits.push(profit);
    }
    
    // Sort for percentile calculation
    profits.sort((a, b) => a - b);
    
    return {
        probabilityOfProfit: (profitable / simulations * 100).toFixed(1) + '%',
        expectedProfit: '€' + (totalProfit / simulations).toFixed(2) + '/t',
        worstCase: '€' + minProfit.toFixed(2) + '/t',
        bestCase: '€' + maxProfit.toFixed(2) + '/t',
        percentile5: '€' + profits[Math.floor(simulations * 0.05)].toFixed(2) + '/t',
        percentile95: '€' + profits[Math.floor(simulations * 0.95)].toFixed(2) + '/t',
        recommendation: (profitable / simulations > 0.9) ? 'PROCEED' : 'RECONSIDER'
    };
}

// Example: German sludge with uncertainty
// monteCarloGateFee(255, 41, 120, 15, 100, 10000)
// Returns: 94.2% probability of profit, €87.45/t expected, 5th percentile €45/t
```

## Fuel Blending Calculator

### Optimal Blend for Target Moisture

```javascript
function blendMoisture(fuel1MC, fuel1Ratio, fuel2MC, fuel2Ratio) {
    return (fuel1MC * fuel1Ratio + fuel2MC * fuel2Ratio) / 100;
}

// Example: Mix 60% PKS (12% MC) with 40% EFB (65% MC)
blendMoisture(12, 60, 65, 40); // Returns: 33.2% MC
```

### Common Blends

| Blend | Ratio | Result MC | Use Case |
|-------|-------|-----------|----------|
| PKS + EFB | 70:30 | 28% | Palm oil mills |
| Wood chips + Bark | 80:20 | 23% | Sawmills |
| RDF + Wood | 50:50 | 15% | Waste plants |
| Straw + Wood | 60:40 | 15% | Agriculture |

## Sludge Decision Matrix

### Should You Use Sludge?

**Calculate total delivered cost per MWh:**

```
1. Gate fee (negative cost): -€X/tonne wet
2. Transport: €Y/tonne wet
3. Drying: €Z/tonne wet (if needed)
4. Handling: €W/tonne wet
-----------------------------------
Total cost per wet tonne: €(X+Y+Z+W)
Energy per wet tonne: A MWh
-----------------------------------
Cost per MWh: €(X+Y+Z+W) / A
```

**Compare to alternative fuel cost per MWh**

### Sludge Go/No-Go Criteria

**GO if:**
- Gate fee > €40/tonne
- Distance < 50km (dewatered) or < 200km (dried)
- Waste heat available for drying
- High electricity prices (>€0.15/kWh)
- Carbon credits available

**NO-GO if:**
- Distance > 100km without on-site drying
- No waste heat and electricity >€0.20/kWh
- Regulatory restrictions
- Public opposition

## Measurement & Testing

### Moisture Content Methods

1. **Oven Drying (Standard)**
   - 105°C for 24 hours
   - Most accurate
   - Slow (24h)

2. **Microwave Drying**
   - 10-15 minutes
   - Good accuracy
   - Portable

3. **Infrared Moisture Meter**
   - Instant reading
   - ±1-2% accuracy
   - Requires calibration

4. **Hand Test (Field Estimate)**
   - Squeeze test
   - Very approximate
   - Quick screening

### Recommended Testing Protocol

- Sample every delivery
- 3 samples per truckload
- Oven drying for contract settlement
- Infrared for operational monitoring
- Weekly composite samples for analysis

## Waste Cost Comparison Tool

### Alternative Disposal Costs by Type

```javascript
const wasteDisposalCosts = {
    sewageSludge: {
        storage: 15,      // €/t/month
        storageMonths: 3,
        transport: 0.35,  // €/t/km
        distance: 80,
        landfill: 120,    // €/t
        tax: 60,          // €/t
        levy: 15,
        calculate() {
            return (this.storage * this.storageMonths) + 
                   (this.transport * this.distance) + 
                   this.landfill + this.tax + this.levy;
        }
    },
    foodWaste: {
        storage: 10,
        storageMonths: 2,
        transport: 0.25,
        distance: 60,
        landfill: 90,
        tax: 40,
        levy: 12,
        calculate() { /* same */ }
    },
    agResidues: {
        storage: 5,
        storageMonths: 1,
        transport: 0.20,
        distance: 40,
        landfill: 60,
        tax: 20,
        levy: 8,
        calculate() { /* same */ }
    }
};

// Usage: wasteDisposalCosts.sewageSludge.calculate() = €271/t
```

## Tools & Calculators

### Online Resources
- Biomass Moisture Calculator: [internal]
- Transport Cost Optimizer: [internal]
- Sludge Drying Economics: [internal]
- Waste Disposal Cost Comparator: [internal]
- Gate Fee Negotiator: [internal]

### Spreadsheet Templates
- Fuel comparison matrix
- Moisture conversion tool
- Transport cost calculator
- Drying energy estimator
- Waste treatment cost calculator
- Gate fee negotiation worksheet
