#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import math

def TempUnits():
    user_input = ''
    while not (user_input == 'c' or user_input == 'f' or user_input == 'k'):
        user_input = input('What are your current units? (Celsius(C),Fahrenheit(F),Kelvin(K)): ').lower()
    return user_input

def MassUnits():
    user_input = ''
    while not (user_input == 'lbs' or user_input == 'g' or user_input == 'oz' or user_input == 'kg'):
        user_input = input('What are your current units? (Pounds(lbs),Grams(g),Ounces(oz),Kilograms(kg)): ').lower()
    return user_input

def CurrencyUnits():
    user_input = ''
    while not (user_input == 'usd' or user_input == 'eur' or user_input == 'cad' or user_input == 'jpy' or user_input == 'gbp' or user_input == 'mxn'):
        user_input = input('What are your currency units? (US Dollar(USD),Euro(EUR),Yen(JPY),British Pound(GBP),Canadian Dollar(CAD), or Mexican Peso(MXN)): ').lower()
    return user_input

def VolumeChoice():
    user_input = ''
    while not (user_input == 'gal' or user_input == 'cf' or user_input == 'qt' or user_input == 'pt' or user_input == 'floz'):
        user_input = input("What are your current units? Gallon(GAL),Pint(PT),Fluid Ounces(FlOz),Quarts(QT), or Cubic feet (CF): ").lower()
    return user_input

def ConversionChoice():
    user = ''
    while not (user == 'c' or user == 't' or user == 'v' or user == 'm'):
        user = input('Convert with Temperature(T), Currency(C), Volume(V), or Mass(M)?: ').lower()
    return user

class Temp():
    def __init__(self,temp):
        self.temp = temp
        
    def CtoF(self):
        print('That temperature in Fahrenheit is...')
        time.sleep(.5)
        return round(((self.temp*9/5)+32),2)
    
    def FtoC(self):
        print('That temperature in Celsius is...')
        time.sleep(.5)
        return round(((self.temp-32)*5/9),2)
    
    def FtoK(self):
        print('That temperature in Kelvin is...')
        time.sleep(.5)
        return round(((self.temp-32) * 5/9 + 273.15),2)
    
    def KtoF(self):
        print('That temperature in Fahrenheit is...')
        time.sleep(.5)
        return round(((self.temp - 273.15) * 9/5 + 32),2)
    
    def CtoK(self):
        print('That temperature in Kelvin is...')
        time.sleep(.5)
        return round((self.temp+273.15),2)
    
    def KtoC(self):
        print('That temperature in Celsius is...')
        time.sleep(.5)
        return round((self.temp-273.15),2)
    
class Mass():
    def __init__(self,mass):
        self.mass = mass
        
    def GramsToPounds(self):
        print('That mass in pounds is... ')
        time.sleep(.5)
        return round((self.mass / 453.592),4)
    
    def GramsToKilograms(self):
        print('That mass in kilograms is...')
        time.sleep(.5)
        return round((self.mass / 1000),3)
    
    def GramsToOunces(self):
        print('That mass in ounces is...')
        time.sleep(.5)
        return round((self.mass / 28.35),4)
    
    def PoundstoGrams(self):
        print('That mass in grams is...')
        time.sleep(.5)
        return round((self.mass * 453.592),3)
    
    def PoundstoKilograms(self):
        print('That mass in kilograms is...')
        time.sleep(.5)
        return round((self.mass / 2.205),4)
    
    def PoundstoOunces(self):
        print('That mass in ounces is...')
        time.sleep(.5)
        return round((self.mass * 16),3)
    
    def KilogramstoPounds(self):
        print('That mass in pounds is...')
        time.sleep(.5)
        return round((self.mass * 2.205),4)
    
    def KilogramstoGrams(self):
        print('That mass in grams is...')
        time.sleep(.5)
        return (self.mass * 1000)
    
    def KilogramstoOunces(self):
        print('That mass in ounces is...')
        time.sleep(.5)
        return round((self.mass * 35.274),3)
    
    def OuncestoGrams(self):
        print('That mass in grams is...')
        time.sleep(.5)
        return round((self.mass * 28.35),3)
    
    def OuncestoPounds(self):
        print('That mass in pounds is...')
        time.sleep(.5)
        return round((self.mass / 16),4)
    
    def OuncestoKilograms(self):
        print('That mass in kilograms is...')
        time.sleep(.5)
        return round((self.mass / 35.274),3)

class Currency():
    def __init__(self,currency):
        self.currency = currency
        
    def USDtoEUR(self):
        print('That currency in Euros is...')
        return round((self.currency * 0.8874),2)
    
    def USDtoJPY(self):
        print('That currency in Yen is... ')
        return round((self.currency * 107.89),2)
    
    def USDtoCAD(self):
        print('That currency in Canadian Dollars is...')
        return round((self.currency * 1.303),2)
    
    def USDtoMXN(self):
        print('That currency in Pesos is...')
        return round((self.currency * 19.01),2)
    
    def USDtoGBP(self):
        print('That currency in British Pounds is...')
        return round((self.currency * 0.7959),2)
    
    def EURtoUSD(self):
        print('That currency in Us Dollars is...')
        return round((self.currency * 1.126),2)
    
    def EURtoJPY(self):
        print('That currency in Yen is...')
        return round((self.currency * 121.57),2)
    
    def EURtoCAD(self):
        print('That currency in Canadian Dollars is...')
        return round((self.currency * 1.469),2)
    
    def EURtoMXN(self):
        print('That currency in Pesos is...')
        return round((self.currency * 21.425411),2)
    
    def EURtoGBP(self):
        print('That currency in British Pounds is...')
        return round((self.currency * 0.896688),2)
    
    def CADtoUSD(self):
        print('That currency in Us Dollars is...')
        return round((self.currency * 0.767196),2)
    
    def CADtoJPY(self):
        print('That currency in Yen is...')
        return round((self.currency * 82.766233),2)
    
    def CADtoEUR(self):
        print('That currency in Euros is...')
        return round((self.currency * 0.680783),2)
    
    def CADtoMXN(self):
        print('That currency in Pesos is...')
        return round((self.currency * 14.581969),2)
    
    def CADtoGBP(self):
        print('That currency in British Pounds is...')
        return round((self.currency * 0.610414),2)
    
    def JPYtoUSD(self):
        print('That currency in Us Dollars is...')
        return round((self.currency * 0.009270),2)
    
    def JPYtoCAD(self):
        print('That currency in Canadian Dollars is...')
        return round((self.currency * 0.012083),2)
    
    def JPYtoEUR(self):
        print('That currency in Euros is...')
        return round((self.currency * 0.008226),2)
    
    def JPYtoMXN(self):
        print('That currency in Pesos is...')
        return round((self.currency * 0.176229),2)
    
    def JPYtoGBP(self):
        print('That currency in British Pounds is...')
        return round((self.currency * 0.007375),2)
    
    def MXNtoUSD(self):
        print('That currency in Us Dollars is...')
        return round((self.currency * 0.052612),2)
    
    def MXNtoCAD(self):
        print('That currency in Canadian Dollars is...')
        return round((self.currency * 0.068560),2)
    
    def MXNtoEUR(self):
        print('That currency in Euros is...')
        return round((self.currency * 0.046676),2)
    
    def MXNtoJPY(self):
        print('That currency in Yen is...')
        return round((self.currency * 5.674150),2)
    
    def MXNtoGBP(self):
        print('That currency in British Pounds is...')
        return round((self.currency * 0.041850),2)
    
    def GBPtoUSD(self):
        print('That currency in Us Dollars is...')
        return round((self.currency * 1.257094),2)
    
    def GBPtoCAD(self):
        print('That currency in Canadian Dollars is...')
        return round((self.currency * 1.638255),2)
    
    def GBPtoEUR(self):
        print('That currency in Euros is...')
        return round((self.currency * 1.115333),2)
    
    def GBPtoJPY(self):
        print('That currency in Yen is...')
        return round((self.currency * 135.577858),2)
    
    
    def GBPtoMXN(self):
        print('That currency in Pesos is...')
        return round((self.currency * 23.891125),2)

def NewCalc(): #restart func
    
    new_calc = input('Recalulate? (Y or N): ').lower()
    
    if new_calc ==  'y':
        
        return 'y'
    else:
        return False
class Volume():
    def __init__(self,volume):
        self.volume = volume
    
    def GALtoCF(self):
        print('That volume in cubic feet is...')
        return round((self.volume / 7.481),4)
    
    def GALtoQT(self):
        print('That volume in quarts is...')
        return round((self.volume * 4),2)
    
    def GALtoPint(self):
        print('That volume in pints is...')
        return round((self.volume * 8),2)
    
    def GALtoOz(self):
        print('That volume in fluid ounces is...')
        return round((self.volume * 128),2)
    
    def CFtoGAL(self):
        print('That volume in gallons is...')
        return round((self.volume * 7.481),2)
    
    def CFtoQT(self):
        print('That volume in quarts is... ')
        return round((self.volume * 29.922),2)
    
    def CFtoPint(self):
        print('That volume in pints is...')
        return round((self.volume * 59.844),3)
    
    def CFtoOZ(self):
        print('That volume in fluid ounces is...')
        return round((self.volume * 957.506),3)
    
    def QTtoGAL(self):
        print('That volume in gallons is...')
        return round((self.volume / 4),2)
    
    def QTtoCF(self):
        print('That volume in cubic feet is... ')
        return round((self.volume / 29.922),2)
    
    def QTtoPint(self):
        print('That volume in pints is...')
        return round((self.volume * 2),2)
    def PinttoGAL(self):
        print('That volume in gallons is...')
        return round((self.volume / 8),2)
    
    def PinttoCF(self):
        print('That volume in cubic feet is...')
        return round((self.volume / 59.844),2)
    
    def PinttoQT(self):
        print('That volume in quarts is...')
        return round((self.volume / 2),2)
                     
    def PinttoOZ(self):
        print('That volume in fluid ounces is...')
        return round((self.volume * 16),2)
    
    def OZtoGAL(self):
        print('That volume in gallons is...')
        return round((self.volume / 128),2)
    
    def OZtoCF(self):
        print('That volume in cubic feet is... ')
        return round((self.volume / 957.506),4)
    
    def OZtoQT(self):
        print('That volume in quarts is...')
        return round((self.volume / 32),2)
    
    def OZtoPint(self):
        print('That volume in pints is...')
        return round((self.volume / 16),2)
    
    def QTtoGAL(self):
        print('That volume in gallons is...')
        return round((self.volume / 4 ),2)
    
    def QTtoCF(self):
        print('That volume in cubic feet is...')
        return round((self.volume / 29.922),3)
    
    def QTtoOZ(self):
        print('That volume in ounces is...')
        return round((self.volume * 32),2)
    
    def QTtoPint(self):
        print('That volume in pints is...')
        return round((self.volume * 2),2)
    
    
##################################################################################################################
print("Welcome to my unit converter.")

print('\n')

time.sleep(1)

while True:
    
    user_choice = ConversionChoice()
##################################################################################################################

                                            ### TEMP CONVERSION ###

##################################################################################################################

    if user_choice == 't':
        Temp_units = TempUnits()

        if Temp_units == 'c':
            
            c1 = ''
            while not (c1 == 'f' or c1 == 'k'):
                c1 = input("Would you like to convert to Fahrenheit or Kelvin (F or K)?: ").lower()
                
            if c1 == 'f':
                temp_c = Temp(float(input("Enter your temperature in Celsius: ")))
                print(temp_c.CtoF())
                time.sleep(1.0)
                
            if c1 == 'k':
                temp_c = Temp(float(input("Enter your temperature in Celsius: ")))
                print(temp_c.CtoK())
                time.sleep(1.0)
                
            if not NewCalc():
                break
                
        if Temp_units == 'f':
            
            f1 = ''
            while not (f1 == 'c' or f1 == 'k'):
                f1 = input("Would you like to convert to Celsius or Kelvin (C or K)?: ").lower()
                
            if f1 == 'c':
                temp_f = Temp(float(input("Enter your temperature in Fahrenheit: ")))
                print(temp_f.FtoC())
                time.sleep(1.0)
                
            if f1 == 'k':
                temp_f = Temp(float(input("Enter your temperature in Fahrenheit: ")))
                print(temp_f.FtoK())
                time.sleep(1.0)
            if not NewCalc():
                break
                
        if Temp_units == 'k':
            
            k1 = ''
            while not (k1 == 'c' or k1 == 'f'):
                k1 = input("Would you like to convert to Celsius or Fahrenheit (C or F)?: ").lower()
                
            if k1 == 'c':
                temp_k = Temp(float(input("Enter your temperature in Kelvin: ")))
                print(temp_k.KtoC())
                time.sleep(1.0)
                
            if k1 == 'f':
                temp_k = Temp(float(input("Enter your temperature in Kelvin: ")))
                print(temp_k.KtoF())
                time.sleep(1.0)
            if not NewCalc():
                break
                
##################################################################################################################

                                             ### MASS CONVERSION ###

##################################################################################################################

    if user_choice == 'm':
        
        mass_units = MassUnits()
        
        if mass_units == 'g':
            
            g1 = ''
            while not (g1 == 'oz' or g1 == 'lbs' or g1 == 'kg'):
                g1 = input("Would you like to convert to Pounds(lbs), Ounces(oz), or Kilograms(kg)?: ").lower()
                
            if g1 == 'lbs':
                mass_lbs = Mass(float(input("Enter your mass in grams: ")))
                print(mass_lbs.GramsToPounds())
                time.sleep(1.0)
                
            if g1 == 'kg':
                mass_kg = Mass(float(input("Enter your mass in grams: ")))
                print(mass_kg.GramsToKilograms())
                time.sleep(1.0)
            if g1 == 'oz':
                mass_oz = Mass(float(input('Enter your mass in grams: ')))
                print(mass_oz.GramsToOunces())
                time.sleep(1.0)
                
            if not NewCalc():
                break
        
        if mass_units == 'lbs':
            
            p1 = ''
            while not (p1 == 'oz' or p1 == 'g' or p1 == 'kg'):
                p1 = input("Would you like to convert to Grams(g), Ounces(oz), or Kilograms(kg)?: ").lower()
                
            if p1 == 'g':
                mass_g = Mass(float(input("Enter your mass in pounds: ")))
                print(mass_g.PoundstoGrams())
                time.sleep(1.0)
                
            if p1 == 'kg':
                mass_kg = Mass(float(input("Enter your mass in pounds: ")))
                print(mass_kg.PoundstoKilograms())
                time.sleep(1.0)
            if p1 == 'oz':
                mass_oz = Mass(float(input('Enter your mass in pounds: ')))
                print(mass_oz.PoundstoOunces())
                time.sleep(1.0)
                
            if not NewCalc():
                break
                
        if mass_units == 'oz':
            
            o1 = ''
            while not (o1 == 'lbs' or o1 == 'g' or o1 == 'kg'):
                o1 = input("Would you like to convert to Grams(g), Pounds(lbs), or Kilograms(kg)?: ").lower()
                
            if o1 == 'g':
                mass_g = Mass(float(input("Enter your mass in ounces: ")))
                print(mass_g.OuncestoGrams())
                time.sleep(1.0)
                
            if o1 == 'kg':
                mass_kg = Mass(float(input("Enter your mass in ounces: ")))
                print(mass_kg.OuncestoKilograms())
                time.sleep(1.0)
            if o1 == 'lbs':
                mass_lbs = Mass(float(input('Enter your mass in ounces: ')))
                print(mass_lbs.OuncestoPounds())
                time.sleep(1.0)
                
            if not NewCalc():
                break
        
        if mass_units == 'kg':
            
            k1 = ''
            while not (k1 == 'lbs' or k1 == 'g' or k1 == 'oz'):
                k1 = input("Would you like to convert to Grams(g), Pounds(lbs), or Ounces(oz)?: ").lower()
                
            if k1 == 'g':
                mass_g = Mass(float(input("Enter your mass in kilograms: ")))
                print(mass_g.KilogramstoGrams())
                time.sleep(1.0)
                
            if k1 == 'oz':
                mass_oz = Mass(float(input("Enter your mass in kilograms: ")))
                print(mass_oz.KilogramstoOunces())
                time.sleep(1.0)
            if k1 == 'lbs':
                mass_lbs = Mass(float(input('Enter your mass in kilograms: ')))
                print(mass_lbs.KilogramstoPounds())
                time.sleep(1.0)
                
            if not NewCalc():
                break
                
##################################################################################################################

                                            ### CURRENCY CONVERSION ###

##################################################################################################################


    if user_choice == 'c':
        
        currencyChoice = CurrencyUnits()
        
        if currencyChoice == 'usd':
            
            u1 = ''
            while not (u1 == 'cad' or u1 == 'jpy' or u1 == 'gbp' or u1 == 'mxn' or u1 == 'eur'):
                u1 = input("Would you like to convert to Euro(EUR),Yen(JPY),British Pound(GBP),Canadian Dollar(CAD), or Mexican Peso(MXN)?: ").lower()
                
            if u1 == 'eur':
                cur_eur = Currency(float(input("Enter your currency in US Dollars: ")))
                print(cur_eur.USDtoEUR())
                time.sleep(1.0)
                
            if u1 == 'jpy':
                cur_jpy = Currency(float(input("Enter your currency in US Dollars: ")))
                print(cur_jpy.USDtoJPY())
                time.sleep(1.0)
                
            if u1 == 'gbp':
                cur_gbp = Currency(float(input('Enter your currency in US Dollars: ')))
                print(cur_gbp.USDtoGBP())
                time.sleep(1.0)
                
            if u1 == 'mxn':
                cur_mxn = Currency(float(input('Enter your currency in US Dollars: ')))
                print(cur_mxn.USDtoMXN())
                time.sleep(1.0)
                
            if u1 == 'cad':
                cur_cad = Currency(float(input('Enter your currency in US Dollars: ')))
                print(cur_cad.USDtoCAD())
                time.sleep(1.0)
                
            if not NewCalc():
                break
        
        if currencyChoice == 'eur':
            
            e1 = ''
            while not (e1 == 'cad' or e1 == 'jpy' or e1 == 'gbp' or e1 == 'mxn' or e1 == 'usd'):
                e1 = input("Would you like to convert to US Dollars(USD),Yen(JPY),British Pound(GBP),Canadian Dollar(CAD), or Mexican Peso(MXN)?: ").lower()
                
            if e1 == 'usd':
                cur_usd = Currency(float(input("Enter your currency in Euros: ")))
                print(cur_usd.EURtoUSD())
                time.sleep(1.0)
                
            if e1 == 'jpy':
                cur_jpy = Currency(float(input("Enter your currency in Euros: ")))
                print(cur_jpy.EURtoJPY())
                time.sleep(1.0)
                
            if e1 == 'gbp':
                cur_gbp = Currency(float(input('Enter your currency in Euros: ')))
                print(cur_gbp.EURtoGBP())
                time.sleep(1.0)
                
            if e1 == 'mxn':
                cur_mxn = Currency(float(input('Enter your currency in Euros: ')))
                print(cur_mxn.EURtoMXN())
                time.sleep(1.0)
                
            if e1 == 'cad':
                cur_cad = Currency(float(input('Enter your currency in Euros: ')))
                print(cur_cad.EURtoCAD())
                time.sleep(1.0)
                
            if not NewCalc():
                break
                
        if currencyChoice == 'mxn':
            
            m1 = ''
            while not (m1 == 'cad' or m1 == 'jpy' or m1 == 'gbp' or m1 == 'eur' or m1 == 'usd'):
                m1 = input("Would you like to convert to US Dollars(USD),Yen(JPY),British Pound(GBP),Canadian Dollar(CAD), or Euros(EUR)?: ").lower()
                
            if m1 == 'usd':
                cur_usd = Currency(float(input("Enter your currency in Pesos: ")))
                print(cur_usd.MXNtoUSD())
                time.sleep(1.0)
                
            if m1 == 'jpy':
                cur_jpy = Currency(float(input("Enter your currency in Pesos: ")))
                print(cur_jpy.MXNtoJPY())
                time.sleep(1.0)
                
            if m1 == 'gbp':
                cur_gbp = Currency(float(input('Enter your currency in Pesos: ')))
                print(cur_gbp.MXNtoGBP())
                time.sleep(1.0)
                
            if m1 == 'eur':
                cur_eur = Currency(float(input('Enter your currency in Pesos: ')))
                print(cur_eur.MXNtoEUR())
                time.sleep(1.0)
                
            if m1 == 'cad':
                cur_cad = Currency(float(input('Enter your currency in Pesos: ')))
                print(cur_cad.MXNtoCAD())
                time.sleep(1.0)
                
            if not NewCalc():
                break
                
        if currencyChoice == 'gbp':
            
            g1 = ''
            while not (g1 == 'cad' or g1 == 'jpy' or g1 == 'mxn' or g1 == 'eur' or g1 == 'usd'):
                g1 = input("Would you like to convert to US Dollars(USD),Yen(JPY),Mexican Pesos(MXN),Canadian Dollar(CAD), or Euros(EUR)?: ").lower()
                
            if g1 == 'usd':
                cur_usd = Currency(float(input("Enter your currency in British Pound: ")))
                print(cur_usd.GBPtoUSD())
                time.sleep(1.0)
                
            if g1 == 'jpy':
                cur_jpy = Currency(float(input("Enter your currency in British Pound: ")))
                print(cur_jpy.GBPtoJPY())
                time.sleep(1.0)
                
            if g1 == 'mxn':
                cur_mxn = Currency(float(input('Enter your currency in British Pound: ')))
                print(cur_mxn.GBPtoMXN())
                time.sleep(1.0)
                
            if g1 == 'eur':
                cur_eur = Currency(float(input('Enter your currency in British Pound: ')))
                print(cur_eur.GBPtoEUR())
                time.sleep(1.0)
                
            if g1 == 'cad':
                cur_cad = Currency(float(input('Enter your currency in British Pound: ')))
                print(cur_cad.GBPtoCAD())
                time.sleep(1.0)
                
            if not NewCalc():
                break
                
                
        if currencyChoice == 'cad':
            
            c1 = ''
            while not (c1 == 'gbp' or c1 == 'jpy' or c1 == 'mxn' or c1 == 'eur' or c1 == 'usd'):
                c1 = input("Would you like to convert to US Dollars(USD),Yen(JPY),Mexican Pesos(MXN),British Pound(GBP), or Euros(EUR)?: ").lower()
                
            if c1 == 'usd':
                cur_usd = Currency(float(input("Enter your currency in Canadian Dollars: ")))
                print(cur_usd.CADtoUSD())
                time.sleep(1.0)
                
            if c1 == 'jpy':
                cur_jpy = Currency(float(input("Enter your currency in Canadian Dollars: ")))
                print(cur_jpy.CADtoJPY())
                time.sleep(1.0)
                
            if c1 == 'mxn':
                cur_mxn = Currency(float(input('Enter your currency in Canadian Dollars: ')))
                print(cur_mxn.CADtoMXN())
                time.sleep(1.0)
                
            if c1 == 'eur':
                cur_eur = Currency(float(input('Enter your currency in Canadian Dollars: ')))
                print(cur_eur.CADtoEUR())
                time.sleep(1.0)
                
            if c1 == 'gbp':
                cur_gbp = Currency(float(input('Enter your currency in Canadian Dollars: ')))
                print(cur_gbp.CADtoGBP())
                time.sleep(1.0)
            
        if currencyChoice == 'jpy':
            
            j1 = ''
            
            while not (j1 == 'gbp' or j1 == 'cad' or j1 == 'mxn' or j1 == 'eur' or j1 == 'usd'):
                
                j1 = input("Would you like to convert to US Dollars(USD),Canadian Dollar(CAD),Mexican Pesos(MXN),British Pound(GBP), or Euros(EUR)?: ").lower()
                
            if j1 == 'usd':
                cur_usd = Currency(float(input("Enter your currency in Yen: ")))
                print(cur_usd.JPYtoUSD())
                time.sleep(1.0)
                
            if j1 == 'cad':
                cur_cad = Currency(float(input("Enter your currency in Yen: ")))
                print(cur_cad.JPYtoCAD())
                time.sleep(1.0)
                
            if j1 == 'mxn':
                cur_mxn = Currency(float(input('Enter your currency in Yen: ')))
                print(cur_mxn.JPYtoMXN())
                time.sleep(1.0)
                
            if j1 == 'eur':
                cur_eur = Currency(float(input('Enter your currency in Yen: ')))
                print(cur_eur.JPYtoEUR())
                time.sleep(1.0)
                
            if j1 == 'gbp':
                cur_gbp = Currency(float(input('Enter your currency in Yen: ')))
                print(cur_gbp.JPYtoGBP())
                time.sleep(1.0)
                
            if not NewCalc():
                
                break
                
            print('\n')
            
            
                        
##################################################################################################################

                                             ### VOLUME CONVERSION ###

##################################################################################################################
            

    if user_choice == 'v':
        
        volumeChoice = VolumeChoice()
        
        if volumeChoice == 'gal':
            g1 = ''
            
            while not (g1 == 'pt' or g1 == 'cf' or g1 == 'qt' or g1 == 'floz'):
                
                g1 = input("Would you like to convert to Pints(PT),Quarts(QT),Fluid Ounces(FlOz), or Cubic Feet(CF)?: ").lower()
                
            if g1 == 'pt':
                vol_pt = Volume(float(input("Enter your volume in gallons: ")))
                print(vol_pt.GALtoPint())
                time.sleep(1.0)
                
            if g1 == 'qt':
                vol_qt = Volume(float(input("Enter your volume in gallons: ")))
                print(vol_qt.GALtoQT())
                time.sleep(1.0)
                
            if g1 == 'floz':
                vol_floz = Volume(float(input('Enter your volume in gallons: ')))
                print(vol_floz.GALtoOz())
                time.sleep(1.0)
                
            if g1 == 'cf':
                vol_cf = Volume(float(input('Enter your volume in gallons: ')))
                print(vol_cf.GALtoCF())
                time.sleep(1.0)
                
                
            if not NewCalc():
                break
                
        if volumeChoice == 'pt':
            p1 = ''
            
            while not (p1 == 'gal' or p1 == 'cf' or p1 == 'qt' or p1 == 'floz'):
                
                p1 = input("Would you like to convert to Gallons(GAL),Quarts(QT),Fluid Ounces(FlOz), or Cubic Feet(CF)?: ").lower()
                
            if p1 == 'gal':
                vol_gal = Volume(float(input("Enter your volume in pints: ")))
                print(vol_gal.PinttoGAL())
                time.sleep(1.0)
                
            if p1 == 'qt':
                vol_qt = Volume(float(input("Enter your volume in pints: ")))
                print(vol_qt.PinttoQT())
                time.sleep(1.0)
                
            if p1 == 'floz':
                vol_floz = Volume(float(input('Enter your volume in pints: ')))
                print(vol_floz.PinttoOZ())
                time.sleep(1.0)
                
            if p1 == 'cf':
                vol_cf = Volume(float(input('Enter your volume in pints: ')))
                print(vol_cf.PinttoCF())
                time.sleep(1.0)
                
                
            if not NewCalc():
                break
        
        if volumeChoice == 'qt':
            q1 = ''
            
            while not (q1 == 'gal' or q1 == 'pt' or q1 == 'cf' or q1 == 'floz'):
                
                q1 = input("Would you like to convert to Gallons(GAL),Cubic Feet(CF),Fluid Ounces(FlOz), or Pints(PT)?: ").lower()
                
            if q1 == 'gal':
                vol_gal = Volume(float(input("Enter your volume in quarts: ")))
                print(vol_gal.QTtoGAL())
                time.sleep(1.0)
                
            if q1 == 'cf':
                vol_cf = Volume(float(input("Enter your volume in quarts: ")))
                print(vol_cf.QTtoCF())
                time.sleep(1.0)
                
            if q1 == 'floz':
                vol_floz = Volume(float(input('Enter your volume in quarts: ')))
                print(vol_floz.QTtoOZ())
                time.sleep(1.0)
                
            if q1 == 'pt':
                vol_pt = Volume(float(input('Enter your volume in quarts: ')))
                print(vol_pt.QTtoPint())
                time.sleep(1.0)
                
                
            if not NewCalc():
                break
                
        if volumeChoice == 'cf':
            c1 = ''
            
            while not (c1 == 'gal' or c1 == 'pt' or c1 == 'qt' or c1 == 'floz'):
                
                c1 = input("Would you like to convert to Gallons(GAL),Quarts(QT),Fluid Ounces(FlOz), or Pints(PT)?: ").lower()
                
            if c1 == 'gal':
                vol_gal = Volume(float(input("Enter your volume in cubic feet: ")))
                print(vol_gal.CFtoGAL())
                time.sleep(1.0)
                
            if c1 == 'qt':
                vol_qt = Volume(float(input("Enter your volume in cubic feet: ")))
                print(vol_qt.CFtoQT())
                time.sleep(1.0)
                
            if c1 == 'floz':
                vol_floz = Volume(float(input('Enter your volume in cubic feet: ')))
                print(vol_floz.CFtoOZ())
                time.sleep(1.0)
                
            if c1 == 'pt':
                vol_pt = Volume(float(input('Enter your volume in cubic feet: ')))
                print(vol_pt.CFtoPint())
                time.sleep(1.0)
                
                
            if not NewCalc():
                break
            
        if volumeChoice == 'floz':
            f1 = ''
            
            while not (f1 == 'gal' or f1 == 'pt' or f1 == 'qt' or f1 == 'cf'):
                
                f1 = input("Would you like to convert to Gallons(GAL),Quarts(QT),Cubic Feet(CF), or Pints(PT)?: ").lower()
                
            if f1 == 'gal':
                vol_gal = Volume(float(input("Enter your volume in fluid ounces: ")))
                print(vol_gal.OZtoGAL())
                time.sleep(1.0)
                
            if f1 == 'qt':
                vol_qt = Volume(float(input("Enter your volume in fluid ounces: ")))
                print(vol_qt.OZtoQT())
                time.sleep(1.0)
                
            if f1 == 'cf':
                vol_cf = Volume(float(input('Enter your volume in fluid ounces: ')))
                print(vol_cf.OZtoCF())
                time.sleep(1.0)
                
            if f1 == 'pt':
                vol_pt = Volume(float(input('Enter your volume in fluid ounces: ')))
                print(vol_pt.OZtoPint())
                time.sleep(1.0)
                
                
            if not NewCalc():
                break
                
        


# In[ ]:





# In[ ]:




