
import random
import time
import os


responses = {
    "cabin": ["cabin status", "carbin level", "let me check cabin", "cabiny", "cb"],
    "altitude": ["altitude status", "altitude level", "let me chack altitude", "alti", "alt"],
    "temperature": ["temperature status", "temperature level", "let me check temperature", "temp", "tp"],
    "oxygen": ["oxygen status", "oxygen level", "let me check oxygen", "ox"],
    "co2": ["co2 status", "co2 level", "let me check co2", "co2"],
    "system": ["system status", "system level", "let me check system", "ss"],
    "radiation": ["radiation status", "radiation level", "let me check radiation", "ch"]
}

cabin_pressure = random.uniform(14.5, 15) # in psi

altitude = random.uniform(0, 100000) # in feet

temperature = random.uniform(18, 25) # in Celsius

oxygen_level = random.uniform(19.5, 20.5) # Percent

co2_levels = random.uniform(0.03, 0.05) # Percent

system_status = random.choice(["Nominal", "Minor Anomaly", "major Anomaly"])

radiation_levels = random.uniform(0, 0.2) # in rad/hour


while True:
    cabin_pressure = random.uniform(14.5, 15) # in psi

    altitude = random.uniform(0, 100000) # in feet

    temperature = random.uniform(18, 25) # in Celsius

    oxygen_level = random.uniform(19.5, 20.5) # Percent

    co2_levels = random.uniform(0.03, 0.05) # Percent

    system_status = random.choice(["Nominal", "Minor Anomaly", "major Anomaly"])

    radiation_levels = random.uniform(0, 0.2) # in rad/hour

    user_input = input("User Text")

    if user_input.lower() == 'exit':
        print("Thank you")
        break

    for key in responses:
            if key in user_input.lower():
                 
                if key == "cabin":
                    chatbot = random.choice(responses[key])
                    print(chatbot)
                    print(f"cabin pressure: {cabin_pressure:.2f} psi")

                elif key == "altitude":
                    chatbot = random.choice(responses[key])
                    print(chatbot)
                    print(f"altitude: {altitude:.2f} feet")

                elif key == "temperature":
                    chatbot = random.choice(responses[key])    
                    print(chatbot)
                    print(f"temperature: {temperature:.2f} celsius")

                elif key == "oxygen":
                    chatbot = random.choice(responses[key])  
                    print(chatbot)
                    print(f"oxygen: {oxygen_level:.2f} percent") 

                elif key == "co2":
                    chatbot = random.choice(responses[key]) 
                    print(chatbot)  
                    print(f"co2: {co2_levels:.2f} percent")

                elif key == "system":
                    chatbot = random.choice(responses[key])
                    print(chatbot) 
                    print(f"system: {system_status}")
                elif key == "radiation":
                    chatbot = random.choice(responses[key])
                    print(f"radiation: {radiation_levels:.2f} rad/hour")

                break
    else:
        print("Bot answer: Please Try Again")