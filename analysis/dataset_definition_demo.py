from ehrql import show, create_dataset, codelist_from_csv
from ehrql.tables.core import patients, clinical_events, practice_registrations

index_date = "2024-03-31"

dataset = create_dataset()
dataset.configure_dummy_data(population_size=1000)

# Patient is alive

# Patient is aged 17 years or older 

# Patient has unresolved diagnosis of depression

show(patients)