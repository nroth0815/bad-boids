from boids import update_boids, Boids
from nose.tools import assert_almost_equal
import os
import yaml

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data_in=regression_data["before"]
    boid_data=Boids(input_list=boid_data_in, flag=1)
    update_boids(boid_data)
    for after,before in zip(regression_data["after"],[boid_data.x,boid_data.y,boid_data.x_velocity, boid_data.y_velocity]):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
	
