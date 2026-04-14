import pandas as pd
import numpy as np
from .models import Pokemon

def get_stats():
    data = Pokemon.objects.all().values()
    df = pd.DataFrame(list(data))
    
    if df.empty:
        return {}
    
    return{
        'average_height': np.mean(df['height']),
        'average_weight': np.mean(df['weight']),
        'average_base_experience': np.mean(df['base_experience'])
    }