"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

range_val=50
limit_1=100
limit_2=10000
middle_const=0.01
speed_const=0.125

#boids_x=[random.uniform(-450,50.0) for x in range(range_val)]
#boids_y=[random.uniform(300.0,600.0) for x in range(range_val)]
#boid_x_velocities=[random.uniform(0,10.0) for x in range(range_val)]
#boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(range_val)]
#boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

class Boids(object):
  def __init__(self, input_list=None, flag=0 ):
    if flag==0:
      self.random_init()
    if flag==1:
      self.from_file(input_list)
    
  def random_init(self):
    self.x=[random.uniform(-450,50.0) for x in range(range_val)]
    self.y=[random.uniform(300.0,600.0) for x in range(range_val)]
    self.x_velocity=[random.uniform(0,10.0) for x in range(range_val)]
    self.y_velocity=[random.uniform(-20.0,20.0) for x in range(range_val)]
    
  def from_file(self, input_list):
    self.x=input_list[0]
    self.y=input_list[1]
    self.x_velocity=input_list[2]
    self.y_velocity=input_list[3]

boids=Boids()
#print boids.y
#print type(boids)

def update_boids(boids):
	xs,ys,xvs,yvs=boids.x, boids.y, boids.x_velocity, boids.y_velocity
	# Fly towards the middle
	for i in range(len(xs)):
		for j in range(len(xs)):
			xvs[i]=xvs[i]+(xs[j]-xs[i])*middle_const/len(xs)
	for i in range(len(xs)):
		for j in range(len(xs)):
			yvs[i]=yvs[i]+(ys[j]-ys[i])*middle_const/len(xs)
	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < limit_1:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])
	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < limit_2:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*speed_const/len(xs)
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*speed_const/len(xs)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids.x,boids.y)

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids.x,boids.y))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
