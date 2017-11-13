from modules import clv,outcome,survival
import pandas


def execute_optimal_pricing_model():

    # Execute the pipeline
    
    o_df = outcome.run()
    
    s_df = survival.run()

    clv_df = clv.run(o_df,s_df)


execute_optimal_pricing_model()




