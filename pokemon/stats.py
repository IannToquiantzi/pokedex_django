import pandas as pd
import numpy as np
from .models import Pokemon

def get_stats():
    data = Pokemon.objects.all().values()
    df = pd.DataFrame(list(data))
    
    if df.empty:
        return {}
    
    return{
        'average_height': df['height'].mean(),
        'average_weight': df['weight'].mean(),
        'average_base_experience': df['base_experience'].mean()
    }