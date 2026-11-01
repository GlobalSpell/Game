import random
player_name = input("Введите имя игрока: ")
player_hp = 100
player_damage = 15
gold = 50 

monster_name = "Mонстер"
monster_damage = 5
monster_hp = 50

def init_map():
    game_map =[[ 'F' for _ in range(5)] for _ in range(5)]  # Создаём пустую карту 5x5?

    item_to_place = ['G', 'G', 'G', 'G', 'M', 'M', 'M']  # Список предметов для размещения
    for item in item_to_place:
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            if game_map[row][col] == 'F':
                game_map[row][col] = item
                break
    return game_map

def display_map(game_map, player_position): 
    #Выводим карту в консоль
    print("\n" * 3) 
    for row in range(len(game_map)):  
        for col in range(len(game_map[0])): 
            if [row, col] == player_position: 
                print('P', end=' ') 
            else:
                print(game_map[row][col], end=' ') 
        print()

def move_player(game_map, player_position, direction, ):
    max_row = len(game_map) - 1 #Получаем максимальное количество строк в карте 
    max_col = len(game_map[0]) - 1 #Получаем максимальное количество столбцов в карте
    row, col = player_position #Получаем текущую позицию игрока
    
        
    if direction =='w': #ХОД НА СЕРВЕР
         if row >0:
            print(f"\n{player_name} шагаешь на север")
            return (row - 1, col)
         else:
            print(f"\n{player_name} на севере тупик - там край карты ") #ЕСЛИ ЗА КАРЙ 
            return row, col
         
    elif direction == 's': #ХОД НА ЮГ 
        if row < max_row:
            print(f"\n{player_name} шагаешь на юг")       
            return (row + 1, col)
        else:
            print(f"\n{player_name} на юге обрыв - там край карты!") #ЕСЛИ ЗА КАРЙ
            return row, col
    elif direction == 'a': #ХОД НА ЗАПАД
        if col > 0:
            print(f"\n{player_name} шагаешь на запад")
            return(row, col -1)
        else:
            print(f"\n{player_name} на западе тупик - там край карты!") #ЕСЛИ ЗА КАРЙ
            return (row, col)
       
    elif direction == 'd': #ХОД НА ВОСТОК
        if col < max_col:
            print(f"\n{player_name} шагаешь на восток")
            return (row, col + 1)
        else:
            print(f"\n{player_name} на востоке тупик - там край карты!")
            return( row, col) 
    else:
        print(f"\n{player_name} Неверное направление движения!")
        return( row, col) 
game_map = init_map() #Инициализируем карту
player_position = [0,0] #Начальная позиция игрока

while True: 
    display_map(game_map, player_position) #Отображаем карту

    direction = input ("Куда идём? (w/a/s/d)")  #Список возможных направлений движения
    previous_position = list(player_position) #Сохраняем предыдущую позицию игрока
    player_position = move_player(game_map, player_position, direction)
    row, col = player_position #Получаем текущую позицию игрока

    if game_map[row][col] == 'M':
        choice = input(f"{player_name} Ты встретил монстра {monster_name} и начинаешь сражаться. Хочешь сражаться или убежать? (1 - атаковать, 2 - убежать): ").strip()
   
        if choice == '1':
            while monster_hp > 0 and player_hp > 0:
                print(f"{player_name} Ты наносишь {player_damage} урона {monster_name} получает {player_damage} урона")
                monster_hp -= player_damage 
                print(f"У {monster_name} осталось здоровья: {monster_hp}")  

                input("Нажми Enter для продолжения боя...")

                if monster_hp <= 0:
                    print(f"\n{monster_name} умер")
                    print(f"{player_name} победил")
                    gold += 20
                    print(f"{player_name} получил {gold} золота")
                    game_map[row][col] = 'F'
                    monster_hp = 50 
                    player_hp = 25
                    print(f"{player_name} Ты восстановил здоровье до {player_hp}")
                    input("Нажми Enter для продолжения боя...")   
                    break
    
                print(f"{monster_name} наносит {monster_damage} урона {player_name} получает {monster_damage} урона")
                player_hp -= monster_damage
                print(f"У {player_name} осталось здоровья: {player_hp}")

                input("Нажми Enter для продолжения боя...")

                if player_hp <= 0:
                    print(f"\n{player_name} проигра в битве с {monster_name}.")
                    player_hp = 100
                    player_position = [0, 0]  # Возвращаем игрока в начальную позицию
                    monster_hp = 50 # Восстанавливаем здоровье монстра
                    print(f"{player_name} Ты возвращаешься на предыдущую позицию.")
                    input("Нажми Enter для продолжения...")
                    break
        else: 
            print(f"\n{player_name} Ты встретил монстра {monster_name} и решил убежать. Ты возвращаешься на предыдущую позицию.")
            player_position =  previous_position 
            input("Нажми Enter для продолжения...")
          
    elif game_map[row][col] == 'G':
        print(f"\n{player_name} Ты нашёл золото! Ты получаешь 15 золота.")
        gold += 15
        print(f"{player_name} Твой баланс золота: {gold}")
        game_map[row][col] = 'F'  # Убираем золото из карты
