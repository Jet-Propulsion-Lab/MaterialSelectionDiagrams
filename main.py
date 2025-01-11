from matplotlib import pyplot as plot
import numpy as np
from units import Convert, CompositeUnit, ROOM_TEMP_STANDARD_C, ROOM_PRESSURE_STANDARD_PA
import argparse
import os

# Define the command line arguments
parser = argparse.ArgumentParser(description='Make a material selection diagram')
parser.add_argument('--verbosity', '-v', type=int, default=0, help='How much information to print')
parser.add_argument('--out', '-o', type=str, default='display', help='Output file name (displays if not specified)')
parser.add_argument('--independent', '-x', type=str, default='Yield Strength', help='Independent variable')
parser.add_argument('--dependent', '-y', type=str, default='Density', help='Dependent variable')
parser.add_argument('--title', '-t', type=str, default='Material Selection Diagram', help='Title of the plot')
args = parser.parse_args()

# Open all available materials
class Characteristic:
    def __init__(self, Name, Value, Max, Min, Unit, TemperatureMax, TemperatureMin,  PressureMax, PressureMin):
        self.Name = Name
        self.Value = Value
        self.Max = Max
        self.Min = Min
        self.Unit = Unit
        self.TemperatureMax = TemperatureMax
        self.PressureMax = PressureMax
        self.TemperatureMin = TemperatureMin
        self.PressureMin = PressureMin
        

class Material:
    def __init__(self, filename, Category="NA"):
        self.Category = Category
        self.Type = "NA"
        self.Name = "NA"
        self.CostKG = "NA"
        self.CostM3 = "NA"
        self.CostCM3 = "NA"
        self.AvailibilityScore = "NA"
        self.Characteristics = {}

        with open(filename, 'r') as file:
            data = file.readlines()
            for line in data:
                line = line.strip()
                if line.startswith("Type,"):
                    self.Type = line.split(",")[1].strip()
                if line.startswith("Name,"):
                    self.Name = line.split(",")[1].strip()
                if line.startswith("Cost/kg,"):
                    self.CostKG = float(line.split(",")[1].strip())
                if line.startswith("Cost/m^3,"):
                    self.CostM3 = float(line.split(",")[1].strip())
                if line.startswith("Cost/cm^3,"):
                    self.CostCM3 = float(line.split(",")[1].strip())
                if line.startswith("Characteristic,"):
                    parts = line.split(",")
                    Name = parts[1].strip()
                    Value = float(parts[2].strip())
                    Max = Value + float(parts[3].strip())
                    Min = Value - float(parts[3].strip())
                    Unit = parts[4].strip()
                    TemperatureMin = float(parts[5].strip()) if parts[5].strip() != "RT" else ROOM_TEMP_STANDARD_C
                    TemperatureMax = float(parts[6].strip()) if parts[6].strip() != "RT" else ROOM_TEMP_STANDARD_C
                    PressureMin = float(parts[7].strip()) if parts[7].strip() != "RP" else ROOM_PRESSURE_STANDARD_PA
                    PressureMax = float(parts[8].strip()) if parts[8].strip() != "RP" else ROOM_PRESSURE_STANDARD_PA
                    self.Characteristics[Name] = Characteristic(Name, Value, Max, Min, Unit, TemperatureMax, TemperatureMin, PressureMax, PressureMin)
                if line.startswith("Availibility Score,"):
                    self.AvailibilityScore = int(line.split(",")[1].strip())

# Open all materials in the /Materials and /Materials/[Category] directory
Materials = []
for file in os.listdir("Materials"):
    if file.endswith(".Mat") or file.endswith(".mat"):
        Materials.append(Material("Materials/" + file))
    
    if os.path.isdir("Materials/" + file):
        for subfile in os.listdir("Materials/" + file):
            if subfile.endswith(".Mat") or subfile.endswith(".mat"):
                Materials.append(Material("Materials/" + file + "/" + subfile, file))

# Create the plot
plot.figure()
plot.title(args.title)
plot.grid(True)
x =     [m.Characteristics[args.independent].Value for m in Materials]
y =     [m.Characteristics[args.dependent].Value for m in Materials]
plot.xlabel(args.independent + " (" + Materials[0].Characteristics[args.independent].Unit + ")")
plot.ylabel(args.dependent + " (" + Materials[0].Characteristics[args.dependent].Unit + ")")
labels = [m.Name for m in Materials]
plot.scatter(x, y)

rotation = 20
offset_x = 5  # Adjust the offset as needed
offset_y = 5  # Adjust the offset as needed

for i in range(len(x)):
    text_obj = plot.text(x[i] + offset_x, y[i] + offset_y, labels[i], fontsize=10, rotation=rotation)

# Show if out is display otherwise save the file in /Output
if args.out == 'display':
    plot.show()
else:
    plot.savefig("Output/" + args.out + ".png")