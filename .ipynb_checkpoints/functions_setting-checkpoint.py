# this script is set to gather all the function that I will use in the differentes script 
# Through the different script and the analysis I will performe I will add different function 


import numpy as np

#import delta_exp as delta_exp
#import Ek_flux as Ek_flux
 

####### Function to get the Displacement thicness, the Delta 95% and the velocity far from the boundary ######



def delta_exp(num_exp, cam):
    '''This function computes the displacement thickness.
    Variables: 
    - num_exp: Index of the experiment.
    - cam: Camera type, must be either 'jai' or 'stereo'.'''
    
    # Setting parameters based on camera type
    if cam == 'jai':
        time = time_jai[num_exp]  # Time array for JAI camera
        u = -ubar_jai[num_exp]    # Velocity array for JAI camera, negated
        dy = dy_jai               # Spatial resolution for JAI camera
        y = Coord_y_jai           # Y-coordinates for JAI camera
        ny = Coord_y_jai.size     # Number of Y-coordinates for JAI camera
    elif cam == 'stereo':
        time = time_stereo[num_exp]  # Time array for Stereo camera
        u = -ubar_stereo[num_exp]    # Velocity array for Stereo camera, negated
        dy = dy_stereo               # Spatial resolution for Stereo camera
        y = Coord_y_stereo           # Y-coordinates for Stereo camera
        ny = Coord_y_stereo.size     # Number of Y-coordinates for Stereo camera
    else:
        return "The variable (cam) must be either 'jai' or 'stereo'"

    # Declaration of the output variables
    d1 = np.zeros(time.size)  # Displacement thickness array
    d95_1 = np.zeros(time.size)  # Delta 95% array for case 1
    d95_2 = np.zeros(time.size)  # Delta 95% array for case 2
    Uout = np.zeros(time.size)   # Far field velocity array
    
    # Main loop over time steps
    for it in range(time.size):
        Umax = np.nanmax(u[:, it])  # Maximum velocity at the current time step
        idMax = (np.int64(np.where(u[:, it] == Umax)))[0][0]  # Index of the maximum velocity
        
        if cam == 'jai':
            Uinfty = np.nanmean(u[-40:, it], axis=0)  # Mean velocity over the last 4 cm for JAI
            Uout[it] = Uinfty
        elif cam == 'stereo':
            Uinfty = np.nanmean(u[-10:, it], axis=0)  # Mean velocity over the last 1 cm for Stereo
            Uout[it] = Uinfty
        else:
            print("The variable (cam) must be either 'jai' or 'stereo'")
        
        # Check if the maximum velocity is in the lower part of the column
        if idMax < 2 * ny // 3:
            # Looking for indices and values above the maximum velocity point
            valid_indices_1 = np.arange(idMax + 1, len(u[:, it]))
            valid_values_1 = np.abs(u[valid_indices_1, it] - 0.95 * Uinfty)
            
            if np.all(np.isnan(valid_values_1)):
                id95_1 = -1  # Indicate no valid index found
            else:
                valid_values_1 = np.where(np.isnan(valid_values_1), np.inf, valid_values_1)
                id95_1 = valid_indices_1[np.nanargmin(valid_values_1)]
            
            # Looking for indices and values below the maximum velocity point
            valid_indices_2 = np.arange(0, idMax)
            valid_values_2 = np.abs(u[valid_indices_2, it] - 0.95 * Uinfty)
            
            if np.all(np.isnan(valid_values_2)):
                id95_2 = -1  # Indicate no valid index found
            else:
                valid_values_2 = np.where(np.isnan(valid_values_2), np.inf, valid_values_2)
                id95_2 = valid_indices_2[np.nanargmin(valid_values_2)]
            
            # Assign the y-coordinates for the delta 95% values
            d95_1[it] = y[id95_1] if id95_1 != -1 else np.nan
            d95_2[it] = y[id95_2] if id95_2 != -1 else np.nan
        
        else:
            # Calculate the delta 95% values when the maximum velocity is not in the lower part
            id95_1 = np.nanargmin(np.abs(u[:, it] - 0.95 * Uinfty))
            id95_2 = np.nanargmin(np.abs(u[:, it] - 0.95 * Uinfty))
            d95_1[it] = y[id95_1]
            d95_2[it] = y[id95_2]
        
        # Calculate the displacement thickness
        d1[it] = np.sum((1 - u[:, it] / Uinfty) * dy)
    
    return d1, d95_1, d95_2, Uout


#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


# Function to compute Ekman flux
def EK_flux(num_exp):
    '''This function computes the Ekman flux.
    Variables:
    - num_exp: Index of the experiment.
    '''

    # Retrieve data specific to the experiment from the stereo camera
    time = time_stereo[num_exp]        # Time array for the Stereo camera
    u = -ubar_stereo[num_exp]          # Velocity array for the Stereo camera, negated
    dy = dy_stereo                     # Spatial resolution for the Stereo camera
    y = Coord_y_stereo                 # Y-coordinates for the Stereo camera
    ny = Coord_y_stereo.size           # Number of Y-coordinates for the Stereo camera
    v = vbar_stereo[num_exp]           # Transverse velocity array for the Stereo camera

    # Initialize the Ekman flux array
    flx_Ek = np.zeros(len(time))       # Ekman flux array, initialized to zeros

    # Main loop over time steps
    for it in range(time.size):
        # Compute the Ekman flux at each time step by summing the product of transverse velocity and spatial resolution
        flx_Ek[it] = np.sum(v[:, it] * dy)

    # Return the computed Ekman flux array
    return flx_Ek



