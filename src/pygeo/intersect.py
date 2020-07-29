from .objects import Ray, Sphere, Triangle,Point
import numpy as np 
import math as m 


def intersect(first_object, second_object):
    ...


def _intersect_ray_with_sphere(ray, sphere):
    '''Function to find the point of intersection of sphere and a ray'''

    if isinstance(ray,Ray) and isinstance(sphere,Sphere):

        intersection_points = []
        #Define ray and sphere
        ray_origin = ray.origin._point
        ray_direction = ray.direction._vector
        sphere_center = sphere.center._point
        sphere_radius = sphere.radius 
        #Finding the discriminant
        a = np.dot(ray_direction,ray_direction)
        b = 2*np.dot(ray_direction,ray_origin-sphere_center)
        c = np.dot(ray_origin-sphere_center,ray_origin-sphere_center) - sphere_radius**2
        discriminant = b**2 - 4*a*c

        if m.isclose(discriminant,0):
            #Condition for 1 point of intersection
            t = -(b/2*a)
            point_1 = ray_origin + t*ray_direction
            intersection_points.append(point_1.tolist())
            return 1,intersection_points
        elif discriminant > 0:
             #Condition for 2 point of intersection
            t_0 = (-b + m.sqrt(discriminant))/2*a
            t_1 = (-b - m.sqrt(discriminant))/2*a
            point_0 = ray_origin + t_0*ray_direction
            point_1 = ray_origin + t_1*ray_direction
            intersection_points.append(point_0.tolist())
            intersection_points.append(point_1.tolist())
            print(intersection_points)
            return 2,intersection_points
        else:
            #Condition for no intersection
            return 0,intersection_points
    else:
        return NotImplemented



def _intersect_ray_with_triangle(ray, triangle):
    '''Function to find the point of intersection of triangle and a ray'''
    #ray
    r0 = ray.origin._point
    v = ray.direction._vector
    #traingle
    v0 = triangle.A._point
    v1 = triangle.B._point
    v2 = triangle.C._point
    #normal to traingle
    n = np.cross((v1-v0),(v2-v0))

    p_intsct = []

    if m.isclose(np.dot(n,v),0):
        return False,p_intsct
    else:
        #finding intersection first
        t = np.dot((v0-r0),n)/np.dot(n,v)
        if t <= 0:
            return False,p_intsct
        p_intsct = Point(r0 + t*v)
        #check if the point lies inside the traingle
        edge0 = v1-v0
        edge1 = v2-v1
        edge2 = v0-v2
        C0 = p_intsct._point - v0
        C1 = p_intsct._point - v1
        C2 = p_intsct._point - v2
        dot_edge0 = np.dot(n,np.cross(edge0,C0))
        dot_edge1 = np.dot(n,np.cross(edge1,C1))
        dot_edge2 = np.dot(n,np.cross(edge2,C2))

        if dot_edge0 >=0 and dot_edge1 >=0 and dot_edge2 >=0:
            return True,p_intsct
        else:
            return False,p_intsct

