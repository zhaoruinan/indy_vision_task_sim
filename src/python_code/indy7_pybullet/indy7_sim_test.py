import pybullet as p
import time
p.connect(p.GUI)
planeId = p.loadURDF("plane.urdf", [0, 0, 0])
indyId= p.loadURDF("indy7.urdf", [0, 0, 0])
p.resetBasePositionAndOrientation(indyId, [0, 0, 0.03], [0, 0, 0, 1])
time.sleep(1000)
p.disconnect()