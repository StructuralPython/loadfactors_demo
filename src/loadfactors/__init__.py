"""
A library for calculating structural factored loads as per your local building code
"""

__version__ = "0.0.1"

from loadfactors.loadfactors import (
    Load,
    open_load_combinations,
    factored_max,
    factored_min,
    factored_max_trace,
    factored_min_trace,
    get_factored_matrix,
    factor_load,
    alias_to_service_loads
)