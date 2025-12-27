"""
The Moonth: A Symbolic–Phenomenological Model of Cyclical Time
Python Implementation
Author: Kamil Wójcik, December 2025
License: CC BY 4.0
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