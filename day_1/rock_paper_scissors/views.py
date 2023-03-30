from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def game_view(request):
    if request.method == 'POST':
        player1_choice = request.POST.get('player1_choice')
        player2_choice = request.POST.get('player2_choice')
        
        if player1_choice == player2_choice:
            winner = "It's a tie!"
        elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
             (player1_choice == 'paper' and player2_choice == 'rock') or \
             (player1_choice == 'scissors' and player2_choice == 'paper'):
            winner = "Player 1 wins!"
        else:
            winner = "Player 2 wins!"
        
        return render(request, 'rock_paper_scissors/roc.html', {'winner': winner})
    else:
        return render(request, 'rock_paper_scissors/roc.html')