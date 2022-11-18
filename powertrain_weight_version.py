#powertain beta version
#creating a program for finding energy required in each phase of flight

#test for checking user input values

#THIS CODE DOES NOT INCLUDE THE VALUES FOR REDUNDANT SYSTEM OR EMERGENCY YET PROCEDURES YET

#formulas to be used for this
#the total hover time will be exactly 10 minutes
#the total forward cruise flight time will be 60 minutes
#in cruise mode the speed will increase from 0 to 200 km/h and reduce to 0 again for landing

cont_main= "yes"  

while cont_main== "yes":

    flight_speed_average = float(input("enter average cruise flight speed"))
    time_cruise= float(input("enter time of cruise flight in minutes"))
    CL= 0.75 
    CD= 0.06
    LD_ratio= CL/CD
    elec_motor_eff= 0.9
    prop_eff= 0.7
    gen_eff= 0.9
    ICE_eff= 0.31
    initial_mass= float(input("enter the initial mass estimation for the aircraft"))
    payload_mass= 50
    density= 1.0225
    elipson= 0.8 #wing oswald's factor used a generic value from the stackexchange
#aero considerations 
    velocity= flight_speed_average*5/18
    min_wing_area= (2*initial_mass*9.81)/(density*CL*velocity**2) #will provode the minimum wing area while in flight
    power_required = ((initial_mass+payload_mass)*velocity*9.81)/(CL/CD)
    power_required_KW= power_required/1000
    power_required_actual= power_required_KW*elec_motor_eff*prop_eff*gen_eff
    print ("power required in KW is")
    print (power_required_actual)
    energy_required = power_required_actual*time_cruise*60/1000
    print ("the energy required for cruise in MJ is:")
    print (energy_required)
#power required for the hover and climb
    number_of_rotors= int(input("enter the number of rotors"))
    dia_rotor= float(input("enter the diameter of the rotor in m"))
    area_rotor= 3.14*(dia_rotor**2)*number_of_rotors/4
    time_hover= int(input("time required for hover of aircraft in minutes"))
    time_hover_seconds= time_hover*60
    K=(2*(9.81**3)/(density*3.14))**0.5
    power_hover= K*((initial_mass+payload_mass)**1.5)/(dia_rotor/2)
    power_hover_KW= power_hover/1000
    power_hover_actual= power_hover_KW*elec_motor_eff*prop_eff*gen_eff
    print ("power required for hover in KW")
    print (power_hover_actual)
    energy_hover = power_hover_actual*time_hover_seconds/1000
    print("energy required for hover in MJ")
    print(energy_hover)
#finding the total energy available 
    total_energy= energy_hover+ energy_required
    total_energy_kwhr= total_energy*0.27778
    print ("total energy storage in KWhr")
    print (total_energy_kwhr)
#power carrier information

    specific_energy_batt= 0.2 #specific energy of the battery in kwhr/kg
    specific_energy_fuel= 2.5 #specific energy of petrol in KWhr/kg
    
#internal combustion engine values
    P= float(input("enter the degree of hybridization"))
    P_frac=P/100
    m_inline_ICE0= 2.93+((P_frac-0.01)*(power_required/1000+power_hover/1000)**0.780)
    m_inline_ICE= 2.93+(P_frac*(power_required/1000+power_hover/1000)**0.780)#mass of the inline dry engine
    m_inline_acc0=0.25*(2.93+(P_frac-0.01)*(power_hover/1000+power_required/1000)**0.780)*(ICE_eff**0.67)
    m_inline_acc=0.25*(2.93+(P_frac*(power_hover/1000+power_required/1000)**0.780))*(ICE_eff**0.67)# mass of the inline engine accesories
    m_inline0=m_inline_ICE0+m_inline_acc0
    m_inline=m_inline_ICE+m_inline_acc #total inline engine mass
    print("mass of the engine is")
    print(m_inline)
    fuel_mass0=((P_frac-0.01)*total_energy_kwhr)/(specific_energy_fuel*ICE_eff)
    fuel_mass=P_frac*total_energy_kwhr/(specific_energy_fuel*ICE_eff)#mass of fuel to run the engine at 30.7% fuel efficiency
    print("mass of the fuel is")
    print(fuel_mass)
#battery values
    batt_mass_1= total_energy_kwhr*(1-P_frac+0.01)/(specific_energy_batt)
    batt_mass_100= total_energy_kwhr*(1-P_frac)/(specific_energy_batt) #mass of the battery in kg
    print("the mass of the battery is")
    print(batt_mass_100)
    chass_mass= 40 #mass of the airframe without battery in kg 
    elec_mass= 10 #mass of electronic components in kg
#final mass of the components
    final_mass0= batt_mass_1+chass_mass+elec_mass+m_inline0+fuel_mass0+payload_mass
    final_mass= batt_mass_100+chass_mass+elec_mass+m_inline+fuel_mass+payload_mass    
    print ("the final mass of the system is")
    print (final_mass)

#from this we notice that the internal combustion engine will always be lighter than hybrid designs
# we need to approach this in a way that gives us the least amount of energy that is used


    cont= "yes" 
    while cont=="yes":
        iteration = int(input("how many times would you like the code to run"))
        i=0
        while i< iteration:
            LD_ratio=5
            CL= 0.75 
            CD= 0.25
            elec_motor_eff= 0.75
            prop_eff= 0.7
            initial_mass= final_mass #mass the iteration starts with 
            payload_mass= 50 #mass of the payload in kgs
            velocity = flight_speed_average*5/18 #velocity of the aircaft converted to m/s
            power_required = ((initial_mass+payload_mass)*velocity*9.81)/(1000*CL/CD) #power required for cruise
            power_required_actual= power_required*elec_motor_eff*prop_eff*gen_eff
            energy_required = power_required_actual*time_cruise*60/1000 #energy storage for cruise in MJ
            #print("energy required for cruise")
            #print(energy_required)
            power_hover= K*((initial_mass+payload_mass)**1.5)/(dia_rotor/2)#power required by the aircraft to hover
            power_hover_actual= power_hover*elec_motor_eff*prop_eff*gen_eff
            energy_hover = power_hover_actual*time_hover_seconds/1000000 #energy to be stored by the aircraft in MJ
            #print ("energy required to hover")
            #print(energy_hover)
            total_energy= energy_hover+ energy_required #total energy stored by the aircraft 
            total_energy_kwhr= total_energy*0.27778 #total energy to be stored by the aircraft in KWhr
            m_inline_ICE= 2.93+(P_frac*(power_required/1000+power_hover/1000)**0.780)#mass of the engine block
            m_inline_acc=0.25*(2.93+(P_frac*(power_hover/1000+power_required/1000)**0.780))*(ICE_eff**0.67)#mass of the engine components
            m_inline= m_inline_ICE+m_inline_acc
            #print("mass of total engine is")
            #print(m_inline)
            fuel_mass=P_frac*total_energy_kwhr/(specific_energy_fuel*ICE_eff)
            #print("mass of fuel is")
            #print(fuel_mass)
            batt_mass_100= total_energy_kwhr*(1-P_frac)/(specific_energy_batt)
            #print("mass of battery is")
            #print (batt_mass_100)
            final_mass= batt_mass_100+chass_mass+elec_mass+m_inline+fuel_mass+payload_mass
            #print("the final mass is")
            print (final_mass)
            i=i+1
        print ("the final mass is")
        print(final_mass)
        print("the battery mass is")
        print(batt_mass_100)
        print("mass of the fuel is")
        
        cont= input("do you wish to reiterate the conversion yes/no")
        if (cont=="no"):
            break
    cont_main= input("Do you wish to restart the program yes/no?")

    if (cont_main=="no"):
        break
    
    
#at this point the entire code needs to run again
#the battery that will be used for this purpose will be the tesla battery
#the powertrain in this case will be modelled using hybrid electric systems
##the cost of operation needs to be the lowest, this may mean the lowest operating power cost or operting with
#maximum energy supplied by the batteries and the motor
