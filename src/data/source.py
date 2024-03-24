from __future__ import annotations
from dataclasses import dataclass
import pandas as pd
from typing import Optional
from .loader import DataSchema
import plotly.express as px

@dataclass
class DataSource:
    _data: pd.DataFrame

    # Creating a custom color map
    # custom_colors = px.colors.qualitative.Vivid

    def filter(self,
               years: Optional[list[str]] = None,
               districts: Optional[list[str]] = None
               ) -> DataSource:
        if districts is None:
            districts = self.get_all_generic(DataSchema.AREA)
        if years is None:
            years = self.unique_years
        filtered_data = self._data[self._data[DataSchema.AREA].isin(districts) & self._data[DataSchema.DATE].dt.year.isin(years)]
        return DataSource(filtered_data)
    
    
    def get_all_generic(self, column_name):
        return self._data[column_name].tolist()
    
    
    def get_unique_generic(self, column_name):
        return set(self.get_all_generic(column_name))
    
    @property
    def all_years(self) -> list[str]:
        return self._data["DATE OCC"].dt.year.tolist()
    
    @property
    def unique_years(self) -> list[str]:
        return sorted(set(self.all_years), key=int)
    
    def truncate_names(self, names, max_length=20, ellipsis='...'):
        return [name[:max_length] + ellipsis if len(name) > max_length else name for name in names]
    
    @property
    def row_count(self) -> int:
        return self._data.shape[0]
    
    
    def create_pivot_table(self, column_name: str, topX :Optional[int] =10) -> pd.DataFrame:
        counts = self._data.groupby(column_name).size().nlargest(topX)
        # Truncate long Crime names
        counts.index = self.truncate_names(counts.index)
        # Creating a DataFrame for Plotly Express
        return pd.DataFrame({column_name: counts.index, 'Frequency': counts.values})
    
    
    def monthly_crime_counts(self, freq: str = 'ME') -> pd.DataFrame:
        # Group by month and count occurrences
        monthly_counts = self._data.groupby(pd.Grouper(key=DataSchema.DATE, freq=freq)).size()
        
        # Reset index to access month as a column
        monthly_counts = monthly_counts.reset_index()
        
        # Rename columns
        monthly_counts.columns = ['Month', 'Number of Crimes']
        
        # Convert 'Month' column to string format for better display
        monthly_counts['Month'] = monthly_counts['Month'].dt.strftime('%b')
        
        return monthly_counts