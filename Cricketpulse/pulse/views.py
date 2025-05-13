import json
import pickle
import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse
from pathlib import Path

with open('pipe.pkl', 'rb') as file:
    model = pickle.load(file)

def home(request):
    return render(request, 'index.html')

def predict_score(request):
    
    batting_team = request.GET['batting-team']
    bowling_team = request.GET['bowling-team']
    venue = request.GET['venue']
    current_score = int(request.GET['current-score'])
    overs_done = float(request.GET['overs-done'])
    wickets_out = int(request.GET['wickets-out'])
    run_scored_five_overs = int(request.GET['run-scored-five-overs'])
    balls_left = 120 - int(overs_done) * 6 - int((overs_done % 1) * 10)
    wickets_left = 10 - wickets_out
    crr = current_score/overs_done
    input_data = pd.DataFrame([{
              'batting_teams': batting_team,
              'bowling_team': bowling_team,
              'city': venue,
              'current_score': current_score,
              'balls_left': balls_left,
              'wickets_left': wickets_left,
              'last_five': run_scored_five_overs,
              'crr': crr
            }])
    
    y_pred = model.predict(input_data)[0]
    print(int(y_pred))
    return render(request,'result.html',{'result':int(y_pred)})