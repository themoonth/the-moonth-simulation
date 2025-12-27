# The Moonth  
A Symbolic–Phenomenological Model of Cyclical Time

**Kamil Wójcik**  
Oslo, Norway / Hrubieszów, Poland  
December 2025  

Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

---

### Core Phenomenological Observation

Human consciousness, when observed under conditions of minimal external stimulation (silence, fasting, sustained attention), organizes itself into recurring cycles of approximately 29 days.

Each cycle consists of **five distinct phases**, and each phase lasts **137 hours**.

**137 hours** — the same numerical value as the denominator of the fine structure constant (α ≈ 1/137.036) — emerges repeatedly as the irreducible temporal quantum of lived experience.

This is not claimed as a physical law, but as a precise symbolic anchor:

**α · Ψ(t) ≈ 1**

The model treats matter (governed by α) and consciousness (structured in 137-hour phases) as reciprocals within the same symbolic framework.

### Buffer Physics and Impedance of Time

Phase transitions are not instantaneous. The system requires time to shift states — an experiential analogue to inductance in electrical circuits.

- Total transition overhead ("buffer"): **11 hours** distributed across the five phase boundaries.
- This creates a natural **impedance of time**: rapid or forced change meets resistance, while aligned pacing flows smoothly.
- The asymmetry (longer rise arc ≈ 18 days, shorter fall ≈ 11 days) reflects golden ratio proportions (18/11 ≈ φ ≈ 1.618).

Together, the 137-hour phase quantum and 11-hour buffer yield one complete symbolic Moonth of **696 hours ≈ 29 days**.

### The Five Phases (Invariant Sequence)

1. **Opening** – Field expands, receptive state, emergence of potential.  
2. **Rise** – Direction crystallizes, momentum builds.  
3. **Expansion** – Peak coherence, maximum flow and expression.  
4. **Descent** – Energy withdraws, release and contraction.  
5. **Integration** – Processing, consolidation, preparation for next cycle.

The sequence is invariant and irreversible within a cycle.

### Dual Symbolic Scaling Systems

- **φ-scaling** (biological/experiential):  
  T(n) = 137h × φⁿ  

- **60-scaling** (civilizational/historical):  
  T(n) = 137h × 60ⁿ  

Both anchored to the same 137-hour reference quantum.

**Symbolic bridge**:  
137 × φ² / 6 ≈ 60 (relative error ~0.0034 or 0.34%)

### Structural Resonances (Numerical Proximities)

Selected observed rhythms and model-derived values:

| Resonance                  | Observed Value | Calculated Value | Proximity | Domain                  |
|----------------------------|----------------|------------------|-----------|-------------------------|
| BRAC (Basic Rest-Activity Cycle) | 90 minutes     | 92.36 minutes    | 0.97      | Neurophysiology         |
| Menstrual cycle            | 28.5 days      | 28.54 days       | 0.99      | Reproductive biology    |
| Human gestation            | 268 days       | 264 days         | 0.96      | Human development       |
| Generational cycle         | 29 years       | 29 years         | 1.00      | Generational time       |

These are presented as candidates for symbolic alignment, not empirical proofs.

### Operational Principles (Leges Undecim)

1. **Cyclicity** – Experience unfolds in recurring cycles independent of calendars.  
2. **Quantization** – The cycle is modeled as five phases of ~137h each.  
3. **Asymmetry** – Expansion and contraction are not symmetric.  
4. **Conservation** – Energy redistributed across the cycle balances out.  
5. **Transition** – Phase changes require time and cannot be instantaneous.  
6. **Resonance** – Individual cycles may align with larger rhythms.  
7. **Invariance** – Phase order does not change within a cycle.  
8. **Scalability** – The same pattern can model multiple time scales.  
9. **Perturbation** – External stress shifts timing but not structure.  
10. **Integration** – Completion of a cycle yields consolidation.  
11. **Interpretation** – Meaning arises from use, not assertion.

### Python Implementation

```python
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                  THE MOONTH SOURCE CODE                                      ║
║                                                                              ║
║         A Symbolic–Phenomenological Model of Cyclical Time                   ║
║                                                                              ║
║                           α · Ψ(t) ≈ 1                                        ║
║                                                                              ║
║  This code does NOT claim physical laws or empirical proof.                  ║
║  It encodes a symbolic structure designed to model recurring                 ║
║  temporal regularities observed across lived experience,                     ║
║  biological rhythms, and historical measurement systems.                     ║
║                                                                              ║
║  The structure was constructed as a lens — not discovered as fact.           ║
║                                                                              ║
║                          Kamil Wójcik · 2025                                 ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import math
from enum import Enum
from dataclasses import dataclass
from typing import List

# PART I: SYMBOLIC CONSTANTS
class KernelConstants:
    """Symbolic anchors used throughout the model."""
    ALPHA_INVERSE = 137.036
    ALPHA = 1 / ALPHA_INVERSE
    PHI = (1 + math.sqrt(5)) / 2
    PHI_SQUARED = PHI ** 2
    PHI_INVERSE = 1 / PHI
    N_PHASES = 5

    @classmethod
    def coherence_check_60_bridge(cls):
        """Symbolic proximity between α⁻¹, φ², and base-60."""
        calculated = cls.ALPHA_INVERSE * cls.PHI_SQUARED / 6
        return {
            "expression": "137 × φ² / 6",
            "result": round(calculated, 4),
            "reference": 60,
            "relative_error": round(abs(calculated - 60) / 60, 4),
        }

# PART II: SCALING SYSTEMS
class ScalingSystem:
    @staticmethod
    def phi_scale(n: int, base_hours: float = 137.0) -> dict:
        hours = base_hours * (KernelConstants.PHI ** n)
        return {
            "n": n,
            "hours": hours,
            "days": hours / 24,
            "years": hours / (24 * 365.25),
        }

    @staticmethod
    def sexagesimal_scale(n: int, base_hours: float = 137.0) -> dict:
        hours = base_hours * (60 ** n)
        return {
            "n": n,
            "hours": hours,
            "days": hours / 24,
            "years": hours / (24 * 365.25),
        }

# PART III: STRUCTURAL RESONANCES
@dataclass
class StructuralResonance:
    name: str
    observed_value: float
    calculated_value: float
    unit: str
    proximity: float
    domain: str

class StructuralResonances:
    CANDIDATES: List[StructuralResonance] = [
        StructuralResonance("BRAC", 90, 92.36, "minutes", 0.97, "Neurophysiology"),
        StructuralResonance("Menstrual Cycle", 28.5, 28.54, "days", 0.99, "Reproductive biology"),
        StructuralResonance("Gestational Duration", 268, 264, "days", 0.96, "Human development"),
        StructuralResonance("Generational Cycle", 29, 29, "years", 1.0, "Generational time"),
    ]

# PART IV: PHASE STATE MACHINE
class Phase(Enum):
    OPENING = 1
    RISE = 2
    EXPANSION = 3
    DESCENT = 4
    INTEGRATION = 5

class PhaseStateMachine:
    PHASE_QUANTUM = 137.0  # hours
    BUFFER_TOTAL = 11.0    # hours

    TRANSITION_IMPEDANCE = {
        (Phase.OPENING, Phase.RISE): 2.0,
        (Phase.RISE, Phase.EXPANSION): 3.0,
        (Phase.EXPANSION, Phase.DESCENT): 1.0,
        (Phase.DESCENT, Phase.INTEGRATION): 4.0,
        (Phase.INTEGRATION, Phase.OPENING): 1.0,
    }

    @classmethod
    def calculate_cycle_duration(cls) -> dict:
        total_hours = 5 * cls.PHASE_QUANTUM + cls.BUFFER_TOTAL
        return {
            "total_hours": total_hours,
            "total_days": round(total_hours / 24, 2),
            "description": "One symbolic Moonth cycle",
        }

# PART V: OPERATIONAL PRINCIPLES
class LegesUndecim:
    LAWS = {
        "Cyclicity": "Experience unfolds in recurring cycles independent of calendars.",
        "Quantization": "The cycle is modeled as five phases of ~137h each.",
        "Asymmetry": "Expansion and contraction are not symmetric.",
        "Conservation": "Energy redistributed across the cycle balances out.",
        "Transition": "Phase changes require time and cannot be instantaneous.",
        "Resonance": "Individual cycles may align with larger rhythms.",
        "Invariance": "Phase order does not change within a cycle.",
        "Scalability": "The same pattern can model multiple time scales.",
        "Perturbation": "External stress shifts timing but not structure.",
        "Integration": "Completion of a cycle yields consolidation.",
        "Interpretation": "Meaning arises from use, not assertion.",
    }


---

### Closing Note

This model is offered as a practical lens for self-observation and timing. It invites personal testing and further exploration, not acceptance as objective truth.

The structure was constructed to illuminate recurring patterns — its value lies in use.

— Kamil Wójcik  
December 2025
