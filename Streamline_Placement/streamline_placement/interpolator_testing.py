from functions_streamline_placement import interpolator
from functions_mesh_creation import mesh_creation

nx, ny, nz = 10, 10, 10
datafileXmZM = "Test_Case_Ones.csv"
datafileXMZm = "Test_case_Ones.csv"
point = [4.,6.,3.]
method = "nearest"

mesh_pyvista, mesh_scipy, u_list, v_list, w_list = mesh_creation(nx, ny, nz, datafileXmZM, datafileXMZm)

vector1 = interpolator(mesh_scipy, u_list, v_list, w_list, point, method)

def interpolator2(mesh_pyvista, point):
    closest_point_index = mesh_pyvista.find_closest_point(point, n=1)
    #closest_point = mesh_pyvista.point[closest_point_index]
    closest_defined_vector = mesh_pyvista["vectors"][closest_point_index]
    return closest_defined_vector

vector2 = interpolator2(mesh_pyvista, point)