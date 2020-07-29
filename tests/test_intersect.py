from src.pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from src.pygeo.objects import Ray, Sphere, Triangle,Point,Vector
import numpy as np 


# Test cases for intersect

# 1.test _intersect_ray_with_sphere
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


# 2.  _intersect_ray_with_triangle
def test_traingle_ray_intersection_return_true():
    '''Test case : ray and traingle having an intersection point
        Traingle : vertices (2,0,0) , (5,0,0) , (2,5,0)
        Ray : Begin(3,1,2) , direction (0,0,-1)
        Expected result : True'''
    a = Point((2,0,0))
    b = Point((5,0,0))
    c = Point((2,5,0))

    point_b = Point((3,1,2))
    vector_vb = Vector((0,0,-1))
    ray_b = Ray(point_b,vector_vb)
    traingle_a = Triangle(a,b,c)
    assert_flag,_ = _intersect_ray_with_triangle(ray_b,traingle_a)
    assert (assert_flag) is True

def test_traingle_ray_no_intersection_return_false():

    '''Test case : ray and traingle having no intersection point
        Traingle : vertices (2,0,0) , (5,0,0) , (2,5,0)
        Ray : Begin(1,4,1) , direction (0,0,-1)
        Expected result : Flase'''
    a = Point((2,0,0))
    b = Point((5,0,0))
    c = Point((2,5,0))

    point_b = Point((1,4,1))
    vector_vb = Vector((0,0,-1))
    ray_b = Ray(point_b,vector_vb)
    traingle_a = Triangle(a,b,c)
    assert_flag,_ = _intersect_ray_with_triangle(ray_b,traingle_a)
    assert (assert_flag) is False
