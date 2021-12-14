import pybullet as p
import time
import numpy as np
objects = ['apple', 'orange', 'banana', 'milk', 'orange']
p.connect(p.GUI)
p.setGravity(0, 0, -9.8)
#planeId = p.loadURDF("plane.urdf", [0, 0, 0])
TableId = p.loadURDF("table/table.urdf", [0.45, 0.35, -0.65])
indyId= p.loadURDF("indy7.urdf", [0, 0, 0])
num_obj = len(objects)
obj_postions = np.random.rand(num_obj,2)
z_postion = np.empty(num_obj); z_postion.fill(0.2)
obj_postions = np.c_[ obj_postions, z_postion ] 
print(obj_postions)
for object in objects:
    obj_path = "models/urdf/"+object+".urdf"
    objId = p.loadURDF(obj_path, obj_postions[-1,])
    obj_postions = np.delete(obj_postions, -1, 0)
#appleId = p.loadURDF("models/urdf/apple.urdf", [-0.4, 0, 0.1])

p.resetBasePositionAndOrientation(indyId, [0, 0, 0.03], [0, 0, 0, 1])
p.setRealTimeSimulation(1) 
time.sleep(1000)
p.disconnect()