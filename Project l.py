
import random
import time
import os


while True:
        
        os.system('cls' if os.name == 'nt' else 'clear')

        cabin_pressure = random.uniform(14.5, 15) # in psi

        altitude = random.uniform(0, 100000) # in feet

        temperature = random.uniform(18, 25) # in Celsius

        oxygen_level = random.uniform(19.5, 20.5) # Percent

        co2_levels = random.uniform(0.03, 0.05) # Percent

        system_status = random.choice(["Nominal", "Minor Anomaly", "major Anomaly"])

        radiation_levels = random.uniform(0, 0.2) # in rad/hour


        print(f"Cabin pressure: {cabin_pressure:.2f} psi")

        print(f"Altitude: {altitude:.2f} feet")

        print(f"Temperature: {temperature:.2f} Celsius")

        print(f"Oxygen_levels: {oxygen_level:.2f} percent")

        print(f"co2_Levels: {co2_levels:.2f} percent")

        print(f"System Status: {system_status}")

        print(f"Radiation Levels: {radiation_levels:.2f} rad/hour")

        time.sleep(1)