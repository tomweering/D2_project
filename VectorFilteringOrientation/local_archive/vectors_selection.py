from compas_rhino.artists import PolylineArtist
from compas_rhino.artists import VectorArtist
from compas_rhino.artists import PointArtist
import compas_rhino
from compas.geometry import Point

str = compas.json_load('streaml_rdp_lr.json')
vec = compas.json_load('streamlines_vec_l.json')
loc = compas.json_load('streamlines_loc_l.json')


for i in str:
    str_art = PolylineArtist(i)
    str_art.draw(show_points=True)
    
    
for j in range(len(vec)):
    vec_art = VectorArtist(vec[j])
    vec_art.draw(point=loc[j])