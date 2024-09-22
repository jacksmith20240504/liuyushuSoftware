from enum import Enum,Flag,auto 


# class Color(Enum):
#     RED: str = 'R'
#     GREEN: str = 'G'
#     BLUE: str = 'B'
    
# # -> 是函数注解的一部分，表示函数的返回值类型提示
# def create_car(color:Color) -> None:
#     match color:
#         case Color.RED:
#              print (f'红车来了')
#         case Color.BLUE:
#              print (f'蓝车来了')
#         case Color.GREEN:
#              print (f'绿车来了')
#         case _:
#             print(f'没有这个{color}色的车')      

# create_car(Color.GREEN)      
             

# class Color(Flag):    
#     RED: int = 1
#     GREEN: int =2
#     BLUE:int=4
#     YELLOW:int =8
#     BLACK:int = 16
    
# cool_colors: Color = Color.RED | Color.YELLOW | Color.BLACK
# my_car_color: Color = Color.RED 

# if my_car_color in cool_colors:
#     print ('You have a cool car!')
# else:
#     print ('Sorry,your car is not cool.')
    
    
# class Color(Flag):    
#     RED:int = auto()
#     GREEN: int = auto()
#     BLUE:int= auto()
#     YELLOW:int = auto()
#     BLACK:int = auto()
#     ALL:int = RED | GREEN  | BLACK | YELLOW | BLACK

# print(Color.RED.value)
# print(Color.GREEN.value)
# print(Color.BLUE.value)
# print(Color.YELLOW.value)
# print(Color.BLACK.value)

# print(Color.ALL.value)

# print(Color.RED in Color.ALL)


class State(Enum):
    OFF:int = 0
    ON:int = 1
    
switch: State = State.OFF

match switch:
    case State.ON:
        print('灯开')
    case State.OFF:
        print('灯关')
    case _:
        print('正在等待正确指令')