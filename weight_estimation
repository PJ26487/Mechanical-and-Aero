#POWER MODULE 2 
#second version of the weight estimation program
#the rotor mechanics have not been inducted into the program yet
#this program aims to create a more realistic approach to weight estimation as compared to the last one
#the weight of the electronics, motors, wings after an input of the AR, efficiency, diamater and CD will be looked at
#The dissertation that Cees had provided to us will be references
#on the suggestion of the coordinator the program will assume all cruise operations take place with an ICE 
cont1="yes"
#operational constant specifications
print("do not enter caps or space in the options")
while cont1=="yes":
    payload_mass= 50 #mass of payload in kg
    payload_weight= payload_mass*9.81 #the weight of the payload in N
    CL_cruise= 0.5
    CL_loiter= 0.7
    CD0= 0.034 #the zero drag coeff will be considered to be 0.034 for now considering the worst possible value
    LD_ratio_ratio= CL_cruise/CD0
    elec_motor_eff= 0.9
    prop_eff= 0.7
    gen_eff= 0.9
    ICE_eff= 0.31
    density= 0.9711 #based on the calcs given for 35C and 1350m where the aircraft has to perform
    mass_initial= float(input("enter the initial mass estimation"))
    specific_energy_batt= 0.2 #specific energy of the battery in kwhr/kg
    specific_energy_fuel= 2.5 #specific energy of petrol/diesel in KWhr/kg
    weight_initial=mass_initial*9.81
    b=2 #the max length of the wing
    wing_loading= 150 #the maximum wing loading of the aircraft in kg/m2
    CD=0.3
    power_density_motor =5 #the power density of an electric motor in KW/kg
    number_of_rotors= int(input("enter the number of rotors"))
    dia_rotor= float(input("enter the diameter of the rotor in m"))
    mass_airframe= 50 #mass of the empty airframe
    mass_elec= 10
    cont= "yes"
    i=0
    
    #flight profile specifications
    opt0= int(input("enter 1 for specifying pre planned mission 2 for selecting custom mission"))
    if opt0==1:
        opt1 = input("which operation would you like to specify delivery or logistics?")
        while cont=="yes":
            count= int(input("how many iterations would you like to run?"))
            while i<count:
    
            #hover calculation
                take_off_time= 120 #time of Vertical take off to reach 150 m height
                thrust_factor= 0.95 #the value of max thrust that can be used during take-off
                area_rotor= 3.14*(dia_rotor**2)*number_of_rotors/4
                if opt1=="delivery":
                    time_hover= (2+1+1)*60 # 2 minutes hover after take off, 1 minute hover in delivery and 1 minute hover for landing
                else:
                    time_hover= (2+1)*60
                emergency_time= 1*60 #hover time required in emergency to run at 100 percent power
                thrust_hover = (mass_initial+payload_mass)*9.81 #thrust in N
                power_hover= (thrust_hover**1.5)/((2*density*area_rotor)**0.5)#power required in W
                #print("power for hover")
                #print(power_hover)
                power_motor= power_hover/prop_eff #power to be supplied by the motor to offset inefficiencies by the propellor
                #print("power of motor")
                #print(power_motor)
                power_batt= power_motor/elec_motor_eff #power to be supplied by the battery to offset inefficiencies by the motor
                #print("power provided by the battery")
                #print(power_batt)
                power_batt_KW= power_hover/1000 #power to be supplied by the battery for hovering 
                energy_hover= power_batt*time_hover #energy for hover in J
                energy_hover_KWhr= energy_hover/3600000
                #print("energy required to hover in KWhr is")
                #print(energy_hover_KWhr)
                batt_mass_hover= energy_hover_KWhr/specific_energy_batt #mass of the battery in kg
                #print("mass of battery for hover is")
                #print(batt_mass_hover)
            #motor specifications
                motor_mass= power_motor/(power_density_motor*1000) #the mass of the motor(s) in kg
                motor_power_100= power_motor/0.90 #the 100% power the motor must be rated for
                emergency_motor_power= motor_power_100*1.50 #the emergency power the motor must be able to provide
                #print("mass of the motor is")
                #print(motor_mass)
            #climb calculations will only consider the VTOL component of the flight
                if opt1=="delivery":
                    time_climb=4*60 #time of climb in seconds
                else:
                    time_climb=2*60
                power_batt_climb= motor_power_100/elec_motor_eff
                power_batt_climb_KW= power_batt_climb/1000
                #print("power required to climb is")
                #print(power_batt_climb)
                energy_climb= power_batt_climb*time_climb
                energy_climb_KWhr= energy_climb/3600000
                batt_mass_climb= energy_climb_KWhr/specific_energy_batt
                #print("mass of battery for climb is")
                #print(batt_mass_climb)
                    
            #cruise consideration
                    
                #aero calcs
                if opt1=="delivery":
                    cruise_time= (14+15)*60 #time of cruise in seconds
                else:
                    cruise_time=(70)*60
                cruise_velocity=220*5/18 #velocity of aircraft during cruise
                #print("cruise velocity in m/s is")
                #print(cruise_velocity)
                chord_length = mass_initial*9.81/(b*wing_loading)
                wing_area= b*chord_length
                #print("the wing area is")
                #print(wing_area)
                CL_cruise= 2*((mass_initial+payload_mass)*9.81)/(density*wing_area*(cruise_velocity**2))
                V3= (2*mass_initial/(density*wing_area*CL_cruise))**1.5
                #considering the cruise is done by the internal combustion engine
                P_shaft_cruise= (1/(2*prop_eff))*density*V3*wing_area*CD
                #print("power required by engine to cruise")
                #print(P_shaft_cruise)
                P_shaft_cruise_KW=P_shaft_cruise/1000
                #print("power required by engine to cruise in KW")
                #print(P_shaft_cruise_KW)
                P_cruise= P_shaft_cruise/ICE_eff
                energy_cruise_KWhr= P_cruise*cruise_time/3600000
                #print("energy required for cruise in KWhr")
                #print(energy_cruise_KWhr)
                fuel_mass= energy_cruise_KWhr/specific_energy_fuel
                #print("mass of the fuel is")
                #print(fuel_mass)
                m_inline_ICE= 2.93+(P_shaft_cruise_KW**0.780)
                #print("mass of dry engine is")
                #print(m_inline_ICE)
                m_inline_acc=0.25*(2.93+(P_shaft_cruise_KW**0.780))*(ICE_eff**0.67)
                #print("mass of engine components")
                #print(m_inline_acc)
                m_inline=m_inline_ICE+m_inline_acc
                #print("mass of the engine is")
                #print(m_inline)
                P_shaft_100= P_shaft_cruise/0.75
                    
            #loiter considerations
                    
                time_loiter= 15*60 #time the aircarft needs to fly in loiter situation for aircraft
                #the CD0 will be taken for the loiter case
                P_shaft_loiter= (1/(2*prop_eff))*density*(V3)*wing_area*CD0
                P_shaft_loiter_KW= P_shaft_loiter/1000 #the shaft power required in KW
                P_loiter= P_shaft_loiter/ICE_eff
                energy_loiter_KWhr= P_loiter*cruise_time/3600000
                fuel_mass_loiter= energy_loiter_KWhr/specific_energy_fuel
                #print("mass of fuel for loiter is")
                #print(fuel_mass_loiter)
                
            #emergency power
                #VTOL motors to run for 5 minutes at 100 percent power
                #The internal combustion engine will operate at 100 percent power for 15 minutes 
                energy_emergency_cruise= P_shaft_100*15*60
                energy_emergency_cruise_KWhr= energy_emergency_cruise/3600000
                energy_emergency_hover= motor_power_100*5*60
                energy_emergency_hover_KWhr= energy_emergency_hover/3600000
                batt_mass_emergency= energy_emergency_hover_KWhr/specific_energy_batt
                #print("mass of battery is")
                #print(batt_mass_emergency)
                fuel_mass_emergency= energy_emergency_cruise_KWhr/specific_energy_fuel
                #print("mass of emergency fuel system")
                #print(fuel_mass_emergency)

            #onboard electronics
                power_consumption_elec= 150 #power consumption by onboard electronics
                if opt1=="delivery":
                    time_sortie= 50*60
                else:
                    time_sortie= 80*60
                energy_electronics= power_consumption_elec*time_sortie
                energy_electronics_KWhr= energy_electronics/36000000
                batt_mass_electronics= energy_electronics_KWhr/specific_energy_batt
                batt_mass= batt_mass_hover+batt_mass_climb+batt_mass_emergency
                fuel_mass= fuel_mass+fuel_mass_loiter+fuel_mass_emergency
                powerplant_mass= batt_mass_hover+motor_mass+batt_mass_climb+fuel_mass+m_inline+fuel_mass_loiter+batt_mass_emergency+fuel_mass_emergency
                final_mass= powerplant_mass+mass_airframe+mass_elec+payload_mass
                #print("final mass is")
                print(final_mass)
                mass_initial= final_mass
            #loop repository
                i=i+1
            final_mass= 1.2*final_mass #just to make sure that the design of further components has a factor of safety
            print("the final mass is")
            print(final_mass)
            print("the mass of the battery is")
            print(batt_mass)
            print("the mass of the fuel is")
            print(fuel_mass)
            cont= input("do you wish to run more iterations for conversion?")
    else:
        print("LOL you wish")

    cont1= input("do you wish to restart the program?")
