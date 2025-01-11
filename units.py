Conversion_Multiplier_LUT={
    "Pa": {"Pa": 1, "kPa": 1e-3, "MPa": 1e-6, "GPa": 1e-9, "psi": 0.000145038, "bar": 1e-5, "atm": 9.8692e-6},
    "kPa": {"Pa": 1e3, "kPa": 1, "MPa": 1e-3, "GPa": 1e-6, "psi": 0.145038, "bar": 0.01, "atm": 0.0098692},
    "MPa": {"Pa": 1e6, "kPa": 1e3, "MPa": 1, "GPa": 1e-3, "psi": 145.038, "bar": 10, "atm": 9.8692},
    "GPa": {"Pa": 1e9, "kPa": 1e6, "MPa": 1e3, "GPa": 1, "psi": 145038, "bar": 100, "atm": 98.692},
    "psi": {"Pa": 6894.76, "kPa": 6.89476, "MPa": 0.00689476, "GPa": 0.00000689476, "psi": 1, "bar": 0.0689476, "atm": 0.068046},
    "bar": {"Pa": 1e5, "kPa": 100, "MPa": 0.1, "GPa": 0.0001, "psi": 14.5038, "bar": 1, "atm": 0.986923},
    "atm": {"Pa": 101325, "kPa": 101.325, "MPa": 0.101325, "GPa": 0.000101325, "psi": 14.6959, "bar": 1.01325, "atm": 1},
    "kJ": {"kJ": 1, "J": 1000, "cal": 238.846, "kcal": 0.238846, "Wh": 0.277778, "kWh": 0.000277778},
    "J": {"kJ": 0.001, "J": 1, "cal": 0.238846, "kcal": 0.000238846, "Wh": 0.000277778, "kWh": 0.000000277778},
    "cal": {"kJ": 0.004184, "J": 4.184, "cal": 1, "kcal": 0.001, "Wh": 0.00116222, "kWh": 0.00000116222},
    "kcal": {"kJ": 4.184, "J": 4184, "cal": 1000, "kcal": 1, "Wh": 1.16222, "kWh": 0.00116222},
    "Wh": {"kJ": 3.6, "J": 3600, "cal": 859.845, "kcal": 0.859845, "Wh": 1, "kWh": 0.001},
    "kWh": {"kJ": 3600, "J": 3600000, "cal": 859845, "kcal": 859.845, "Wh": 1000, "kWh": 1},
    "C": {"C": 1, "K": 1, "F": 1.8},
    "K": {"C": 1, "K": 1, "F": 1.8},
    "F": {"C": 0.555556, "K": 0.555556, "F": 1},
    "μm": {"μm": 1, "mm": 0.001, "cm": 0.0001, "m": 1e-6, "in": 3.93701e-5, "ft": 3.28084e-6, "yd": 1.09361e-6},
    "mm": {"μm": 1000, "mm": 1, "cm": 0.1, "m": 0.001, "in": 0.0393701, "ft": 0.00328084, "yd": 0.00109361},
    "cm": {"μm": 10000, "mm": 10, "cm": 1, "m": 0.01, "in": 0.393701, "ft": 0.0328084, "yd": 0.0109361},
    "m": {"μm": 1e6, "mm": 1000, "cm": 100, "m": 1, "in": 39.3701, "ft": 3.28084, "yd": 1.09361},
    "in": {"μm": 25400, "mm": 25.4, "cm": 2.54, "m": 0.0254, "in": 1, "ft": 0.0833333, "yd": 0.0277778},
    "ft": {"μm": 304800, "mm": 304.8, "cm": 30.48, "m": 0.3048, "in": 12, "ft": 1, "yd": 0.333333},
    "yd": {"μm": 914400, "mm": 914.4, "cm": 91.44, "m": 0.9144, "in": 36, "ft": 3, "yd": 1},
    "kg": {"kg": 1, "g": 1000, "mg": 1e6, "lb": 2.20462, "oz": 35.274},
    "g": {"kg": 0.001, "g": 1, "mg": 1000, "lb": 0.00220462, "oz": 0.035274},
    "mg": {"kg": 1e-6, "g": 0.001, "mg": 1, "lb": 2.20462e-6, "oz": 3.5274e-5},
    "lb": {"kg": 0.453592, "g": 453.592, "mg": 453592, "lb": 1, "oz": 16},
    "Ω": {"Ω": 1, "kΩ": 0.001, "MΩ": 1e-6, "GΩ": 1e-9},
    "kΩ": {"Ω": 1000, "kΩ": 1, "MΩ": 0.001, "GΩ": 1e-6},
    "MΩ": {"Ω": 1e6, "kΩ": 1000, "MΩ": 1, "GΩ": 0.001},
    "GΩ": {"Ω": 1e9, "kΩ": 1e6, "MΩ": 1000, "GΩ": 1},
}

Conversion_Offset_LUT={
    "C": {"C": 0, "K": 273.15, "F": 32},
    "K": {"C": -273.15, "K": 0, "F": -459.67},
    "F": {"C": -17.7778, "K": 255.372, "F": 0},
}

ROOM_TEMP_STANDARD_C = 20
ROOM_PRESSURE_STANDARD_PA = 101325

class CompositeUnit:
    def __init__(self, NumeratorUnits, DenominatorUnits):
        self.NumeratorUnits = NumeratorUnits
        self.DenominatorUnits = DenominatorUnits

def Convert(value, unit, target_unit):

    if isinstance(unit, CompositeUnit):
        NewVal = value
        for u, tU in zip(unit.NumeratorUnits, unit.DenominatorUnits):
            NewVal = Convert(NewVal, u, tU)
        for u, tU in zip(unit.NumeratorUnits, unit.DenominatorUnits):
            NewVal = Convert(NewVal, u, target_unit)

        return NewVal

    if(unit not in Conversion_Multiplier_LUT or target_unit not in Conversion_Multiplier_LUT[unit]):
        raise ValueError("NO VALID CONVERSION FROM " + unit + " TO " + target_unit)
    
    if(unit in Conversion_Offset_LUT and target_unit in Conversion_Offset_LUT[unit]):
        return (value + Conversion_Offset_LUT[unit][target_unit]) * Conversion_Multiplier_LUT[unit][target_unit]
    else:
        return value * Conversion_Multiplier_LUT[unit][target_unit]
    