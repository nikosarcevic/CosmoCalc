# %%
import numpy as np
import matplotlib.pyplot as plt
import yaml

def plot_distances(z_array, rz_array, trz_array, DLz_array, DAz_array):
        
        fig, ax = plt.subplots(figsize=(width, height))
        
        colors = {
         'orange' : '#ffc345',
         'gray' : '#333333',
         'white' : '#FFFFFF',
        }
        
        ax.spines['bottom'].set_color(colors['orange'])
        ax.spines['top'].set_color(colors['orange']) 
        ax.spines['right'].set_color(colors['orange'])
        ax.spines['left'].set_color(colors['orange'])

        ax.tick_params(axis='x', colors=colors['orange'])
        ax.tick_params(axis='y', colors=colors['orange'])

        ax.yaxis.label.set_color(colors['orange'])
        ax.xaxis.label.set_color(colors['orange'])
        
        for axis in ['top','bottom','left','right']:
            ax.spines[axis].set_linewidth(3)

        ax.tick_params(width=3)
        ax.tick_params(axis='both', labelsize=12)

        ax.set_facecolor(colors['white'])
        fig.patch.set_facecolor(colors['white'])
   
        if plot_rz:
            myplot = ax.plot(z_array, rz_array, label='Comoving Distance', color=colors['gray'], ls='-', lw=3)
        if plot_trz:
            myplot = ax.plot(z_array, trz_array, label='Transverse Comoving Distance', color=colors['gray'], ls='-.', lw=3)
        if plot_DLz:
           myplot = ax.plot(z_array, DLz_array, label='Luminosity Distance', color=colors['gray'], ls='--', lw=3)
        if plot_DAz:
            myplot = ax.plot(z_array, DAz_array, label='Angular Diameter Distance', color=colors['gray'], ls=':', lw=3)
        

        legend = plt.legend(frameon = 1)
        plt.setp(legend.get_texts(), color=colors['gray'])
        frame = legend.get_frame()
        frame.set_facecolor(colors['white'])
        frame.set_edgecolor(colors['white'])

        ax.set_xlabel('Redshift', size=15)
        ax.set_ylabel('Distance [Mpc]', size=15)
        
        return myplot
        
