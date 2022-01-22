'''
Age factors
Travveled over seas or out of state in past 2-3 weeks(yes=most likely)
Any mass gatherings attended(yes=most likely)
Symptoms:
Cough
Runny nose
Sneezing
Sore throat
Shortness of breath
Fever
Night sweats
Chills
Headache
Loss of smell
Fatigue
How long symptoms take to show up
Doses of vaccination
tiredness
red eyes
Cancer

Chronic kidney disease

Chronic liver disease

Chronic lung diseases

Dementia or other neurological conditions

Diabetes (type 1 or type 2)

Down syndrome

Heart conditions

HIV infection

Immunocompromised state (weakened immune system)

Mental health conditions

Overweight and obesity

Sickle cell disease or thalassemia

Smoking, current or former

Substance use disorders

Tuberculosis
'''
def symptoms():
  cough = str(input("Have you been coughing frequently?"))
  runny_nose = str(input("Is your nose runny?"))
  sneezing = str(input("Have you been sneezing frequently?"))
  shortness_of_breath = str(input("Do you have any difficulty in breathing?"))
  sore_throat = str(input("Do you have a sore throat?"))
  fever = str(input("Do you have a fever?"))
  night_sweats = str(input("Do you sweat in the night?"))
  chills = str(input("Have you been getting chills recently?"))
  headache = str(input("Hav you been getting headaches recently?"))
  loss_of_smell = str(input("Have you lost your sense of smell?"))
  fatigue = str(input("Have you been feeling tired and getting a lot of fatigue?"))
  Time=int(input("How long did it take for symptoms to show"))
  listof=["Cancer","Chronic kidney disease","Chronic Lung disease","Dementia","Neurological Conditions","Diabetes","Down Syndrome","Heart conditions","HIV","Weakened Immune system","Mental Health conditions","Overweight and obesity","Sickle cell disease","smoking, current of former","substance use disorders","Tuberculosis"]
  print(listof)
  dis=str(input("Do you find yourself in any of these conditions and diseases?"))
  if dis=="yes" and cough=="yes" and runny_nose=="yes" and sneezing=="yes" and shortness_of_breath=="yes" and sore_throat=="yes"and fever=="yes" and night_sweats=="yes" and chills=="yes" and headache=="yes" and loss_of_smell=="yes" and fatigue=="yes":
    print("please take appropriate precation moving forward.")
  
  elif dis=="yes" and cough=="no" and runny_nose=="no" and sneezing=="no" and shortness_of_breath=="no" and sore_throat=="no" and fever=="no" and night_sweats=="no" and chills=="no" and headache=="no" and loss_of_smell=="no" and fatigue=="no":
    print("be careful as you are in dagerous condition.")
  
  elif dis=="no" and cough=="yes" and runny_nose=="yes" and sneezing=="yes" and shortness_of_breath=="yes" and sore_throat=="yes"and fever=="yes" and night_sweats=="yes" and chills=="yes" and headache=="yes" and loss_of_smell=="yes" and fatigue=="yes":
    print("")
  
  elif dis=="no" and cough=="no" and runny_nose=="no" and sneezing=="no" and shortness_of_breath=="no" and sore_throat=="no" and fever=="no" and night_sweats=="no" and chills=="no" and headache=="no" and loss_of_smell=="no" and fatigue=="no":
    print("ef")
  

  
print("Welcome to the COVID Predictor")
Name=str(input("What is your name?"))
Age=int(input("What is your age?"))
if Age>=60:
  dose=int(input("How many doses  of vaccination have you taken?"))
  if dose<2:
    print("Please take",str(2-dose),"doses, along with a booster dose")
    symptoms()
  elif dose==2:
    print("Good Job, but take a booster dose to increase your safety")  
    symptoms() 
  else:
    print("Great Job, now follow all COVID precautions")
    symptoms()
else:
  print("Please take the required amount of doses for your age, and follow corona protocols at all times.")
  symptoms()







