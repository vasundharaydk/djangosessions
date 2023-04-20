from django.shortcuts import render,redirect
import random

def home(request):
    return render(request, 'handcrik/game.html')

def play_game(request):
    win_messege = ''
    if request.method == 'POST':
        player_choice = int(request.POST.get('player_choice'))
        # print(player_choice)
        computer_choice = random.randint(1, 6)
        score = int(request.session.get('score', 0))
        if player_choice == computer_choice:
            score = 0
            win_messege = 'player_out'
            
          
        else:
            runs = player_choice
            score += runs

        request.session['score'] = score
      
        scorecard = { 'score': score,'win_messege':win_messege,'computer_choice':computer_choice,'player_choice':player_choice,}
        return render(request, 'handcrik/game.html', {'scorecard': scorecard})
    else:
        return redirect('home')
