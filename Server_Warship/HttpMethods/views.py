from django.shortcuts import render
from django.http import HttpResponse
from HttpMethods.models import Board, Player, Ship, Update, Base
from django.views.decorators.csrf import csrf_exempt
import json
import random as rd

number_of_ships = Base.number_of_ship

def index(request):
    all_boards = Board.objects.get(code=1)
    return HttpResponse(all_boards)
def first(request):
    return render(request, 'first.html')
def start_game(request):
    return HttpResponse("Hello, world. You're at the start_game index.")

@csrf_exempt
def create_board(request):
    response_data = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        code = Board.objects.count() + 1
        board = Board.objects.create(code=code, num_player=1)
        creater = Player.objects.create(name=name, board=board)
        Update.objects.create(name=name, front=1, change=0, board=board)
        for i in range(number_of_ships):
            Ship.objects.create(number=i + 1, owner=creater, board=board, Hp=rd.randint(50, 100), Atk=rd.randint(10, 30))
        response_data = {}
        response_data["status"] = "Ok"
        response_data["board"] = code
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        response_data["status"] = "Wrong Method"
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    
@csrf_exempt
def join_board(request):
    response_data = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        code = int(request.POST.get('board'))
        if code not in [board.code for board in Board.objects.all()]:
            response_data["status"] = "Board does not exist"
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        board = Board.objects.get(code=code)
        if name in [player.name for player in Player.objects.filter(board=board)]:
            response_data["status"] = "Name already exists"
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        if board.num_player == 2:
            response_data["status"] = "Board is full"
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        board.num_player += 1
        board.save()
        player = Player.objects.create(name=name, board=board)
        for i in range(number_of_ships):
            Ship.objects.create(number=i + 1, owner=player, board=board, Hp=rd.randint(50, 100), Atk=rd.randint(10, 30))
        response_data["status"] = "Ok"
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        response_data["status"] = "Wrong Method"
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    
@csrf_exempt
def send_status(request):
    respond_data = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        code = int(request.POST.get('board'))
        if code not in [board.code for board in Board.objects.all()]:
            respond_data["status"] = "Board does not exist"
            return HttpResponse(json.dumps(respond_data), content_type="application/json")
        board = Board.objects.get(code=code)
        if name not in [player.name for player in Player.objects.filter(board=board)]:
            respond_data["status"] = "Name does not exist"
            return HttpResponse(json.dumps(respond_data), content_type="application/json")
        #when player is 1
        if board.num_player == 1:
            respond_data["status"] = "Wait"
            return HttpResponse(json.dumps(respond_data), content_type="application/json")
        #when player is 2
        respond_data["status"] = "Ok"
        respond_data["commands"] = ["1", "2", "3"]
        player = Player.objects.get(name=name, board=board)
        respond_data["can_front"] = [ship.number for ship in Ship.objects.filter(owner= player, board=board) if ship.Hp > 0 and ship.number != player.front]
        status = 30 * "=" + "\n"
        status += f"Board code: {board.code}\n"
        turn = board.turn
        update = Update.objects.get(board=board)
        players = Player.objects.filter(board=board)
        for player in players:
            status += f"Player {player.name}'s ships status:\n"
            for ship in Ship.objects.filter(owner=player, board=board):
                status += f"Ship {ship.number} Hp: {ship.Hp if ship.Hp > 0 else 0} " 
                if (update.change != 0 and update.name == player.name and update.front == ship.number):
                    status += "(+" if update.change > 0 else "(" 
                    status += str(update.change) + ") "
                status += f"Atk: {ship.Atk} " 
                status += "(front)" if (ship.number == player.front and ship.Hp > 0) else ""
                status += "(destroy)" if ship.Hp <= 0 else ""
                status += "\n"
        status += 30 * "=" + "\n"
        
        if board.status:
            status += "Game Over\n"
            status += f"The Winner is {board.winner}\n"
            respond_data["your_turn"] = -1
            respond_data["announce"] = status
        else:
            if Player.objects.get(name=name, board=board) == players[turn]:
                respond_data["your_turn"] = 1
                respond_data["announce"] = status + f"It's your turn.\n" + "What R U gonna do? \n1. attack\n2. defense\n3. switch your front ship"
            else:
                respond_data["your_turn"] = 0
                respond_data["announce"] = status + f"It's Player {players[turn].name}'s turn.\n" + "Waiting for you opponent to make a dicision..."
        return HttpResponse(json.dumps(respond_data), content_type="application/json")
    else:
        respond_data["status"] = "Wrong Method"
        return HttpResponse(json.dumps(respond_data), content_type="application/json")

@csrf_exempt
def send_choice(request):
    respond_data = {}
    if request.method == "POST":
        name = request.POST.get('name')
        code = int(request.POST.get('board'))
        if code not in [board.code for board in Board.objects.all()]:
            respond_data["status"] = "Board does not exist"
            return HttpResponse(json.dumps(respond_data), content_type="application/json")
        board = Board.objects.get(code=code)
        if name not in [player.name for player in Player.objects.filter(board=board)]:
            respond_data["status"] = "Name does not exist"
            return HttpResponse(json.dumps(respond_data), content_type="application/json")
        
        players = Player.objects.filter(board=board)
        player = players[board.turn]
        enemy = players[1 - board.turn]
        update = Update.objects.filter(board=board)
        if players[board.turn].name == name:
            action = request.POST.get('action')
            temp = request.POST.get('temp')
            pship = Ship.objects.get(number=player.front, owner=player, board=board)
            if action == "1":
                eship = Ship.objects.get(number=enemy.front, owner=enemy, board=board)
                eship.Hp -= pship.Atk
                eship.save()
                if eship.Hp <= 0:
                    enemy.survive -= 1
                update.update(name=enemy.name, front=enemy.front, change=-pship.Atk)
                if enemy.survive == 0:
                    board.winner = player.name
                    board.status = 1
                else:
                    while eship.Hp <= 0:
                        enemy.front += 1;
                        if enemy.front > number_of_ships:
                            enemy.front -= number_of_ships
                        eship = Ship.objects.get(number=enemy.front, owner=enemy, board=board)
                    enemy.save()
            elif action == "2":
                pship.Hp += pship.Atk
                update.update(name=player.name, front=player.front, change=pship.Atk)
                pship.save()
            elif action == "3":
                player.front = int(temp)
                player.save()
            board.turn = 1 - board.turn
            board.save()
            respond_data["status"] = "Ok"
            return HttpResponse(json.dumps(respond_data), content_type="application/json")
        else:
            respond_data["status"] = "Not your turn"
            return HttpResponse(json.dumps(respond_data), content_type="application/json")