from experta import *
import sys, getopt
import app
fertilizer_details={'DAP':"DAP fertilizer is an excellent source of Phosphorus and nitrogen (N) for plant nutrition. It's highly soluble and thus dissolves quickly in soil to release plant-available phosphate and ammonium. A notable property of DAP is the alkaline pH that develops around the dissolving granule.",
                  '10-26-26':"NPK 10-26-26 fixes the phosphorus and potassium content in the soil and is highly effective in soils with leaching condition. The product is granular and comes in moisture resistant HDP bags allowing easy handling and storage.",
                  'Urea':"Urea is the most important nitrogenous fertilizer in the market, with the highest Nitrogen content (about 46 percent). It is a white crystalline organic chemical compound. Urea is neutral in pH and can adapt to almost all kinds of soils.",
                  '14-35-14':"GROMOR 14-35-14 is a complex fertiliser containing all major nutrients viz. Nitrogen, Phosphate and Potash. - The only complex having highest total nutrient content among the NPK complex fertilisers. (Total nutrients are 63%). - Nitrogen and Phosphate are available in 1:2.5.",
                  '28-28':"NPK 28-28 is a complex fertiliser containing 2 major nutrients, Nitrogen at 28% and Phosphorus at 28%, provides instantaneous and prolonged greenness for crops.",
                  '20-20':"The 20-20-20 fertilizer is an all-purpose mix that works well for nearly everything that has green leaves and grows in the dirt. The number signifies that the fertilizer product contains 20% of all three major nutrients needed by plants (nitrogen, phosphorous, and potassium).",
                  '17-17-17':" 17 17 17 is a balanced fertilizer (potash) used for many plants, grasses, and shrubs. This type of fertilizer contains minerals in a balanced npk ratio just like triple 14 fertilizer."}


#salience means priority
class Welcome(KnowledgeEngine):
    @DefFacts()
    def initial(self):
        yield Fact(action="find_Crop")
        yield Fact(action="find_Fertilizer")

    @Rule(Fact(action='find_Crop'),NOT(Fact(Nitrogen=W())),NOT(Fact(Phosphorous=W())),NOT(Fact(Potassium=W())),NOT(Fact(Temperature=W())),NOT(Fact(Humidity=W())),NOT(Fact(Rainfall=W())),salience=1)
    def symptoms(self):
        print(inputUser)
        
        self.declare(Fact(Nitrogen=float(inputUser["Nitrogen"])))
        self.declare(Fact(Phosphorous=float(inputUser["Phosphorous"])))
        self.declare(Fact(Potassium=float(inputUser["Potassium"])))
        self.declare(Fact(Temperature=float(inputUser["Temperature"])))
        self.declare(Fact(Humidity=float(inputUser["Humidity"])))
        self.declare(Fact(Rainfall=float(inputUser["Rainfall"])))
        print(MATCH.Rainfall)
        print(type(MATCH.Rainfall))
    @Rule(Fact(action='find_Crop'),NOT(Fact(Nitrogen=W())),salience=-999)
    def symptom_0(self):
        self.declare(Fact(Nitrogen=float(input("Nitrogen: "))))  #first
    
    @Rule(Fact(action='find_Crop'),NOT(Fact(Phosphorous=W())),salience=-999)
    def symptom_1(self):
        self.declare(Fact(Phosphorous=float(input("Phosphorous: "))))  #first
   
    
    @Rule(Fact(action='find_Crop'),NOT(Fact(Potassium=W())),salience=-999)
    def symptom_2(self):
        self.declare(Fact(Potassium=float(input("Potassium: "))))  #first
    
    @Rule(Fact(action='find_Crop'),NOT(Fact(Temperature=W())),salience=-999)
    def symptom_3(self):
        self.declare(Fact(Temperature=float(input("Temperature: "))))  #first
    
    @Rule(Fact(action='find_Crop'),NOT(Fact(Humidity=W())),salience=-999)
    def symptom_4(self):
        self.declare(Fact(Humidity=float(input("Humidity: "))))  #first
    
    @Rule(Fact(action='find_Crop'),NOT(Fact(Rainfall=W())),salience=-999)
    def symptom_6(self):
        self.declare(Fact(Rainfall=float(input("Rainfall: "))))  #first
    
    
    
    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity <= 74.92),
          TEST(lambda Nitrogen: Nitrogen <= 59.50),
          TEST(lambda Rainfall: Rainfall <= 75.76 and Rainfall <= 59.73),
          TEST(lambda Potassium: Potassium <= 35.50))
    def Crop_0(self):
        self.declare(Fact(Crop="Lentil"))

    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity <= 74.92),
          TEST(lambda Nitrogen: Nitrogen <= 59.50),
          TEST(lambda Rainfall: Rainfall >  59.73),
          TEST(lambda Rainfall:  Rainfall <= 75.76),
          TEST(lambda Potassium: Potassium <= 35.50))
    def Crop_1(self):
        self.declare(Fact(Crop="Blackgram"))

    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity <= 74.92),
          TEST(lambda Nitrogen: Nitrogen <= 59.50),
          TEST(lambda Phosphorous: Phosphorous <= 47.50),
          TEST(lambda Rainfall: Rainfall >  75.76),
          TEST(lambda Potassium: Potassium <= 35.50))
    def Crop_1(self):
        self.declare(Fact(Crop="Mango"))

    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity <= 74.92),
          TEST(lambda Nitrogen: Nitrogen <= 59.50),
          TEST(lambda Phosphorous: Phosphorous >  47.50),
          TEST(lambda Rainfall: Rainfall >  75.76),
          TEST(lambda Potassium: Potassium <= 35.50))
    def Crop_2(self):
        self.declare(Fact(Crop="Pigeonpeas"))

    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity <= 74.92),
          TEST(lambda Nitrogen: Nitrogen >  59.50),
          TEST(lambda Temperature: Temperature <= 29.01),
          TEST(lambda Rainfall: Rainfall <= 112.45),
          TEST(lambda Potassium: Potassium <= 35.50))
    def Crop_3(self):
        self.declare(Fact(Crop="Maize"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity <= 74.92),
          TEST(lambda Nitrogen: Nitrogen >  59.50),
          TEST(lambda Temperature: Temperature >  29.01),
          TEST(lambda Rainfall: Rainfall <= 112.45),
          TEST(lambda Potassium: Potassium <= 35.50))
    def Crop_4(self):
        self.declare(Fact(Crop="Blackgram"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity <= 74.92),
          TEST(lambda Nitrogen: Nitrogen >  59.50),
          TEST(lambda Phosphorous: Phosphorous <= 47.00),
          TEST(lambda Rainfall: Rainfall >  112.45),
          TEST(lambda Potassium: Potassium <= 35.50))
    def Crop_5(self):
        self.declare(Fact(Crop="Coffee"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity <= 74.92),
          TEST(lambda Nitrogen: Nitrogen >  59.50),
          TEST(lambda Phosphorous: Phosphorous >  47.00),
          TEST(lambda Rainfall: Rainfall >  112.45),
          TEST(lambda Potassium: Potassium <= 35.50))
    def Crop_6(self):
        self.declare(Fact(Crop="Jute"))

    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity >  74.92),
          TEST(lambda Phosphorous: Phosphorous <= 32.50),
          TEST(lambda Potassium: Potassium <= 20.00),
          TEST(lambda Potassium: Potassium <= 35.50))
    def Crop_7(self):
        self.declare(Fact(Crop="Orange"))
    
    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity >  74.92),
          TEST(lambda Temperature: Temperature <= 24.14),
          TEST(lambda Phosphorous: Phosphorous <= 32.50),
          TEST(lambda Potassium: Potassium > 20.00),
          TEST(lambda Potassium: Potassium <= 35.50))
    def Crop_8(self):
        self.declare(Fact(Crop="Pomegranate"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity >  74.92),
          TEST(lambda Temperature: Temperature >  24.14),
          TEST(lambda Phosphorous: Phosphorous <= 32.50),
          TEST(lambda Potassium: Potassium > 20.00),
          TEST(lambda Potassium: Potassium <= 35.50))
    def Crop_9(self):
        self.declare(Fact(Crop="Coconut"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity >  74.92),
          TEST(lambda Nitrogen: Nitrogen <= 99.50),
          TEST(lambda Phosphorous: Phosphorous >  32.50),
          TEST(lambda Potassium: Potassium <= 35.50),
          TEST(lambda Potassium: Potassium >  30.00))
    def Crop_10(self):
        self.declare(Fact(Crop="Jute"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity >  74.92),
          TEST(lambda Nitrogen: Nitrogen >  99.50),
          TEST(lambda Phosphorous: Phosphorous >  32.50),
          TEST(lambda Potassium: Potassium <= 35.50))
    def Crop_11(self):
        self.declare(Fact(Crop="Cotton"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity <= 52.58),
          TEST(lambda Nitrogen: Nitrogen <= 59.50),
          TEST(lambda Phosphorous: Phosphorous <= 140.00),
          TEST(lambda Potassium: Potassium > 35.50))
    def Crop_12(self):
        self.declare(Fact(Crop="Chickpea"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity <= 52.58),
          TEST(lambda Nitrogen: Nitrogen <= 59.50),
          TEST(lambda Phosphorous: Phosphorous <= 140.00),
          TEST(lambda Potassium: Potassium > 35.50))
    def Crop_13(self):
        self.declare(Fact(Crop="Chickpea"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity >  52.58),
          TEST(lambda Nitrogen: Nitrogen <= 59.50),
          TEST(lambda Phosphorous: Phosphorous <= 140.00),
          TEST(lambda Phosphorous: Phosphorous <= 38.50),
          TEST(lambda Potassium: Potassium > 35.50))
    def Crop_14(self):
        self.declare(Fact(Crop="Pomegranate"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity >  52.58),
          TEST(lambda Nitrogen: Nitrogen <= 59.50),
          TEST(lambda Phosphorous: Phosphorous <= 140.00),
          TEST(lambda Phosphorous: Phosphorous >  38.50),
          TEST(lambda Potassium: Potassium > 35.50))
    def Crop_15(self):
        self.declare(Fact(Crop="Papaya"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity >  52.58),
          TEST(lambda Nitrogen: Nitrogen <= 59.50),
          TEST(lambda Phosphorous: Phosphorous > 140.00),
          TEST(lambda Phosphorous: Phosphorous >  38.50),
          TEST(lambda Rainfall: Rainfall <= 87.52),
          TEST(lambda Potassium: Potassium > 35.50))
    def Crop_16(self):
        self.declare(Fact(Crop="Grapes"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity >  52.58),
          TEST(lambda Nitrogen: Nitrogen <= 59.50),
          TEST(lambda Phosphorous: Phosphorous > 140.00),
          TEST(lambda Phosphorous: Phosphorous >  38.50),
          TEST(lambda Rainfall: Rainfall >  87.52),
          TEST(lambda Potassium: Potassium > 35.50))
    def Crop_17(self):
        self.declare(Fact(Crop="Apple"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity <= 90.00),
          TEST(lambda Nitrogen: Nitrogen >  59.50),
          TEST(lambda Phosphorous: Phosphorous <= 32.50),
          TEST(lambda Potassium: Potassium > 35.50))
    def Crop_18(self):
        self.declare(Fact(Crop="Watermelon"))


    @Rule(Fact(action='find_Crop'),Fact(Potassium=MATCH.Potassium),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Humidity: Humidity >  90.00),
          TEST(lambda Nitrogen: Nitrogen >  59.50),
          TEST(lambda Phosphorous: Phosphorous <= 32.50),
          TEST(lambda Potassium: Potassium > 35.50))
    def Crop_19(self):
        self.declare(Fact(Crop="Muskmelon"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Rainfall: Rainfall <= 150.04),
          TEST(lambda Nitrogen: Nitrogen >  59.50),
          TEST(lambda Phosphorous: Phosphorous >  32.50),
          TEST(lambda Nitrogen: Nitrogen >  75.00),
          TEST(lambda Potassium: Potassium > 35.50))
    def Crop_20(self):
        self.declare(Fact(Crop="Banana"))


    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Rainfall: Rainfall >  150.04),
          TEST(lambda Rainfall: Rainfall <= 199.78),
          TEST(lambda Phosphorous: Phosphorous >  32.50),
          TEST(lambda Nitrogen: Nitrogen >  59.50),
          TEST(lambda Potassium: Potassium > 35.50))
    def Crop_21(self):
        self.declare(Fact(Crop="Jute"))



    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Rainfall: Rainfall >  150.04),
          TEST(lambda Rainfall: Rainfall >  199.78),
          TEST(lambda Phosphorous: Phosphorous >  32.50),
          TEST(lambda Nitrogen: Nitrogen >  59.50),
          TEST(lambda Potassium: Potassium > 35.50))
    def Crop_22(self):
        self.declare(Fact(Crop="Rice"))


          
    @Rule(Fact(action='find_Crop'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          Fact(Crop=MATCH.Crop),salience=-997)
    def Crop(self,Rainfall,Potassium,Phosphorous,Nitrogen,Temperature,Humidity,Crop):
        a =Crop
        
        #Crop_detail=get_description(a)
        #Crop_treatment=get_treatment(a)
        print("For: \n  Rainfall= "+str(Rainfall)+"\n  Potassium= "+str(Potassium)+" \n  Phosphorous= "+str(Phosphorous)+" \n  Nitrogen= "+str(Nitrogen)+" \n  Temperature= "+str(Temperature)+" \n  Humidity= "+str(Humidity)+"\n")
        print("The most probable Crop is "+a+"\n")
        predictionResult["Rainfall"]=Rainfall
        predictionResult["Crop"]=Crop
        predictionResult["Potassium"]=Potassium
        predictionResult["Phosphorous"]=Phosphorous
        predictionResult["Nitrogen"]=Nitrogen
        predictionResult["Temperature"]=Temperature
        predictionResult["Humidity"]=Humidity

        predictionResult["Crop"]=Crop
        #print("the short description is "+Crop_detail+"\n")
        #print("the common medications are "+Crop_treatment+ "\n")
        
    @Rule(Fact(action='find_Crop'),
         Fact(Rainfall=MATCH.Rainfall),
         Fact(Potassium=MATCH.Potassium),
         Fact(Phosphorous=MATCH.Phosphorous),
         Fact(Nitrogen=MATCH.Nitrogen),
         Fact(Temperature=MATCH.Temperature),
         Fact(Humidity=MATCH.Humidity),
         NOT(Fact(Crop=MATCH.Crop)),salience=-999)
    def not_matched(self,Rainfall,Potassium,Phosphorous,Nitrogen,Temperature,Humidity):
        print("Your features doesn't matches our record")
        predictionResult["Crop"]="Your features doesn't matches our record"

    @Rule(Fact(action='find_Fertilizer'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Phosphorous: Phosphorous <= 21.50),
          TEST(lambda Nitrogen: Nitrogen <= 18.00),
          TEST(lambda Potassium: Potassium <= 5.00))
    def Fertilizer_0(self):
        self.declare(Fact(Fertilizer="20-20"))     

    @Rule(Fact(action='find_Fertilizer'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Phosphorous: Phosphorous <= 21.50),
          TEST(lambda Nitrogen: Nitrogen <= 18.00),
          TEST(lambda Potassium: Potassium >  5.00 and Potassium <= 15.00))
    def Fertilizer_1(self):
        self.declare(Fact(Fertilizer="17-17-17"))     
    
    @Rule(Fact(action='find_Fertilizer'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Phosphorous: Phosphorous <= 21.50),
          TEST(lambda Nitrogen: Nitrogen <= 18.00),
          TEST(lambda Potassium: Potassium >  5.00 and Potassium > 15.00))
    def Fertilizer_2(self):
        self.declare(Fact(Fertilizer="10-26-26"))   



    @Rule(Fact(action='find_Fertilizer'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Phosphorous: Phosphorous > 21.50),
          TEST(lambda Nitrogen: Nitrogen <= 18.00 and Nitrogen <= 10.50 ))
    def Fertilizer_3(self):
        self.declare(Fact(Fertilizer="14-35-14"))  
    
    @Rule(Fact(action='find_Fertilizer'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Phosphorous: Phosphorous > 21.50),
          TEST(lambda Nitrogen: Nitrogen <= 18.00 and Nitrogen > 10.50 ))
    def Fertilizer_4(self):
        self.declare(Fact(Fertilizer="DAP"))  

    @Rule(Fact(action='find_Fertilizer'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Phosphorous: Phosphorous <= 9.00),
          TEST(lambda Nitrogen: Nitrogen > 18.00))
    def Fertilizer_5(self):
        self.declare(Fact(Fertilizer="Urea"))  

    @Rule(Fact(action='find_Fertilizer'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          TEST(lambda Phosphorous: Phosphorous > 9.00),
          TEST(lambda Nitrogen: Nitrogen > 18.00))
    def Fertilizer_6(self):
        self.declare(Fact(Fertilizer="28-28"))  

    @Rule(Fact(action='find_Fertilizer'),
          Fact(Rainfall=MATCH.Rainfall),
          Fact(Potassium=MATCH.Potassium),
          Fact(Phosphorous=MATCH.Phosphorous),
          Fact(Nitrogen=MATCH.Nitrogen),
          Fact(Temperature=MATCH.Temperature),
          Fact(Humidity=MATCH.Humidity),
          Fact(Fertilizer=MATCH.Fertilizer),salience=-997)
    def Fertilizer(self,Rainfall,Potassium,Phosphorous,Nitrogen,Temperature,Humidity,Fertilizer):
        a =Fertilizer
        predictionResult["Fertilizer"]=Fertilizer
        predictionResult["fertilizer_details"]=fertilizer_details[a]
        #print("For: \n  Rainfall= "+str(Rainfall)+"\n  Potassium= "+str(Potassium)+" \n  Phosphorous= "+str(Phosphorous)+" \n  Nitrogen= "+str(Nitrogen)+" \n  Temperature= "+str(Temperature)+" \n  Humidity= "+str(Humidity)+"\n")
        print("The most probable Fertilizer is "+a+"\n")
        print(fertilizer_details[a])
        
    @Rule(Fact(action='find_Fertilizer'),
         Fact(Rainfall=MATCH.Rainfall),
         Fact(Potassium=MATCH.Potassium),
         Fact(Phosphorous=MATCH.Phosphorous),
         Fact(Nitrogen=MATCH.Nitrogen),
         Fact(Temperature=MATCH.Temperature),
         Fact(Humidity=MATCH.Humidity),
         NOT(Fact(Fertilizer=MATCH.Fertilizer)),salience=-999)
    def not_matched_Fertilizer(self,Rainfall,Potassium,Phosphorous,Nitrogen,Temperature,Humidity):
        print("Your features doesn't matches our record.")
        predictionResult["Fertilizer"]="Your features doesn't matches our record."

global predictionResult
predictionResult={}

def main(inputU):
    global inputUser
    inputUser=inputU
    engine=Welcome()
    engine.reset()   
    engine.run()
    return predictionResult
       