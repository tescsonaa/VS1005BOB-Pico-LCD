# define constant value 
display_interval=1000   # milli second

# define icon on/off voltage 
value_good_solar=8.0      # if reach value, icon on white colour, otherwise gray colour 
value_good_battery=8.0
value_good_adaptor=8.0
value_good_renew=3.0

# define max voltage of 4 bar 
solar_value_max=20 
battery_value_max=15 
adaptor_value_max=20 
renew_value_max=8

max_v=50.0   # max voltage display 
max_c=5.0    # max current display

# top position 
clock_x=65
clock_y=15

# bottom position 
bar_x=15
bar1_y=115
bar2_y=bar1_y+10
bar3_y=bar2_y+10
bar4_y=bar3_y+10

percentage_total_sector=20  # gangue 80x80 20 sectors


# Define Position 
circle1_x=10     # solar
circle1_y=10
circle2_x=125    # battery
circle2_y=10
circle3_x=25     # adaptor
circle3_y=130
circle4_x=130    # renew
circle4_y=130

gauges_x=0
gauges_y=0
gauges_solar_x=20
gauges_solar_y=30
gauges_battery_x=120
gauges_battery_y=30
gauges_adaptor_x=20
gauges_adaptor_y=150
gauges_renew_x=120
gauges_renew_y=150

gauges_solar_value_x=40
gauges_solar_value_y=gauges_solar_y+23
gauges_battery_value_x=140
gauges_battery_value_y=gauges_battery_y+23
gauges_adaptor_value_x=40
gauges_adaptor_value_y=gauges_adaptor_y+23
gauges_renew_value_x=140
gauges_renew_value_y=gauges_renew_y+23


# icon position - solar, battery, renew icons 
icon_x=255
icon1_y=50          
icon2_y=icon1_y+60
icon3_y=icon2_y+60

# somazing position
somazing_x=230
somazing_y=220




# time = interval x 2, eg, interval=15, delay time=30sec
# MQTT update time 
heartbeat_interval=15



# Define global variables 
def init():
    global v_solar    
    global v_battery 
    global v_adaptor
    global v_renew
    global c_solar
    global c_battery
    global c_adaptor
    global c_renew
    global p_solar
    global p_battery
    global p_adaptor
    global p_renew
    
    global device_id

#    global rxData
#    global txData