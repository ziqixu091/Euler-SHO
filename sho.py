k = 1   # spring constant in N/m
m = 0.5 # mass in kg

# no automatic scaling of window
scene.autoscale=0
scene.width=380
scene.range=10.0

# use a standard Python 3D object to represent particle
ball=sphere(radius=1.,pos=vector(0.,4.0,0),color=color.red)
ball.vel=vector(0,0,0)  # velocity vector of mass
spring=helix(pos=vector(0.,10.0,0),axis=ball.pos-vector(0,10,0), radius=.6, coils=10, color=color.white, thickness=0.2)  # create a spring object for plotting

dt=0.01
t=0

# loop over time (for ever!)
while 1:
    rate(300)
    t=t+dt
    ball.pos=ball.pos+ball.vel*dt  #find new position from velocity
    
    Fspring = -k*ball.pos   # restoring force from Hooke's law
    Fdrag = -0.2*ball.vel   # drag force
    Fnet = Fspring          # calculate net force
    a   = Fnet/m            # acceleration due to net force
    
    ball.vel=ball.vel+a*dt  # find new velocity from acceleration
    
    spring.axis=ball.pos-vector(0., 10., 0) #update spring length in plot