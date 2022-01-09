
import pickle
import numpy as np
import sklearn
import pandas as pd
from flask import Flask,render_template,request

app=Flask(__name__)
model=pickle.load(open("flightprice.pkl","rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method == "POST":
        
        airline=request.form["airline"]
        if (airline=="Jet Airways"):
            
            Jet_Airways=1
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujetet_Airways=0
            
        elif (airline=="IndiGo"):
            
            Indigo=1
            Jet_Airways=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujetet_Airways=0
        
        elif (airline=="Air_India"):
            
            Air_India=1
            IndiGo=0
            Jet_Airways=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujetet_Airways=0
            
            
        elif (airline=="Multiple_carriers"):
            
            Multiple_carriers=1
            IndiGo=0
            Air_India=0
            Jet_Airways=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujetet_Airways=0
            
        elif (airline=="SpiceJet"):
            
            SpiceJet=1
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            Jet_Airways=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujetet_Airways=0
            
        elif (airline=="Vistara"):
            
            Vistara=1
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Jet_Airways=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujetet_Airways=0
            
        elif (airline=="GoAir"):
            
            GoAir=1
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            Jet_Airways=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujetet_Airways=0
            
        elif (airline=="Multiple_carriers_Premium_economy"):
            
            Multiple_carriers_Premium_economy=1
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Jet_Airways=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujetet_Airways=0
            
        elif (airline=="Jet_Airways_Business"):
            
            Jet_Airways_Business=1
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways=0
            Vistara_Premium_economy=0
            Trujetet_Airways=0
            
        elif (airline=="Vistara_Premium_economy"):
            
            Vistara_Premium_economy=1
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Jet_Airways=0
            Trujetet_Airways=0
       
        elif (airline=="Trujetet_Airways"):
            
            Trujetet_Airways=1
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Jet_Airways=0
            Vistara_Premium_economy=0
            
            
        else:
            
            Trujetet_Airways=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Jet_Airways=0
            Vistara_Premium_economy=0
            IndiGo=0
            
        
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0

        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1

        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            
        
            
        Destination=request.form["Destination"]
        
        if (Destination == 'Delhi'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif (Destination == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Destination == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Destination == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif (Destination == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0 
            
        
        dep_time=request.form["Dep_Time"]
        Journey_day=int(pd.to_datetime(dep_time).day)
        Journey_month=int(pd.to_datetime(dep_time).month)
        
        Dep_hour=int(pd.to_datetime(dep_time).hour)
        Dep_min=int(pd.to_datetime(dep_time).minute)
        
        arr_time=request.form["Arrival_Time"]
        Arrival_hour=int(pd.to_datetime(arr_time).hour)
        Arrival_min=int(pd.to_datetime(arr_time).minute)
        
        #Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        
        dur_hour=abs(Arrival_hour-Dep_hour)
        dur_min=abs(Arrival_min-Dep_min)
        
        Total_stops=int(request.form["stops"])
        
      
            
        prediction=model.predict([[
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujetet_Airways,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi,
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min]]) 
        
        
        output=round(prediction[0],2)
            
        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)