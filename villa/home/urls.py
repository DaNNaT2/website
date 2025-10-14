from django.urls import path
from .views import *

urlpatterns = [
    path( '', home, name='home'),
    path( 'double_standard', two_p, name='2p'),
    path( 'triple_standard', tree_p, name='3p'),
    path( 'quadruple_standard', four_p, name='4p'),
    path( 'triple_standard_kitchen', tree_p_coc, name='3p_coc'),
    path( 'double_comfort', two_comf, name='2p_c'),
    path( 'triple_comfort', tree_comf, name='3p_c'),
    path( 'double_famile', two_f, name='2_room'),
    path( 'double_apart', tree_ap, name='3_room'),
    path( 'house', house, name='house'),
    path( 'inform', dop_inf, name='inform'),
]