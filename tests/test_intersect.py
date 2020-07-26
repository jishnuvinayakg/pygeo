from src.pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from src.pygeo.objects import Ray, Sphere, Triangle,Point,Vector
import numpy as np 


# intersect


# test _intersect_ray_with_sphere
def test_ray_sphere_intersection_2_point_return_true():
    '''Test case : intersection of ray @ 2 points with a sphere. 
       Sphere : center [0,0,0], radius = 5
       Ray : Begin [-6,3,0], direction[1,0,0]
       Expected intersection points : [-4,3,0] & [4,3,0]'''
    point_1 =[-4,3,0]
    point_2 =[4,3,0]
    assert_flag = False
    ray = Ray(Point((-6,3,0)),Vector((1,0,0)))
    sphere = Sphere(Point((0,0,0)),5)
    num_intersection_point,points = _intersect_ray_with_sphere(ray,sphere)
    if ((points[0] == point_1 or points[0] == point_2) and 
    (points[1] == point_1 or points[1] == point_2)):
        assert_flag = True
    assert(num_intersection_point==2 and assert_flag)is True

def test_ray_sphere_intersection_1_point_return_true():
    '''Test case : intersection of ray @ 1 point with a sphere. 
       Sphere : center [0,0,0], radius = 5
       Ray : Begin [-6,5,0], direction[1,0,0]
       Expected intersection points : [0,5,0] '''
    point_3 =[0.0,5.0,0.0]
    assert_flag = False
    ray = Ray(Point((-6,5,0)),Vector((1,0,0)))
    sphere = Sphere(Point((0,0,0)),5)
    num_intersection_point,points = _intersect_ray_with_sphere(ray,sphere)
    print(point_3)
    print(points[0])
    print(points[0] == point_3)
    if points[0] == point_3:
        assert_flag = True

    assert(num_intersection_point==1 and assert_flag)is True

def test_ray_sphere_no_intersection_return_true():
    '''Test case : intersection of ray @ 0 point with a sphere. 
       Sphere : center [0,0,0], radius = 5
       Ray : Begin [-6,6,0], direction[1,0,0]
       Expected intersection points : No intersection '''
    ray = Ray(Point((-6,6,0)),Vector((1,0,0)))
    sphere = Sphere(Point((0,0,0)),5)
    num_intersection_point,_ = _intersect_ray_with_sphere(ray,sphere)
    assert(num_intersection_point==0)is True


# _intersect_ray_with_triangle
