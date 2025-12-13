import pyhula
import time
import math
import sys

# class BlockNode:
#     def __init__(self, x: int, y: int, parent: BlockNode = None) -> None:
#         self.x = x
#         self.y = y
#         self.parent = parent

api = pyhula.UserApi()

if not api.connect():
    print("connect error")
    sys.exit(0)
else:
    print("connection to station by wifi")

def move_to_coordinates(x, y, z):
    print(f"moving to coordinates: [X: {x}, Y: {y}, Z: {z}]")
    api.single_fly_straight_flight(x, y, z)
    time.sleep(2)

def move_to_elevation(z):
    c = api.get_coordinate()
    move_to_coordinates(c[0], c[1], z)

def take_off():
    print("---------taking off")
    api.Plane_cmd_switch_QR(0)
    time.sleep(1)
    api.single_fly_takeoff()
    time.sleep(2)

def land():
    print("---------landing")
    api.single_fly_touchdown()
    time.sleep(2)

def center_at_current_block():
    print("centering at current block")
    x, y, z = api.get_coordinate()
    print(f"current coordinates: [X: {x}, Y: {y}, Z: {z}]")

    if x < 0:
        x = 0
    if y < 0:
        y = 0
    print(f"after zeroing: [X: {x}, Y: {y}, Z: {z}]")

    center_x = math.floor(x / 60.0) * 60 + 15
    center_y = math.floor(y / 60.0) * 60 + 15
    print(f"center coordinates: [X: {center_x}, Y: {center_y}, Z: {z}")
    move_to_coordinates(center_x, center_y, z)

def center_yaw():
    print("centering yaw")
    yaw, pitch, roll = api.get_yaw()
    print(f"current yaw: {yaw}")
    if yaw > 0:
        print("turning right")
        api.single_fly_turnleft(yaw)
    if yaw < 0:
        print("turning left")
        api.single_fly_turnright(yaw * -1)

def move_to_block(x, y):
    print(f"moving to block: [X: {x}, Y: {y}]")
    target_x = 60 * x + 15
    target_y = 60 * y + 15
    print(f"target coordinates: [X: {target_x}, Y: {target_y}]")
    move_to_coordinates(target_x, target_y, 80)

take_off()
move_to_elevation(80)
center_at_current_block()
center_yaw()

# path = [
#     [0, 0],
#     [0, 1],
#     [0, 2],
#     [1, 2],
#     [1, 1],
#     [1, 0],
#     [2, 0],
#     [3, 0],
#     [3, 1],
#     [3, 2]
# ]

# for x, y in path:
#     move_to_block(x, y)

land()
