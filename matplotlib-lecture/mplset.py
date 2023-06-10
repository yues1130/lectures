import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker

#rcParams_default = mpl.rcParamsDefault
rcParams_default = { # dpi only
     'figure.dpi'           : 600
    ,'savefig.dpi'          : 600
    }

rcParams_nat = {
    # font
     'font.family'          : 'Arial' # or 'Helvetica' or 'STIXGeneral' for theoretical works
    ,'font.size'            : 8.0
    #,'mathtext.fontset'     : 'stix'
    
    # x tick
    ,'xtick.major.size'     : 2
    ,'xtick.minor.size'     : 1.5
    ,'xtick.major.width'    : 0.75
    ,'xtick.minor.width'    : 0.75
    ,'xtick.labelsize'      : 8.0
    ,'xtick.direction'      : 'in'
    ,'xtick.top'            : True
    
    # y tick
    ,'ytick.major.size'     : 2
    ,'ytick.minor.size'     : 1.5
    ,'ytick.major.width'    : 0.75
    ,'ytick.minor.width'    : 0.75
    ,'ytick.labelsize'      : 8.0
    ,'ytick.direction'      : 'in'
    ,'ytick.right'          : True
    
    # pad
    ,'xtick.major.pad'      : 2
    ,'xtick.minor.pad'      : 2
    ,'ytick.major.pad'      : 2
    ,'ytick.minor.pad'      : 2
    
    # axes
    ,'figure.figsize'       : (3.4, 3.4*0.7) # width, height [unit: inch]
    # size -> size of bounding-box (canvas or artwork)
    ,'figure.dpi'           : 600
    ,'savefig.dpi'          : 600
    ,'axes.unicode_minus'   : False
    ,'axes.linewidth'       : 0.75
    ,'lines.linewidth'      : 1.0
    
    }

#import matplotlib as mpl
mpl.rcParams.update(rcParams_default)
#mpl.rcParams.update(rcParams_nat)

