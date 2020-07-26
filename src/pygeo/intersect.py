from .objects import Ray, Sphere, Triangle
import numpy as np 
import math as m 


def intersect(first_object, second_object):
    ...


def _intersect_ray_with_sphere(ray, sphere):

    if isinstance(ray,Ray) and isinstance(sphere,Sphere):

        intersection_points = []

        ray_origin = ray.origin._point
        ray_direction = ray.direction._vector
        sphere_center = sphere.center._point
        sphere_radius = sphere.radius 

        a = np.dot(ray_direction,ray_direction)
        b = 2*np.dot(ray_direction,ray_origin-sphere_center)
        c = np.dot(ray_origin-sphere_center,ray_origin-sphere_center) - sphere_radius**2

        discriminant = b**2 - 4*a*c

        if m.isclose(discriminant,0):
            t = -(b/2*a)
            point_1 = ray_origin + t*ray_direction
            #intersection_points = np.append(intersection_points,point_1.tolist())
            intersection_points.append(point_1.tolist())
            return 1,intersection_points
        
        elif discriminant > 0:
            t_0 = (-b + m.sqrt(discriminant))/2*a
            t_1 = (-b - m.sqrt(discriminant))/2*a
            point_0 = ray_origin + t_0*ray_direction
            point_1 = ray_origin + t_1*ray_direction
            intersection_points.append(point_0.tolist())
            intersection_points.append(point_1.tolist())
            print(intersection_points)
            return 2,intersection_points
        else:
            return 0,intersection_points
    else:
        return NotImplemented



def _intersect_ray_with_triangle(ray, triangle):
    ...
