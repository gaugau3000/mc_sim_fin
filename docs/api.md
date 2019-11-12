## mc_sim_fin.mc.mc_analysis

### mc_sim_fin.mc.mc_analysis(results: DataFrame, start_equity: float,ruin_equity: float, **kwargs)

| Type | name:Type | Informations |
| ------:| -----------:|-----------:|
| param1   | results: DataFrame | first column of the dataframe has to be the date of the trade and second the profit|
| param2   | start_equity: float | the equity you start trading with|
| param3   | ruin_equity: float | the equity you consider as a ruin |
| opt_param   | sim_years_duration:float | the duration of the simulation in years |
| opt_param   | nb_iterations:int | the number of iterations  |
| return   | :Dict | the result of the simulation |
