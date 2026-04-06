import os
import matplotlib.pyplot as plt

def save_plot(fig_name, folder='eda'):
    """Saves plots to the specified directory."""
    base_path = os.path.join('..', 'plots', folder)
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    save_path = os.path.join(base_path, fig_name)
    plt.savefig(save_path, bbox_inches='tight', dpi=300)
    print(f"Plot saved: {save_path}")