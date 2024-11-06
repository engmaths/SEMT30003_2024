#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pylab import *

# Some custom colors, just for fun! 
import matplotlib.colors as mcolors
# Bridget Riley's "Gather"
WHITE      = np.float32(mpl.colors.to_rgb('#f1f0e9'))
RUST       = np.float32(mpl.colors.to_rgb('#eb7a59'))
OCHRE      = np.float32(mpl.colors.to_rgb('#eea300'))
AZURE      = np.float32(mpl.colors.to_rgb('#5aa0df'))
TURQUOISE  = np.float32(mpl.colors.to_rgb('#00bac9'))
TEAL       = np.float32(mpl.colors.to_rgb('#00bac9'))
BLACK      = np.float32(mpl.colors.to_rgb('#44525c'))
GATHER     = [WHITE,RUST,OCHRE,AZURE,TURQUOISE,BLACK]
# A purple and green to round-out and complement the Gather pallet
MAUVE      = np.float32(mpl.colors.to_rgb('#b56ab6'))
MOSS       = np.float32(mpl.colors.to_rgb('#77ae64'))
OFFWHITE   = BLACK*.1+WHITE*.9
OFFBLACK   = BLACK*.9+WHITE*.1
# Other colors (just OK)
YELLOW     = np.float32(mpl.colors.to_rgb('#efcd2b'))
INDIGO     = np.float32(mpl.colors.to_rgb('#606ec3'))
VIOLET     = np.float32(mpl.colors.to_rgb('#8d5ccd'))
MAGENTA    = np.float32(mpl.colors.to_rgb('#cc79a7'))
CHARTREUSE = np.float32(mpl.colors.to_rgb('#b59f1a'))
VIRIDIAN   = np.float32(mpl.colors.to_rgb('#11be8d'))
CRIMSON    = np.float32(mpl.colors.to_rgb('#b41d4d'))
# I liked Virginia Rutten's color scheme
GOLD       = np.float32(mpl.colors.to_rgb('#ffd92e'))
TAN        = np.float32(mpl.colors.to_rgb('#765931'))
SALMON     = np.float32(mpl.colors.to_rgb('#fa8c61'))
GRAY       = np.float32(mpl.colors.to_rgb('#b3b3b3'))
LICHEN     = np.float32(mpl.colors.to_rgb('#63c2a3'))
RUTTEN     = [GOLD,TAN,SALMON,GRAY,LICHEN]
# Set line propert cycle for Matplotlib
COLORS     = [BLACK,WHITE,YELLOW,OCHRE,CHARTREUSE,MOSS,VIRIDIAN,TURQUOISE,AZURE,INDIGO,VIOLET,MAUVE,MAGENTA,RUST]
CYCLE      = [BLACK,RUST,TURQUOISE,OCHRE,AZURE,MAUVE,YELLOW,INDIGO]
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=CYCLE)
# Override defaults
mcolors.colorConverter.colors['r'] = RUST
mcolors.colorConverter.colors['g'] = MOSS
mcolors.colorConverter.colors['b'] = AZURE
mcolors.colorConverter.colors['y'] = OCHRE
mcolors.colorConverter.colors['m'] = MAUVE
mcolors.colorConverter.colors['c'] = TEAL



def hh_plot(tt, solution, I_apply, tstart, tstop):
    v,h,n,m = solution
    vmax = min(100,int(ceil(np.max(v))))

    T = tt[-1]
    opts = dict(solid_capstyle='butt',clip_on=False)
    
    figure(0,(6,3.8),120)
    
    subplot(211)
    plot(tt, v,label='voltage',**opts)

    axvspan(tstart,tstop,facecolor=(0.8,)*3,alpha=1,zorder=-1)
    text(tstart,vmax,"I = %s nA applied"%I_apply,ha='left',va='bottom')
    simpleraxis()
    
    xticks([])
    xlim(0,T)
    axhline(0,lw=0.6,color='k',linestyle=':')
    
    ylabel("Voltage (mv)")
    ylim(-70,vmax)
    yticks([-70,0,vmax])
    
    subplot(212)
    plot(tt, h, label='$h$: Na${}^{+}$ active', **opts)
    plot(tt, n, label='$n$: Na${}^{+}$ open'     , **opts)
    plot(tt, m, label='$m$: K${}^{+}$ open'      , **opts)
    base_legend(fudge=-.5,ncol=3)
    simpleraxis()
    
    xlabel("Time (ms)")
    xlim(0,T)
    
    ylabel("Fraction of Channels")
    ylim(0,1)
    yticks([0,1])
    
    gcf().align_ylabels()
    tight_layout()
    show()

def base_legend(*args,fudge=-0.1,**kwargs):
    '''
    Legend outside the plot on the base.

    Other Parameters
    ----------------
    fudge: padding between legend and axis, default -0.1
    '''
    lg = plt.legend(*args,**{**{
        'loc':'upper center',
        'bbox_to_anchor':(0.5,0.0+fudge),
        },**kwargs})
    lg.get_frame().set_linewidth(0.0)
    return lg


def simpleraxis(ax=None):
    '''
    Only draw the left y axis, nothing else
    
    Parameters
    ----------
    ax: maplotlib.Axis; default ``plt.gca()``
    '''
    if ax is None: ax=plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.autoscale(enable=True, axis='x', tight=True)